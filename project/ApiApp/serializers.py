from rest_framework import serializers
from MainApp import models


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quiz
        fields = ['title', 'date_start', 'date_finish', 'description', 'questions', ]


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = ['text', 'type', ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Answer
        fields = ['text', 'author']
