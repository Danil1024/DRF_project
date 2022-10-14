# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from .models import Women
# from .serializers import WomenSerializer


class WomenAPIView(APIView):
	def get (self, request):
		list_women = Women.objects.values()
		return Response({'list_women': list_women})

	def post(self, request):
		new_women = Women.objects.create(
			title = request.data['title'],
			content = request.data['content'],
			cat_id = request.data['cat_id']
			)
		return Response({'list_women': model_to_dict(new_women)})




'''class WomenAPIView(generics.ListAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer'''
