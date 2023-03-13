from django.urls import path
from .views import AddressCreate

urlpatterns = [path("address/", AddressCreate.as_view())]
