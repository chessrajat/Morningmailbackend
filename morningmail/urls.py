from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include("users.urls")),
    path('api/v1/email/', include("dashboard.urls")),
    re_path(r"^$", TemplateView.as_view(template_name="index.html")),
    re_path(r"^(?:.*)/?$", TemplateView.as_view(template_name="index.html"))
]
