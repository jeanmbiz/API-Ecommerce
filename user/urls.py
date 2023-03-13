from .views import UserViewGenerics, LoginJWTView, UserAdminUpdateGenerics
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

urlpatterns = [
    path("user/", UserViewGenerics.as_view()),
    path("user/<uuid:pk>/", UserAdminUpdateGenerics.as_view()),
    path("user/login/", LoginJWTView.as_view()),
    path("user/login/refresh/", TokenRefreshView.as_view()),
]
