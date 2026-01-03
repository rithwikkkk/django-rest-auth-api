from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username=email,   # ✅ REQUIRED
            email=email,
            password=password,
        )
        return user