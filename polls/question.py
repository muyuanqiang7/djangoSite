from polls.models import Question, Choice
from django.utils import timezone


def saveQuestion():
    question = Question(question_text="what's new", pub_date=timezone.now())
    question.save()
    return question;
