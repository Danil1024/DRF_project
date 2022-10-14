from rest_framework import serializers
from .models import Women


class WomenSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=255)
	content = serializers.CharField()
	time_create = serializers.DateTimeField(read_only=True)
	time_update= serializers.DateTimeField(read_only=True)
	is_published = serializers.BooleanField(default=True)
	cat_id = serializers.IntegerField()


"""class WomenSerializer(serializers.ModelSerializer): Для авто полей модели сразу ставиться read_only=True
	class Meta:
		model = Women
		fields = ('title', 'content', 'time_create', 'time_update', 'is_published', 'cat_id')"""

