from django.urls import path
from .views import MyUserGetAPIView, MyUserCreateAPIView, MyUserUpdateAPIView, MyUserDeleteAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # トークン取得
    path('login/', TokenObtainPairView.as_view()),
    # トークン再取得
    path('login/refresh/', TokenRefreshView.as_view()),
    # ユーザー作成
    path('register/', MyUserCreateAPIView.as_view()),
    # ユーザー情報の取得
    path('mypage/', MyUserGetAPIView.as_view()),
    # ユーザー情報更新
    path('update/', MyUserUpdateAPIView.as_view()),
    # ユーザー削除
    path('delete/', MyUserDeleteAPIView.as_view())
]