from rest_framework.routers import DefaultRouter
from . import views


app_name = 'MainApp'

router = DefaultRouter()
router.register(r'quizes', views.QuizViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)
