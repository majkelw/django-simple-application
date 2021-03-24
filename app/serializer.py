from .models import User, UserCatOwner, Cat, Hunting, HuntingDetails, Prey
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


class HuntingSerializer(serializers.HyperlinkedModelSerializer):
    cat_name = serializers.ReadOnlyField(source='cat.name')

    class Meta:
        model = Hunting
        fields = ['id', 'cat', 'cat_name', 'duration']
        extra_kwargs = {
            'cat': {'write_only': True},
        }


class PreySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prey
        fields = ['id', 'type']


class HuntingDetailsSerializer(serializers.HyperlinkedModelSerializer):
    cat_name = serializers.ReadOnlyField(source='cat.name')
    hunting_id = serializers.ReadOnlyField(source='hunting.id')
    prey_type = serializers.ReadOnlyField(source='prey.type')

    class Meta:
        model = HuntingDetails
        fields = ['hunting_id', 'cat_name', 'prey_type', 'cat', 'hunting', 'prey']
        extra_kwargs = {
            'cat': {'write_only': True},
            'hunting': {'write_only': True},
            'prey': {'write_only': True}
        }
