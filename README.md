# Cluster RabbitMQ wiht Mirroed Queues :rabbit: :crystal_ball:

Running example of the RabbitMQ with mirroed queues [tutorial](https://bhoey.com/blog/high-availability-rabbitmq-with-mirrored-queues/).

## Run

Start the RabbitMQ cluster:
```
> git clone https://github.com/jfloff/rabbitmq-cluster-mirroed-queue.git
> cd rabbitmq-cluster-mirroed-queue
> docker-compose up
```

Run the test:
```
> pip install pika
> ./test.py
```

## Config
Most things will be how you expect:
* The default username and password are `admin`/`admin`
* The broker accepts connections on `localhost:5672[3]`
* The Management interface is found at `localhost:15672[3]`