#! -*- coding: utf-8 -*-
import pika


class RabbitMQ(object):

    def __init__(self, host, port, virtual_host, user, password):
        credentials = pika.PlainCredentials(user, password)
        parameters = pika.ConnectionParameters(host=host, port=port, virtual_host=virtual_host, credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)

    def start_mq(self, queue):
        channel = self.connection.channel()
        channel.queue_declare(queue=queue)

        channel.basic_consume(queue=queue, on_message_callback=self.callback, auto_ack=True)

        print('[django-rabbitmq] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    @staticmethod
    def callback(ch, method, properties, body):
        print("[django-rabbitmq] Received %r" % body)

