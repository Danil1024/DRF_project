from django.urls import path, include, re_path
from .views import WomenRetrieveUpdateAPIView, WomenRetrieveDestroyAPIView, WomenListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
	path('api/v1/women/', WomenListAPIView.as_view(), name='women_list_create'),
	path('api/v1/women/delete/<int:pk>/', WomenRetrieveDestroyAPIView.as_view(), name='women_detail_delete'),
	path('api/v1/women/<int:pk>/', WomenRetrieveUpdateAPIView.as_view(), name='women_detail_update'),
	path('api/v1/auth/', include('djoser.urls')),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
