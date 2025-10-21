from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class AccountViewsTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.public_url = reverse('public_view')
        self.protected_url = reverse('protected_view')
        self.register_url = reverse('user-registration')
        self.token_obtain_pair_url = reverse('token_obtain_pair')

        
        self.username = 'testuser'
        self.email = 'test@example.com'
        self.password = 'testpassword123'
        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            first_name='Test',
            last_name='User'
        )

    def get_auth_token(self):
        response = self.client.post(self.token_obtain_pair_url, {'username': self.username, 'password': self.password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']

    def test_public_view_access(self):
        response = self.client.get(self.public_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'публічна інформація'})

    def test_protected_view_access_unauthenticated(self):
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_protected_view_access_authenticated(self):
        access_token = self.get_auth_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'захищена інформація'})