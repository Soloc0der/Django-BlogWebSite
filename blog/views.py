from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views import View
from django.db.models import Q
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import *

class BlogList(View):
    def get(self, request):
        posts = Post.objects.all()
        search = request.GET.get("search")
        if search:
            posts = Post.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
        cats = Category.objects.all()
        tags = Tag.objects.all()
        return render(request, "blog/list.html", {"posts": posts, "cats": cats, "tags": tags}) 
    
    def post(self, request):
        pass

class BlogDeatil(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post)
        return render(request, "blog/detail.html", {"post": post, "comments": comments})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        Comment.objects.create(name=name, email=email, text=comment, post=post)
        return redirect('detail', slug)

class CategoryDetail(View):
    def get(self, request, cat_slug):
        cats = Category.objects.all()
        category = get_object_or_404(Category, slug=cat_slug)
        # comments = Comment.objects.filter(category=category)
        posts = Post.objects.filter(category=category)
        return render(request, "blog/list.html", {"posts": posts, "cats": cats})



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]

class CatList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer
    permission_classes = [IsAdminUser]

class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer
    permission_classes = [IsAdminUser]

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]

def blog_price(request):
    return render(request, 'blog/price.html')

def blog_feature(request):
    return render(request, 'blog/feature.html')

def blog_testimonial(request):
    return render(request, 'blog/testimonial.html')

def blog_team(request):
    return render(request, 'blog/team.html')

def blog_quote(request):
    return render(request, 'blog/quote.html')