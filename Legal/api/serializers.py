from rest_framework import serializers
from django.utils.translation import ugettext as _
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .. import models


class LegalDocuments(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    file = serializers.FileField(
        max_length=None, use_url=True, allow_null=True, allow_empty_file=True,
    )

    class Meta:
        model = models.Documents
        exclude = ["deleted_at", "timestamp", "create_by"]

    def get_file(self, obj):
        if obj.file:
            return self.context["request"].build_absolute_uri(obj.file.url)

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)
