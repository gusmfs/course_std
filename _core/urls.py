from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView, SpectacularRedocView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('contents.urls')),
    path('api/', include('courses.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
