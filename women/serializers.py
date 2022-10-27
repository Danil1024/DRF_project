from rest_framework import serializers
from .models import Women
from django.contrib.auth.models import User
import datetime


class WomenSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = Women
		fields = ('id', 'title', 'content', 'time_create', 'time_update', 'cat', 'user')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    last_login = serializers.HiddenField(default= datetime.datetime.now())
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            last_login=validated_data['last_login']
        )
        return user

    class Meta:
        model = User
        fields = ( "id", "username", "password", 'last_login')
