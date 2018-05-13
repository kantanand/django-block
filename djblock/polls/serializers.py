from polls.models import Question, Choice
from rest_framework import serializers

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = (
            'url',
            'question_text',
            'pub_date',
            'is_published',
            'created_by',
        )
