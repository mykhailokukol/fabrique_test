from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_page'),
    path('login/', views.login_page, name='login_page'),
]
