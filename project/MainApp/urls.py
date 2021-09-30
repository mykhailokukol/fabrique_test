from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('quiz/<int:quiz_pk>/', views.AnswersView.as_view(), name='answers_page'),
    path('select-answer/', views.ViewAnswers.as_view(), name='answer_select_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('create-quiz/', login_required(views.CreateQuizView.as_view()), name='quiz_create_page'),
    path('create-question/', login_required(views.CreateQuestionView.as_view()), name='question_create_page'),
    path('update-quiz/<int:pk>/', login_required(views.UpdateQuizView.as_view()), name='quiz_update_page'),
    path('update-question/<int:pk>/', login_required(views.UpdateQuestionView.as_view()), name='question_update_page'),
    path('delete-quiz/<int:pk>/', login_required(views.DeleteQuizView.as_view()), name='quiz_delete_page'),
    path('delete-question/<int:pk>/', login_required(views.DeleteQuestionView.as_view()), name='question_delete_page'),
]
