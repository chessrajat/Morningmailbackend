from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include("users.urls")),
    path('api/v1/email/', include("dashboard.urls")),
]
