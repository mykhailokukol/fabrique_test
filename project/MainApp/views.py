from django.shortcuts import render


def index(request):

    return render(request, 'MainApp/index.html', {

    })

def login_page(request):

    return render(request, 'MainApp/login.html', {

    })
