from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from .models import Women
from .serializers import WomenSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class WomenListAPIView(generics.ListCreateAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer
	permission_classes = (IsAuthenticated,)


class WomenRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer
	permission_classes = (IsOwnerOrReadOnly,)


class WomenRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer
	permission_classes = (IsAdminOrReadOnly,)
