from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """

    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class UserSignUpSerializer(serializers.ModelSerializer):
    """DRF Serializer For User Registration"""

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
        ]  # You can add here first_name ,last_name

    def create(self, validated_data):
        password = validated_data.pop("password")
        user_instance = User.objects.create(**validated_data)
        user_instance.set_password(password)
        user_instance.is_active = False
        user_instance.token = default_token_generator.make_token(user_instance)
        user_instance.send_confirmation_email()
        user_instance.save()
        return user_instance


class ProfileInfoSerializer(serializers.ModelSerializer):
    """Serializer for the user settings objects"""

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "username",
            "password",
            "phone_number",
            "private_account",
            "website",
            "fullname",
            "bio",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
                "allow_null": True,
                "required": False,
                "min_length": 5,
            },
            "username": {"min_length": 3},
        }

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for viewing a user posts"""

    followed_by_req_user = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "fullname",
            "phone_number",
            "website",
            "is_verify",
            "bio",
            "profile_pic",
            "followed_by_req_user",
        )

    def get_followed_by_req_user(self, obj):
        user = self.context["request"].user
        return user in obj.followers.all()


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for listing all followers"""

    class Meta:
        model = get_user_model()
        fields = ("username", "profile_pic")


class AllUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

