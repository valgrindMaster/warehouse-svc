from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('categories/', views.getCategories),
    path('products/', views.getProducts),
    path('product/<int:id>/', views.getProduct),
]
