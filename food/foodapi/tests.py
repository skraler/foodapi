from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import FoodCategory, Food


class FoodAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category1 = FoodCategory.objects.create(
            name_ru="Напитки",
            name_en="Drinks",
            order_id=10
        )
        self.category2 = FoodCategory.objects.create(
            name_ru="Выпечка",
            order_id=20
        )
        self.category3 = FoodCategory.objects.create(
            name_ru="Овощи",
            order_id=30
        )

        self.food1 = Food.objects.create(
            internal_code=100,
            code=1,
            name_ru="Чай",
            description_ru="Чай 100 гр",
            cost="123.00",
            category=self.category1
        )
        self.food2 = Food.objects.create(
            internal_code=200,
            code=2,
            name_ru="Кола",
            description_ru="Кола",
            cost="123.00",
            category=self.category1
        )
        self.food3 = Food.objects.create(
            internal_code=300,
            code=3,
            name_ru="пирог",
            description_ru="пирог",
            cost="100.00",
            category=self.category2
        )
        self.food4 = Food.objects.create(
            internal_code=400,
            code=4,
            name_ru="сосиска в тесте",
            description_ru="",
            cost="103.00",
            category=self.category2,
            is_publish = False
        )
        self.food5 = Food.objects.create(
            internal_code=500,
            code=5,
            name_ru="томат",
            description_ru="",
            cost="203.00",
            category=self.category3,
            is_publish=False
        )

    def test_get_categories(self):
        response = self.client.get('/api/v1/foods')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

