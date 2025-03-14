from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.db.models import Prefetch, Count, Q
from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodListView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        food_queryset = Food.objects.filter(is_publish=True)
        return FoodCategory.objects.annotate(total=Count('food')).filter(total__gt=0, food__is_publish=True) \
            .prefetch_related(Prefetch('food__additional', queryset=food_queryset))


def index(request):
    return render(request, 'index.html')

