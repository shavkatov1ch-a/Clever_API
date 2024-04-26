from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only = ['created_at', 'updated_at']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only = ['created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = '__all__'
        read_only = ['created_at', 'updated_at']



class CoursesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesCategory
        fields = '__all__'
        read_only = ['created_at', 'updated_at']





class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        read_only = ['created_at', 'updated_at']\



class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'
        read_only = ['created_at', 'updated_at']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read_only = ['created_at', 'updated_at']


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
        read_only = ['created_at', 'updated_at']

