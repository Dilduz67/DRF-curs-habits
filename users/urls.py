from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

from users.views import CustomTokenObtainPairView, RegisterAPIView

app_name = "users"

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name="take_token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh_token"),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),  # login endpoint
    path('register/', RegisterAPIView.as_view(), name='register'),  # registration endpoint

]