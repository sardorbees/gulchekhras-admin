from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet,
    ProductListView, CategoryListView, ColorListView, SizeListView, DressTypeListView, ProductSearchView
)

# --- DRF Router ---
router = DefaultRouter()
router.register(r'products', ProductViewSet)

# --- URL patterns ---
urlpatterns = [
    path('', include(router.urls)),

    # Классические CBV для фильтров и поиска
    path('filters/categories/', CategoryListView.as_view(), name='category-list'),
    path('filters/colors/', ColorListView.as_view(), name='color-list'),
    path('filters/sizes/', SizeListView.as_view(), name='size-list'),
    path('filters/dresses/', DressTypeListView.as_view(), name='dress-list'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    # Если нужно, можно оставить дублирующий путь для категорий
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
