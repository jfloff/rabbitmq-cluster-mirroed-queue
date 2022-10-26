#!/usr/bin/env python3
import pika
import sys
from datetime import datetime

port = int(sys.argv[1])
creds = pika.PlainCredentials('admin', 'admin')
rabbit1 = pika.ConnectionParameters(host='localhost', port=port, credentials=creds)

# create connection and channel
rabbit1_connection = pika.BlockingConnection([rabbit1])
rabbit1_channel = rabbit1_connection.channel()

# declare topic
EXCHANGE = 'notifications'
rabbit1_channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')

# publish message
message = str(datetime.now())
rabbit1_channel.basic_publish(exchange=EXCHANGE, routing_key=str(port), body=message)
print(f" [x] [{EXCHANGE}:{port}] Sent: {message}")

# close connection
rabbit1_channel.close()
rabbit1_connection.close()
