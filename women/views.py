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
		serializer.save()

		return Response({'new_women': serializer.data})

	def put(self, request, *args, **kwargs):
		pk = kwargs.get('pk', None)
		if not pk:
			return Response({'Error':'Method PUT not allowed'})

		try:
			instance = Women.objects.get(pk=pk)
		except:
			return Response({'Error':'Object does not exist'})

		serializer = WomenSerializer(data= request.data, instance=instance)
		serializer.is_valid(raise_exception= True)
		serializer.save()

		return Response({'change_women':serializer.data})

	def delete(self, request, *args, **kwargs):
		print(kwargs)
		pk = kwargs.get('pk', None)
		if not pk:
			return Response({'Error':'Method PUT not allowed'})

		try:
			women = Women.objects.get(pk=pk)
		except:
			return Response({'Error':'Object does not exist'})

		women.delete()

		return Response({'delete_women_id':pk,'delete_women': model_to_dict(women)})


'''class WomenAPIView(generics.ListAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer'''
