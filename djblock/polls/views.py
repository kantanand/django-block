from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone



from polls.models import Question, Choice
from polls.decorators import user_is_entry_author

# deprecated  
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = "nox questions"
#     if latest_question_list:
#         output = ', '.join([q.question_text for q in latest_question_list])
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# @user_is_entry_author
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question: ': question}
#     return render(request,'polls/result.html',context)


# class based view 
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    """
    By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html.
    In our case, it would use the template "polls/question_detail.html"
    """
    # template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('api:polls:results', args=(question.id,)))
