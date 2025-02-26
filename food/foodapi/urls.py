from django.urls import path
from .views import FoodListView, index

urlpatterns = [
    path('api/v1/foods', FoodListView.as_view()),
    path('', index)
]
