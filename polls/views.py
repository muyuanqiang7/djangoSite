from django.shortcuts import render
from django.http import HttpResponse
from polls.question import saveQuestion
from django.core.serializers import serialize


# Create your views here.

def index(request):
    question = saveQuestion()
    print(serialize('json', question))
    return HttpResponse("Hello World from django backend!")
