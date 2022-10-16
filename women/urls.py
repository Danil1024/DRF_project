from django.urls import path
from .views import WomenListAPIView, WomenAPIDetailView


urlpatterns = [
	path('api/v1/womenlist/', WomenListAPIView.as_view(), name= 'women'),
	path('api/v1/women/detail/<int:pk>/', WomenAPIDetailView.as_view()),
]
