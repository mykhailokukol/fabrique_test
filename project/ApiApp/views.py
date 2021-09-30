from rest_framework import viewsets
from . import serializers
from MainApp import models


class QuizViewSet(viewsets.ModelViewSet):

    queryset = models.Quiz.objects.all().order_by('date_start')
    serializer_class = serializers.QuizSerializer


class QuestionViewSet(viewsets.ModelViewSet):

    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):

    queryset = models.Answer.objects.all().order_by('author')
    serializer_class = serializers.AnswerSerializer
