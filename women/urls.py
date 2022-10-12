from django.urls import path
from .views import WomenAPIView


urlpatterns = [
	path('api/v1/womenlist/', WomenAPIView.as_view(), name= 'women_list')
]