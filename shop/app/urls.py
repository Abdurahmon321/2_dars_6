from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.product_list, name='product_list'),
]
