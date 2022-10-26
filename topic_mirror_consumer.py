#!/usr/bin/env python3
import pika
import sys

port = int(sys.argv[1])
creds = pika.PlainCredentials('admin', 'admin')
rabbit2 = pika.ConnectionParameters(host='localhost', port=port, credentials=creds)

# create connection and channel
rabbit2_connection = pika.BlockingConnection(rabbit2)
rabbit2_channel = rabbit2_connection.channel()

EXCHANGE = 'notifications'
rabbit2_channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')

queues = []

# if port == 5672:
#   queues << {
#     'name': 'write-home-timeline-eu'
#     'routing_key': str(5672),
#   }
# elif port == 5673:
#   queues << {
#     'name': 'write-home-timeline-us'
#     'routing_key': str(5673),
#   }

queues.append({
  'name': 'write-home-timeline-eu',
  'routing_key': str(5672),
})
queues.append({
  'name': 'write-home-timeline-us',
  'routing_key': str(5673),
})

# result = rabbit2_channel.queue_declare('', exclusive=True)
# queue_name = result.method.queue

def callback(ch, method, properties, body):
  print(f" [x] [{EXCHANGE}:{method.routing_key}] Received: {body.decode()}")

for queue in queues:
  rabbit2_channel.queue_bind(exchange=EXCHANGE, queue=queue['name'], routing_key=queue['routing_key'])
  rabbit2_channel.basic_consume(queue=queue['name'], on_message_callback=callback, auto_ack=True)
  print(f" [*] Waiting for logs [{EXCHANGE}:{queue['routing_key']}--{queue['name']}]. To exit press CTRL+C")

rabbit2_channel.start_consuming()

# close connection
# rabbit2_channel.close()
# rabbit2_connection.close()