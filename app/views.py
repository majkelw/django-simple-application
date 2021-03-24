from .models import User, UserCatOwner, Cat, Hunting, HuntingDetails, Prey
from rest_framework import viewsets
from .serializer import UserSerializer, UserCatOwnerSerializer, CatSerializer, HuntingSerializer, \
    HuntingDetailsSerializer, PreySerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCatOwnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserCatOwner.objects.all()
    serializer_class = UserCatOwnerSerializer


class CatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class PreyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Prey.objects.all()
    serializer_class = PreySerializer


class HuntingViewSet(viewsets.ModelViewSet):
    queryset = Hunting.objects.all()
    serializer_class = HuntingSerializer


class HuntingDetailsViewSet(viewsets.ModelViewSet):
    queryset = HuntingDetails.objects.all()
    serializer_class = HuntingDetailsSerializer
