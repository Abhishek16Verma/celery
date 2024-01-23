from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.http import HttpResponse
from myapp.tasks import add

def my_view(request):
    result = add.delay(4, 4)
    return HttpResponse(f'Task {result.task_id} is now processing in the background.')
