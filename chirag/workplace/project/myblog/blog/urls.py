from django.urls import path
from .views import  *

urlpatterns = [
    path('postlist', post_list),
    path('postdetail', post_detail),
]