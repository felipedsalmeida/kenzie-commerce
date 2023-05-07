from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from carts.models import Cart
from addresses.serializers import Address, AddressSerializer
from users.models import User, USER_TYPE


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        address = validated_data.pop("address")
        address_db = Address.objects.create(**address)

        if validated_data.get("type") == USER_TYPE.ADMIN:
            user = User.objects.create_superuser(
                **validated_data, address=address_db
            )
        else:
            user = User.objects.create_user(
                **validated_data, address=address_db
            )
        Cart.objects.create(user=user)
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

    address = AddressSerializer()

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
            "email": {
                "validators": [UniqueValidator(queryset=User.objects.all())]
            },
        }
