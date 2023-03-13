from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.exceptions import APIException
from .serializers import CartSerializer
from products.models import Product
from .models import Cart


# Create your views here.
class ServiceUnavailable(APIException):
    status_code = 400
    default_detail = "Insufficient stock."
    default_code = "service_unavailable"


class CartView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        products_list = self.request.data["products"]

        for prducts in products_list:
            products_get = Product.objects.get(id=prducts["id"])
            if products_get.stock < prducts["quantity"]:
                raise ServiceUnavailable()

        user = self.request.user
        serializer.save(user=user)
