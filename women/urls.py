from django.urls import path, include, re_path
from .views import WomenRetrieveUpdateAPIView, WomenRetrieveDestroyAPIView, WomenListAPIView


urlpatterns = [
	path('api/v1/women/', WomenListAPIView.as_view()),
	path('api/v1/women/delete/<int:pk>/', WomenRetrieveDestroyAPIView.as_view()),
	path('api/v1/women/<int:pk>/', WomenRetrieveUpdateAPIView.as_view()),
	path('api/v1/auth/', include('djoser.urls')),
	re_path(r'^auth/', include('djoser.urls.authtoken')),
]
