from rest_framework import serializers

from rest.models import Blog


class BlogSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Blog
        fields = ['title', 'body', 'author']

    def get_username(self, blog):
        return blog.author.username
