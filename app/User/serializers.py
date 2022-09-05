from rest_framework import serializers
from .models import MyUser

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        #fields = ('email', 'username', 'password', 'is_active', 'is_admin')
        #フィールドをすべて指定
        fields = '__all__'