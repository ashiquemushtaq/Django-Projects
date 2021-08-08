from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('cart',views.cart,name="cart"),
    path('add/<int:product_id>', views.add_cart, name="addCart"),
    path('remove/<int:product_id>', views.min_cart, name="ct_remove"),
    path('delete/<int:product_id>', views.cart_delete, name="delete"),
    path('<slug:c_slug>/',views.index,name="prod_cat"),
    path('<slug:c_slug>/<slug:p_slug>/',views.details,name="details")
]