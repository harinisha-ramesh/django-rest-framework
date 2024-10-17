from django.urls import path
from .views import * 

urlpatterns = [
    path('products/',ProductView.as_view()),
    path('products/<int:id>/',ProductViewById.as_view()),
    path('category/',CategoryView.as_view()),
    path('category/<int:id>/',CategoryViewById.as_view()),
]
