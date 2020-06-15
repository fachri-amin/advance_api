from django.urls import path

from .views import (
    api_detail_blog_view,
    api_update_blog_view,
    api_delete_blog_view,
    api_post_blog_view
)

app_name = 'rest'

urlpatterns = [
    path('post', api_post_blog_view, name='post_blog_api'),
    path('detail/<str:slug>', api_detail_blog_view, name='detail_blog_api'),
    path('update/<str:slug>', api_update_blog_view, name='update_blog_api'),
    path('delete/<str:slug>', api_delete_blog_view, name='delete_blog_api'),
]
