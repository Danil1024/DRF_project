from django.urls import path
from .views import WomenAPIView


urlpatterns = [
	path('api/v1/womenlist/', WomenAPIView.as_view(), name= 'women'),
	path('api/v1/change_women/<int:pk>/', WomenAPIView.as_view()),
	path('api/v1/delete_women/<int:pk>/', WomenAPIView.as_view())
]
