from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permissions import CreateProductPermission
from .permissions import IsAuthenticatedPermission
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import OrdersSerializer
from address.models import Address
from .models import Orders


class OrderViewGenerics(ListCreateAPIView):
    queryset = Orders.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedPermission]
    serializer_class = OrdersSerializer

    def perform_create(self, serializer) -> Response:
        address = get_object_or_404(Address, id=self.request.data["address"])

        serializer.save(address=address)


class OrderViewDetailGenerics(RetrieveUpdateAPIView):
    queryset = Orders.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateProductPermission]
    serializer_class = OrdersSerializer
    slug_url_kwarg = "uuid"
