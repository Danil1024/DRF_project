# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
	def get (self, request):
		list_women = Women.objects.all()
		return Response({'list_women': WomenSerializer(list_women, many=True).data})

	def post(self, request):
		serializer = WomenSerializer(data= request.data)
		serializer.is_valid(raise_exception= True)

		new_women = Women.objects.create(
			title = request.data['title'],
			content = request.data['content'],
			cat_id = request.data['cat_id']
			)
		return Response({'new_women': WomenSerializer(new_women).data})


'''class WomenAPIView(generics.ListAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer'''
