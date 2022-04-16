import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'innowisedjango.settings')

app = Celery('innowisedjango')
app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task
def add(x, y):
    return x + y


@app.task
def summa(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args[0])