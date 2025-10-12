from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.validated_data
            user = User.objects.create_user(
                username=valid_data["username"],
                email=valid_data["email"],
                password=valid_data["password"],
                first_name=valid_data["first_name"],
                last_name=valid_data["last_name"],
            )
            return Response({"message": "користувач створений."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
class LogOutView(APIView):
    def post(self, request):   
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "успішний вихід."}, status=status.HTTP_205_RESET_CONTENT)
        
class PublicView(APIView):
    def get(self, request):
        return Response({"message": "публічна інформація"}, status=status.HTTP_200_OK)       


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": "захищена інформація"}, status=status.HTTP_200_OK)
