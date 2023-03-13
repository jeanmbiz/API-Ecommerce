from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import RegisterAddressPermission
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from .serializers import AddressSerializer
from user.models import User
from .models import Address


class AddressCreate(CreateAPIView):
    queryset = Address.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [RegisterAddressPermission]
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.user.id)

        serializer.save(user=user)
