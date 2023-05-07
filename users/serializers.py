from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from addresses.models import Address
from addresses.serializers import AddressSerializer
from carts.models import Cart
from carts.serializers import CartSerializer

from .models import USER_TYPE, User


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    def create(self, validated_data: dict) -> User:
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        user_type = validated_data.get('type')

        if user_type == USER_TYPE.ADMIN:
            user = User.objects.create_superuser(address=address, **validated_data)
        else:
            user = User.objects.create_user(address=address, **validated_data)

        Cart.objects.create(user=user)
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        address_data = validated_data.pop('address')
        address = instance.address

        for key, value in address_data.items():
            setattr(address, key, value)
        address.save()

        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "type",
            "address",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "email": {"validators": [UniqueValidator(queryset=User.objects.all())]},
        }
