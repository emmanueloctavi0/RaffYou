
# Django
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.db import transaction

# Django REST framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from products.models import Product, Provider

CART_PRODUCT_URL = reverse('carts:cartproduct-list')


class PrivateCartProductApiTest(TestCase):
    """Test authenticated cart product API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='secret@123',
        )

        self.client.force_authenticate(user=self.user)
        self.provider1 = Provider.objects.create(
            name='provider1'
        )

        self.product1 = Product.objects.create(
            name='product_name',
            address='address 1 blue',
            price=12,
            provider=self.provider1
        )

    def test_fail_add_product_to_cart(self):
        """Test add product with empty payload to user cart"""
        payload = {
        }

        res = self.client.post(CART_PRODUCT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_product_to_cart(self):
        """Test add a product with a valid payload"""
        payload = {
            'product': self.product1.id
        }
        res = self.client.post(CART_PRODUCT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
