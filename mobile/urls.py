
from django.urls import path
from .views import Create_Product,list_products,edit_item,product_detail,delete_product



urlpatterns=[
    path("products",Create_Product,name="create_product"),
    path("items",list_products,name="fetchitems"),
    path("item/change/<int:id>",edit_item,name="change"),
    path("item/<int:id>",product_detail,name="product_detail"),
    path("item/remove/<int:id>",delete_product,name="remove"),



]


