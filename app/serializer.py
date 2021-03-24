from .models import User, UserCatOwner, Cat
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'cats_number']


class UserCatOwnerSerializer(serializers.HyperlinkedModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.name')
    cat_name = serializers.ReadOnlyField(source='cat.name')

    class Meta:
        model = UserCatOwner
        fields = ['id', 'user_name', 'cat_name']


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ['id', 'name', 'color', 'gender']
