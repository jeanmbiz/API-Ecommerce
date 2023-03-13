from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, CustomJWTSerializer
from .permissions import UpdatePermission
from .models import User


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class UserViewGenerics(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAdminUpdateGenerics(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [UpdatePermission]
    serializer_class = UserSerializer
