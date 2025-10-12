from django.urls import path
from .views import UserRegistrationView, LogOutView, PublicView, ProtectedView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogOutView.as_view(), name='auth_logout'),
    path('public/', PublicView.as_view(), name='public_view'),
    path('protected/', ProtectedView.as_view(), name='protected_view'),
]