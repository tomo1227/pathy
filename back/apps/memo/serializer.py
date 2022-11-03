# coding: utf-8
import logging
from rest_framework import serializers
from djoser.serializers import UserSerializer
from apps.memo.models import Article
from apps.user.models import MyUser


logger = logging.getLogger(__name__)


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=MyUser.objects.all(), write_only=True
    )

    class Meta:
        model = Article
        fields = "__all__"

    def create(self, validated_data):
        logger.debug(validated_data)
        validated_data["author"] = validated_data.get("user_id", None)
        if validated_data["author"] is None:
            raise serializers.ValidationError("User not found.")

        del validated_data["user_id"]

        return Article.objects.create(**validated_data)
