from django.contrib import admin
from django.urls import path, include

from apps.memo.urls import router as memo_router

BASE_URL_API = "api/v1/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("memo/", include("apps.memo.urls")),
    path(BASE_URL_API + "memo/", include(memo_router.urls)),
    path(BASE_URL_API + "auth/", include("apps.user.urls")),
    path(BASE_URL_API + "auth/", include("djoser.urls")),
    path(BASE_URL_API + "auth/", include("djoser.urls.jwt")),
]
