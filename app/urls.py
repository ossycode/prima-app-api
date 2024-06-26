"""
Project URL patterns.
"""
from django.contrib import admin
from django.urls import include, path
from . import views

from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    path('api/users/', include('users.urls')),
    path('', views.redirect_to_api_docs, name='base_url_redirect')

]

