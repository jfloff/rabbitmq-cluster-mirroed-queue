#!/usr/bin/env python3
import pika
import sys

port = int(sys.argv[1])
EXCHANGE = 'rabbit1' if port == 5672 else 'rabbit2'
QUEUE = 'write-home-timeline'
creds = pika.PlainCredentials('admin', 'admin')

#------------------------------
# Receive message on Rabbit2
#------------------------------
rabbit2 = pika.ConnectionParameters(host='localhost', port=port, credentials=creds)

# create connection and channel
rabbit2_connection = pika.BlockingConnection(rabbit2)
rabbit2_channel = rabbit2_connection.channel()

rabbit2_channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')

# result = channel.queue_declare('', exclusive=True)
# queue_name = result.method.queue
# rabbit2_channel.queue_declare(QUEUE, exclusive=True)

rabbit2_channel.queue_bind(exchange=EXCHANGE, queue=QUEUE, routing_key=EXCHANGE)

def callback(ch, method, properties, body):
  print(f" [{port}-{EXCHANGE}] [x] {method.routing_key}:{body.decode()}")

rabbit2_channel.basic_consume(queue=QUEUE, on_message_callback=callback, auto_ack=True)

print(f' [{port}-{EXCHANGE}] [*] Waiting for logs. To exit press CTRL+C')
rabbit2_channel.start_consuming()

# close connection
# rabbit2_channel.close()
# rabbit2_connection.close()