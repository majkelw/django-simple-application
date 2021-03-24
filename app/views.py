from .models import User, UserCatOwner, Cat
from rest_framework import viewsets
from .serializer import UserSerializer, UserCatOwnerSerializer, CatSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCatOwnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserCatOwner.objects.all()
    serializer_class = UserCatOwnerSerializer


class CatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
