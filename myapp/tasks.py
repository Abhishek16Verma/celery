# myapp/tasks.py
from celery import Celery

app = Celery('myapp', broker='pyamqp://guest:guest@localhost//')

@app.task
def add(x, y):
    return x + y
