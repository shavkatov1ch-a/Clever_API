from django.urls import path
from .views import *


urlpatterns = [
    path('home/', HomePageAPIView.as_view(), name='home'),
    path('category/', CategoryAPIView.as_view(), name='category'),
    path('author/', AuthorAPIView.as_view(), name='author'),
    path('post/', PostAPIView.as_view(), name='post'),
    path('courses/', CourseAPIView.as_view(), name='courses'),
    path('teachers/', TeachersAPIView.as_view(), name='teachers'),
    path('blog/', BlogAPIView.as_view(), name='blog'),
    path('detail/<int:pk>/', DetailAPIView.as_view(), name='detail'),
    path('messages/', MessagesAPIView.as_view(), name='messages'),
    path('coursescategory/', CoursesCategoryAPIView.as_view(), name='coursescategory')

]
