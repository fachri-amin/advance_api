from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest.models import Blog
from .serializers import BlogSerializer


@api_view(['GET', ])
def api_detail_blog_view(request, slug):

    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers_data = BlogSerializer(blog)
        return Response(serializers_data.data)


@api_view(['PUT', ])
def api_update_blog_view(request, slug):

    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializers_data = BlogSerializer(blog, data=request.data)
        data = {}
        if serializers_data.is_valid():
            serializers_data.save()
            data['success'] = 'update success'
            return Response(data=data)
        return Response(serializers_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_blog_view(request, slug):

    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = blog.delete()
        data = {}
        if operation:
            data['success'] = 'delete successful'
        else:
            data['failure'] = 'delete failed'
        return Response(data=data)
