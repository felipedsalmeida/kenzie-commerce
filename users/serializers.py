from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from addresses.models import Address
from addresses.serializers import AddressSerializer
from carts.models import Cart

from .models import USER_TYPE, User


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    def validate_type(self, value: str) -> str:
        user = self.context["request"].user

        if value == USER_TYPE.ADMIN and not (user and user.is_superuser):
            raise serializers.ValidationError("Only Admins can set the type to Admin.")
        return value

    def create(self, validated_data: dict) -> User:
        address_data = validated_data.pop("address")
        address = Address.objects.create(**address_data)
        user_type = validated_data.get("type")

        if user_type == USER_TYPE.ADMIN:
            user = User.objects.create_superuser(address=address, **validated_data)
        else:
            user = User.objects.create_user(address=address, **validated_data)

        Cart.objects.create(user=user)
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        address_data = validated_data.pop("address")
        address = instance.address

        for key, value in address_data.items():
            setattr(address, key, value)
        address.save()

        user = self.context["request"].user
        if user and user.is_superuser:
            for key, value in validated_data.items():
                if key == "password":
                    instance.set_password(value)
                elif key == "type":
                    if value == USER_TYPE.ADMIN:
                        instance.is_superuser = True
                        instance.is_staff = True
                    elif value in [USER_TYPE.CUSTOMER, USER_TYPE.SELLER]:
                        instance.is_superuser = False
                        instance.is_staff = False
                    setattr(instance, key, value)
                else:
                    setattr(instance, key, value)
        else:
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
