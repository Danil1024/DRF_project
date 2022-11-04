from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly, IsOwnerOrReadOnly
from .filters import IsOwnerOrAdminFilterBackend


class WomenListAPIView(generics.ListCreateAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer
	permission_classes = (IsAuthenticated,)
	filter_backends = [IsOwnerOrAdminFilterBackend,]


class WomenRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer
	permission_classes = (IsOwnerOrReadOnly,)


class WomenRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
	queryset = Women.objects.all()
	serializer_class = WomenSerializer
	permission_classes = (IsOwnerOrAdminOrReadOnly,)
