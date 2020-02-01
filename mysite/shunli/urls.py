from django.urls import path
from . import views
from shunli.views import contact

app_name ="shunli"
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', contact, name="contact"),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]