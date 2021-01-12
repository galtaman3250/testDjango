from django.urls import path

from .views import *


app_name = "articles"


urlpatterns = [
    path('', index),
    path('article', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
]
