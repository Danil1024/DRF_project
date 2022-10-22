from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from .models import Women
from .serializers import WomenSerializer#, UserSerializer
#from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


"""class UserCreateAPIView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer"""


class WomenListAPIView(generics.ListCreateAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer
	permission_classes = (IsOwnerOrReadOnly,)


class WomenRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer
	permission_classes = (IsAdminOrReadOnly,)




"""
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
			return Response({'Error':'Object does not exist'}
		serializer = WomenSerializer(data= request.data, instance=instance)
		serializer.is_valid(raise_exception= True)
		serializer.save()
		return Response({'change_women':serializer.data})

	def delete(self, request, *args, **kwargs):
		pk = kwargs.get('pk', None)
		if not pk:
			return Response({'Error':'Method PUT not allowed'})
		try:
			women = Women.objects.get(pk=pk)
		except:
			return Response({'Error':'Object does not exist'})
		women.delete()
		return Response({'delete_women_id':pk,'delete_women': model_to_dict(women)})
"""
