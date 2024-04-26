from django.contrib import admin
from .models import Post, Category, Author, Courses, Teachers, Blog, Messages, CoursesCategory


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('title', 'created_at', 'updated_at')


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Courses)
admin.site.register(Teachers)
admin.site.register(Blog)
admin.site.register(Messages)
admin.site.register(CoursesCategory)
