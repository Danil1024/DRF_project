from rest_framework import serializers
from .models import Women
#from django.contrib.auth.models import User
#import datetime


class WomenSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = Women
		fields = ('id', 'title', 'content', 'time_create', 'time_update', 'cat', 'user')


'''class UserSerializer(serializers.ModelSerializer):
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
        fields = ( "id", "username", "password", 'last_login')'''


'''class WomenSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=255)
	content = serializers.CharField()
	time_create = serializers.DateTimeField(read_only=True)
	time_update= serializers.DateTimeField(read_only=True)
	is_published = serializers.BooleanField(default=True)
	cat_id = serializers.IntegerField()

	def create(self, validated_data):
		return Women.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.content = validated_data.get('content', instance.content)
		instance.time_update = validated_data.get('time_update', instance.time_update)
		instance.is_published = validated_data.get('is_published', instance.is_published)
		instance.cat_id = validated_data.get('cat_id', instance.cat_id)
		instance.save()
		return instance'''


''''{    
    "title": "Danil",
    "content": "Danil Danil Danil",
    "cat_id": 2
}'''