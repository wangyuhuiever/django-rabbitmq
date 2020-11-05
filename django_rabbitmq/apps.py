from django.apps import AppConfig
from django.conf import settings
from threading import Thread


class DjangoMqConfig(AppConfig):
    name = 'django_rabbitmq'

    def ready(self):
        thr = Thread(name='mq_thread', target=self.run_mq)
        thr.daemon = True
        thr.start()

    def run_mq(self):
        mq_settings = settings.RABBITMQ.get('default')
        from .mq import RabbitMQ

        mq = RabbitMQ(
            mq_settings.get('HOST'),
            mq_settings.get('PORT'),
            mq_settings.get('VIRTUAL_HOST'),
            mq_settings.get('USER'),
            mq_settings.get('PASSWORD'),
        )

        mq.start_mq(mq_settings.get('QUEUE'))
