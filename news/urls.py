from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='home'),
    path('category/<int:cat_id>',get_cat, name='category')
]