from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User
class UserSerializer(serializers.ModelSerializer):
       
    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
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
            "address"
        ]
        extra_kwargs = {"password": {"write_only": True}, 
        "username": {"validators": [UniqueValidator(queryset=User.objects.all(),
        message="A user with that username already exists.")]}, 
        "email": {"validators": [UniqueValidator(queryset=User.objects.all())]}}