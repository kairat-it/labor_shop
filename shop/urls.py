from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('products/add/', views.add_product, name='add_product'),
]
