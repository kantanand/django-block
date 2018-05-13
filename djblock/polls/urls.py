from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views
from polls import api_views

router = routers.DefaultRouter()
router.register(r'questions', api_views.QuestionViewSet)
app_name = "polls"
urlpatterns = [
    # url(r'^', include(router.urls)),
    # path('', views.index, name='index'),
    # path('details/', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
