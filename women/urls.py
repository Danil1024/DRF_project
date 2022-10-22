from django.urls import path, include
from .views import WomenRetrieveUpdateAPIView, WomenRetrieveDestroyAPIView,\
					WomenListAPIView#, UserCreateAPIView



urlpatterns = [
	path('api/v1/women/', WomenListAPIView.as_view()),
	path('api/v1/women/delete/<int:pk>/', WomenRetrieveDestroyAPIView.as_view()),
	path('api/v1/women/<int:pk>/', WomenRetrieveUpdateAPIView.as_view()),
	#path('api/v1/user/', UserCreateAPIView.as_view())
]
