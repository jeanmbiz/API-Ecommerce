from django.urls import path, include
from django.contrib import admin
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("user.urls")),
    path("api/", include("products.urls")),
    path("api/", include("address.urls")),
    path("api/", include("orders.urls")),
    path("api/", include("cart.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path("api/docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
