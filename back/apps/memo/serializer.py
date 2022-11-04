# coding: utf-8
import logging
from rest_framework import serializers
from djoser.serializers import UserSerializer
from apps.memo.models import Article
from apps.user.models import MyUser


logger = logging.getLogger(__name__)


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    user_email = serializers.SlugRelatedField(
        queryset=MyUser.objects.all(), write_only=True,slug_field='email'
    )

    class Meta:
        model = Article
        fields = "__all__"

    def create(self, validated_data):
        logger.debug(validated_data)
        validated_data["author"] = validated_data.get("user_email", None)
        if validated_data["author"] is None:
            raise serializers.ValidationError("User not found.")

        del validated_data["user_email"]

        return Article.objects.create(**validated_data)
