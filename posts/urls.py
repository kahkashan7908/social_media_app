from django.urls import path
from.import views


urlpatterns = [
    path('create',views.post_create,name='create'),
    path('',views.feedPage,name='feed'),
    path('like',views.like_post,name="like`")
   
]