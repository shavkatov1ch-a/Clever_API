from django.shortcuts import render
from rest_framework import generics
from .seriallizers import ContactSerializer, ContactInfoSerializer
from .models import Contact, ContactInfo

class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInfoAPIView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


