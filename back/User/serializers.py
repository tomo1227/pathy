from rest_framework import serializers
from .models import MyUser

class MyUserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        #fields = ('email', 'username')
        #フィールドをすべて指定
        fields = '__all__'

class MyUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')
    # modelsで定義したcreate_user呼び行く
    def create(self, validated_data):
        return MyUser.objects.create_user(request_data=validated_data)

class MyUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')
    
    def update(self, instance, validated_data):
        # パスワードはハッシュ化
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance

class MyUserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        #fields = ('email', 'username')
        #フィールドをすべて指定
        fields = '__all__'