from django.http import HttpResponse
from polls.question import saveQuestion
from django.core.serializers import serialize


# Create your views here.

def index(request):
    question = saveQuestion()
    result = serialize('json', [question, ])
    print(result)
    return HttpResponse(result)
