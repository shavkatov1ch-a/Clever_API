from django     .shortcuts import render
from rest_framework import generics
from .models import Post, Category, Author, Teachers, Blog, Courses
from .serializers import *


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        title = self.request.query_params.get('title')
        if category:
            return Post.objects.filter(category__name__icontains=category)
        if title:
            return Post.objects.filter(title__name__icontains=title)
        else:
            return Post.objects.all()


class TeachersAPIView(generics.ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer


class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer



class CoursesCategoryAPIView(generics.ListAPIView):
    queryset = CoursesCategory.objects.all()
    serializer_class = CoursesCategorySerializer



class CourseAPIView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class HomePageAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class MessagesAPIView(generics.CreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer



