from django.db import models


class Quiz(models.Model):

    title = models.CharField(max_length=255, blank=False, null=False)
    date_start = models.DateField(auto_now_add=True, null=True)
    date_finish = models.DateField(null=True)
    description = models.TextField(default='Описание опроса.')


QUESTION_TYPE_CHOICES = [
    ('text', 'Ответ с текстом'),
    ('choice', 'Ответ с выбором одного ванианта'),
    ('m_choice', 'Ответ с выбором нескольких вариантов'),
]


class Question(models.Model):

    text = models.CharField(max_length=255, blank=False, null=False)
    type = models.CharField(max_length=36, blank=False, null=False, choices=QUESTION_TYPE_CHOICES)
