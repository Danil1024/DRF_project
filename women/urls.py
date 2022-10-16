from django.urls import path, include
from .views import WomenViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'women', WomenViewSet)


urlpatterns = [
	path('api/v1/', include(router.urls)),
]
