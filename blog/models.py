from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='post')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Messages(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    phone_number = models.CharField(max_length=212)
    site = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class CoursesCategory(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Courses(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='courses')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(CoursesCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Teachers(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='teachers')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='blog')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title







