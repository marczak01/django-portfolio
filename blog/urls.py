from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('single-post/<str:pk>', views.singlePost, name='single-post'),
]