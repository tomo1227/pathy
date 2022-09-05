from rest_framework import generics

from .models import MyUser
from .serializers import MyUserSerializer

class MyUserAPIView(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer