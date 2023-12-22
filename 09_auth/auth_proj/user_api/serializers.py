# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        # パスワードをハッシュ化して保存
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
