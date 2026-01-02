from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError("Email and password are required")

        user = authenticate(
            request=self.context.get("request"),
            username=email,   
            password=password,
        )

        if not user:
            raise serializers.ValidationError("Invalid email or password")

        data = super().validate({
            self.username_field: user.email,
            "password": password,
        })

        data["email"] = user.email
        return data