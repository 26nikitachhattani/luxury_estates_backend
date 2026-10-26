from rest_framework import serializers
from .models import Property, Inquiry


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class InquirySerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(
        source="property.name",
        read_only=True,
    )

    class Meta:
        model = Inquiry
        fields = [
            "id",
            "property",
            "property_name",
            "name",
            "email",
            "phone",
            "message",
            "created_at",
        ]
        read_only_fields = ("id", "property_name", "created_at")

    def validate_phone(self, value):
        cleaned = value.strip()
        digits = "".join(ch for ch in cleaned if ch.isdigit())

        if len(digits) < 7 or len(digits) > 15:
            raise serializers.ValidationError(
                "Enter a valid phone number."
            )

        return cleaned