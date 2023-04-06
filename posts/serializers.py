from rest_framework import serializers
from blog.models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description', 'image', 'author', 'category', 'tag', 'created', 'updated',)
        read_only_fields = ('id',)
        model = Post

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        fields= ('id', 'title', 'slug', )
        read_only_fields = ('id',)
        model = Category

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', )
        read_only_fields = ('id', )
        model = Tag