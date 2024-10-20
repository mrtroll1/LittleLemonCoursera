from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser1', password='123ewq456')

        self.client = APIClient()

        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.menu1 = Menu.objects.create(title="Pizza", menu_item_description="Cheese pizza", price=12.99)
        self.menu2 = Menu.objects.create(title="Pasta", menu_item_description="Penne pasta", price=9.99)
        self.menu3 = Menu.objects.create(title="Salad", menu_item_description="Greek salad", price=7.99)

    def test_getall(self):
        url = reverse('menu')
        
        response = self.client.get(url)
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
