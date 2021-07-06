from django.urls import path,include
from .views import registration,login_view,sign_out,index,user_home,item_detail,add_to_cart,my_cart,remove_cartitem,place_order, \
    my_order,remove_order




urlpatterns=[
    path("index",index,name="index"),
    path("account",registration,name="registration"),
    path("signin",login_view,name="login"),
    path("signout",sign_out,name="logout"),
    path("home",user_home,name="home"),
    path("item/<int:id>",item_detail,name="item_detail"),
    path("carts",my_cart,name="carts"),
    path("carts/<int:id>",add_to_cart,name="add_to_cart"),
    path("remove/<int:id>",remove_cartitem,name="removecart"),
    path("placeorder/<int:id>/<int:cid>", place_order, name="place_order"),
    path("myorder", my_order, name="myorder"),
    path("removeorder/<int:id>",remove_order,name="removeorder"),




]