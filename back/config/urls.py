from django.contrib import admin
from django.urls import path, include

from memo.urls import router as memo_router

BASE_URL_API = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('memo/', include('memo.urls')),
    path(BASE_URL_API + 'memo/', include(memo_router.urls)),
]
