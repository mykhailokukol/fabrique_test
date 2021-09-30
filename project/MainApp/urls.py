from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('create-quiz/', views.CreateQuizView.as_view(), name='quiz_create_page'),
    path('create-question/', views.CreateQuestionView.as_view(), name='question_create_page'),
    path('update-quiz/<int:pk>/', views.UpdateQuizView.as_view(), name='quiz_update_page'),
    path('update-question/<int:pk>/', views.UpdateQuestionView.as_view(), name='question_update_page'),
    path('delete-quiz/<int:pk>/', views.DeleteQuizView.as_view(), name='quiz_delete_page'),
    path('delete-question/<int:pk>/', views.DeleteQuestionView.as_view(), name='question_delete_page'),
]
