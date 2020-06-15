from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest.models import Blog
from .serializers import BlogSerializer
from account.models import Account


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def api_detail_blog_view(request, slug):

    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers_data = BlogSerializer(blog)
        return Response(serializers_data.data)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def api_update_blog_view(request, slug):

    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if user != blog.author:
        return Response({'response': "You don't have permission to edit that!"})

    if request.method == 'PUT':
        serializers_data = BlogSerializer(blog, data=request.data)
        data = {}
        if serializers_data.is_valid():
            serializers_data.save()
            data['success'] = 'update success'
            return Response(data=data)
        return Response(serializers_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def api_delete_blog_view(request, slug):

    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if user != blog.author:
        return Response({'response': "You don't have permission to edit that!"})

    if request.method == 'DELETE':
        operation = blog.delete()
        data = {}
        if operation:
            data['success'] = 'delete successful'
        else:
            data['failure'] = 'delete failed'
        return Response(data=data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def api_post_blog_view(request):
    account = request.user
    blog = Blog(author=account)
    if request.method == 'POST':
        serializers_data = BlogSerializer(blog, data=request.data)
        if serializers_data.is_valid():
            serializers_data.save()
            return Response(serializers_data.data, status=status.HTTP_201_CREATED)
        return Response(serializers_data.errors, status=status.HTTP_400_BAD_REQUEST)
