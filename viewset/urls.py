from django.urls import path, include
from .views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'list', MyReadOnlyViewSet, basename= 'readonlyproducts')

urlpatterns = [
    path('', include(router.urls)),
]

