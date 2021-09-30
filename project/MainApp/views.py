from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from . import models, forms
from datetime import datetime


class IndexView(View):

    def get(self, request):
        active_quizes = models.Quiz.objects.filter(date_finish__gte=datetime.date(datetime.now())).order_by('date_finish')
        return render(request, 'MainApp/index.html', {
            'quizes': active_quizes,
        })

    def post(self, request):
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

@login_required
def logout_view(request):

    logout(request)

    return redirect('/')
