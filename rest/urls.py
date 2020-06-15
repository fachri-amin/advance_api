from django.urls import path

from .views import CreateBlog

app_name = 'rest'

urlpatterns = [
    path('createBlog', CreateBlog.as_view(), name='createBlog'),
]
