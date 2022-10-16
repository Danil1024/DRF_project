from django.urls import path
from .views import WomenListAPIView


urlpatterns = [
	path('api/v1/womenlist/', WomenListAPIView.as_view(), name= 'women'),
	path('api/v1/women/change/<int:pk>/', WomenListAPIView.as_view()),
	path('api/v1/women/delete/<int:pk>/', WomenListAPIView.as_view())
]
