from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.logout_view, name='logout'),
]
