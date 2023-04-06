from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description', 'image', 'author', 'category', 'tag', 'created', 'updated',)
        read_only_fields = ('id',)
        model = Post

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id',)
        read_only_fields = ('id',)
        model = Category

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'post', 'author', 'name', 'email', 'text')
        read_only_fields = ('id', )
        model = Comment

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', )
        read_only_fields = ('id', )
        model = Tag