from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    re_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("id", "name", "email", "password", "re_password")

    def validate(self, data):
        re_password = data.get("re_password")
        data.pop("re_password")
        password = data.get("password")

        try:
            if password != re_password:
                raise exceptions.ValidationError(
                    "The two password fields didn't match.")

        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {"password": serializer_errors["non_field_errors"]}
            )

        return data

    def validate_email(self, value):
        value = value.lower()
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "user with this email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data["name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        self.token = data.get("refresh", "")

        return data

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            raise serializers.ValidationError({
                "refresh": [
                    "Invalid RefreshToken"
                ]
            })
