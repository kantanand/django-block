from rest_framework import viewsets
from polls.models import Question, Choice
from polls.serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer