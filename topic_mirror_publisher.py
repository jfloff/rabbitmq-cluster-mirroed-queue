#!/usr/bin/env python3
import pika
from datetime import datetime

EXCHANGE = 'rabbit1'
QUEUE = 'write-home-timeline'
creds = pika.PlainCredentials('admin', 'admin')
message = str(datetime.now())

#------------------------------
# Publish message on Rabbit1
#------------------------------
rabbit1 = pika.ConnectionParameters(host='localhost', port=5672, credentials=creds)

# create connection and channel
rabbit1_connection = pika.BlockingConnection([rabbit1])
rabbit1_channel = rabbit1_connection.channel()

# declare topic
rabbit1_channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')

# publish message
rabbit1_channel.basic_publish(exchange=EXCHANGE, routing_key=EXCHANGE, body=message)
print(" [x] Sent %r:%r" % (QUEUE, message))

# close connection
rabbit1_channel.close()
rabbit1_connection.close()
