===========================
Django RabbitMQ Integration
===========================

Start a RabbitMQ consumer after django server start.

Quick start
-----------

1. Add "django-rabbitmq" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_rabbitmq',
    ]

2. Config rabbitmq settings like this::

    RABBITMQ = {
        'default': {
            'HOST': 'server_ip',
            'PORT': 5672,
            'VIRTUAL_HOST': '/',
            'USER': 'user',
            'PASSWORD': 'password',
            'QUEUE': 'queue'
        }
    }

3. Create a mq.py and inherit RabbitMQ model::

    from django_rabbitmq.mq import RabbitMQ


    class CustomModel(RabbitMQ):

        def callback(self, ch, method, properties, body):
            print("[django-rabbitmq] Received %r" % body)
            ......
            your code
            ......

    RabbitMQ.callback = CustomModel.callback


