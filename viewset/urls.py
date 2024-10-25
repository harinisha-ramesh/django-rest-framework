from django.urls import path, include
from .views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'list', MyReadOnlyViewSet, basename= 'readonlyproducts')
router.register(r'generic_product', ProductGenericViewSet, basename= 'generic_product')

urlpatterns = [
    path('', include(router.urls)),
    # path('generic_product/',ProductGenericViewSet.as_view(),name='generic_product'),
]

