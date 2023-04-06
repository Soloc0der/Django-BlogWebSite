from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/posts/', PostList.as_view(), name="posts_list"),
    path('api/v1/post/<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('api/v1/cats/', CatList.as_view(), name="cats_list"),
    path('api/v1/cat/<int:pk>/', CatDetail.as_view(), name="cats_datal"),
    path('api/v1/tags/', TagList.as_view(), name="tags_list"),
    path('api/v1/tag/<int:pk>/', TagDetail.as_view(), name="tags_detal"),
]   