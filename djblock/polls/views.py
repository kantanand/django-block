from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from polls.decorators import user_is_entry_author

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = "nox questions"
    if latest_question_list:
        output = ', '.join([q.question_text for q in latest_question_list])
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

@user_is_entry_author
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    context = {'question: ' : question_id}
    return render(request,'polls/results.html',context)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
