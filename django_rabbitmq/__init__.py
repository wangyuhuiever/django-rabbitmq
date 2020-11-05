import os

if not os.environ.get('RUN_MAIN', None):
    default_app_config = 'django_rabbitmq.apps.DjangoMqConfig'
