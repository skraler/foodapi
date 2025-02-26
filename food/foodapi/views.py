from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.db.models import Prefetch, Count, Q
from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodListView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        return FoodCategory.objects.prefetch_related(
            Prefetch(
                'food',
                queryset=Food.objects.filter(is_publish=True)
            )
        ).annotate(
            published_food_count=Count(
                'food',
                filter=Q(food__is_publish=True)
            )
        ).filter(
            published_food_count__gt=0
        ).order_by('order_id', 'name_ru')


def index(request):
    return render(request, 'index.html')

