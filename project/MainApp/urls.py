from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('create-quiz/', views.CreateQuizView.as_view(), name='quiz_create_page'),
    path('create-question/', views.CreateQuestionView.as_view(), name='question_create_page'),
]
