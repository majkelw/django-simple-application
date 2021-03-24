from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, UserCatOwnerViewSet, CatViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'catowner', UserCatOwnerViewSet)
router.register(r'cats', CatViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
