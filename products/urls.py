from django.urls import path, include

from products.views import ProductListView, get_carts, select_one_cart, create_new_group_cart

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/carts', get_carts),
    path('/carts/<int:cart_id>', select_one_cart),
    path('/create-cart', create_new_group_cart),
]
