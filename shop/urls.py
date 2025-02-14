from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('categories/', views.getCategories, name="get_categories"),
    path('products/', views.getProducts, name="get_products"),
    path('product/<int:id>/', views.getProduct, name="get_product"),
]
