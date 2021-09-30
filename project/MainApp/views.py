from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.views.generic import View
from . import models, forms
from .utils import CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin
from datetime import datetime


class IndexView(View):

    def get(self, request):
        active_quizes = models.Quiz.objects.filter(date_finish__gte=datetime.date(datetime.now())).order_by('date_finish')
        return render(request, 'MainApp/index.html', {
            'quizes': active_quizes,
        })


class AnswersView(View):

    def get(self, request, quiz_pk):
        form = forms.AnswerForm()
        quiz = models.Quiz.objects.get(pk=quiz_pk)
        return render(request, 'MainApp/answer.html', {
            'quiz': quiz,
            'form': form,
        })

    def post(self, request, quiz_pk):
        form = forms.AnswerForm(request.POST)
        quiz = models.Quiz.objects.get(pk=quiz_pk)
        if form.is_valid():
            request.session.save()
            if not request.session.exists(request.session.session_key):
                request.session.create()
            session = Session.objects.get(session_key=request.session.session_key)
            for answr in request.POST.getlist('text'):
                new_answer = models.Answer.objects.create(
                    text=answr,
                    author=session,
                )
                quiz.answers.add(models.Answer.objects.get(text=answr, author=session))
        return redirect('/')


class LoginView(View):

    def get(self, request):
        form = forms.LoginForm()
        return render(request, 'MainApp/login.html', {
            'form': form,
        })

    def post(self, request):

        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            raw_password = request.POST['password']
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        return redirect('/')


class CreateQuizView(CreateObjectMixin, View):
    model_form = forms.QuizForm
    template = 'MainApp/quiz_create.html'


class CreateQuestionView(CreateObjectMixin, View):
    model_form = forms.QuestionForm
    template = 'MainApp/question_create.html'


class UpdateQuizView(UpdateObjectMixin, View):
    model = models.Quiz
    model_form = forms.QuizForm
    template = 'MainApp/quiz_update.html'


class UpdateQuestionView(UpdateObjectMixin, View):
    model = models.Question
    model_form = forms.QuestionForm
    template = 'MainApp/question_update.html'


class DeleteQuizView(DeleteObjectMixin, View):
    model = models.Quiz
    template = 'MainApp/quiz_delete.html'


class DeleteQuestionView(DeleteObjectMixin, View):
    model = models.Question
    template = 'MainApp/question_delete.html'


class ViewAnswers(View):

    def get(self, request):
        user_answers = None
        form = forms.ChooseAnswerForm()
        return render(request, 'MainApp/answers_select.html', {
            'form': form,
            'user_answers': user_answers,
        })

    def post(self, request):
        form = forms.ChooseAnswerForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['author']
            user_answers = models.Answer.objects.filter(author=user)
            return render(request, 'MainApp/answers_select.html', {
                'form': form,
                'user_answers': user_answers,
            })
        else:
            return render(request, 'MainApp/answers_select.html', {
                'form': form,
            })


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
