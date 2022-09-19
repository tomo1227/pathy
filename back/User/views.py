from django.db import transaction
from rest_framework import generics, authentication, permissions
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from .models import MyUser
from .serializers import MyUserGetSerializer, MyUserCreateSerializer, MyUserUpdateSerializer, MyUserDeleteSerializer
from django.http import Http404

'''
# ログインユーザー情報取得
class MyUserGetAPIView(generics.RetrieveAPIView):
    # ログイン状態でのみ取得可
    permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = [permissions.AllowAny] 
    queryset = MyUser.objects.all()
    serializer_class = MyUserGetSerializer

    def get(self, request, format=None):
        return Response(data={
            'username': request.user.username,
            'email': request.user.email,
            },
            status=status.HTTP_200_OK)

# ユーザー作成
class MyUserCreateAPIView(generics.CreateAPIView):
    # 認証されていなくても許可
    permission_classes = (permissions.AllowAny,)
    queryset = MyUser.objects.all()
    serializer_class = MyUserCreateSerializer

    # トランザクション
    @transaction.atomic
    def post(self, request, format=None):
        serializer = MyUserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyUserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = MyUser.objects.all()
    serializer_class = MyUserUpdateSerializer

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except MyUser.DoesNotExist:
            raise Http404

class MyUserDeleteAPIView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = MyUser.objects.all()
    serializer_class = MyUserDeleteSerializer
    lookup_field = 'email'

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except MyUser.DoesNotExist:
            raise Http404
'''