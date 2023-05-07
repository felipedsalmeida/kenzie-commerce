from rest_framework import serializers

from addresses.models import Address

class AddressSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Address:
        return Address.objects.create(**validated_data)
    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "number",
            "zip_code",
            "city",
            "state"
        ]