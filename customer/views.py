from django.shortcuts import render, redirect
from customer.forms import UserRegistraionForm, LoginForm, PlaceOrderForm
from django.contrib.auth import authenticate, login, logout
from mobile.models import Product, Cart, Orders
from mobile.views import get_object as get_product
from .decorators import loginrequired, permissionrequired


# Create your views here.
def index(request):
    return render(request, "index.html")


def registration(request, *args, **kwargs):
    form = UserRegistraionForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context["form"] = form

    return render(request, "registration.html", context)


def login_view(request, *arges, **kwargs):
    form = LoginForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                print("login success")
                login(request, user)
                return redirect("home")
            else:
                print("failed")
                context["form"] = form
    return render(request, "login.html", context)


def sign_out(request, *args, **kwargs):
    logout(request)
    return redirect("login")


@loginrequired
def user_home(request, *args, **kwargs):
    mobiles = Product.objects.all()
    context = {
        "mobiles": mobiles
    }
    return render(request, "home.html", context)


def item_detail(request, *args, **kwargs):
    id = kwargs.get("id")
    mobile = Product.objects.get(id=id)
    context = {
        "mobile": mobile
    }
    return render(request, "productdetail.html", context)


@loginrequired
def add_to_cart(request, *args, **kwargs):
    pid = kwargs.get("id")
    product = get_product(pid)
    cart = Cart(product=product, user=request.user)
    cart.save()
    return redirect("carts")


@loginrequired
def my_cart(request, *args, **kwargs):
    cart_items = Cart.objects.filter(user=request.user, status="cart")
    context = {
        "cart_items": cart_items
    }
    return render(request, "mycart.html", context)


@loginrequired
@permissionrequired
def remove_cartitem(request, *args, **kwargs):
    id = kwargs.get("id")
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect("carts")


def place_order(request, *args, **kwargs):
    pid = kwargs.get("id")
    mobile = get_product(pid)
    context = {
        "form": PlaceOrderForm(initial={"product": mobile.mobile_name})
    }
    print(kwargs)

    if request.method == "POST":
        print(kwargs)
        cid=kwargs.get("cid")
        cart=Cart.objects.get(id=cid)
        form = PlaceOrderForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data.get("address")
            product = mobile
            order = Orders(address=address, product=mobile, user=request.user)
            order.save()
            cart.status="orderplaced"
            cart.save()
            return redirect("home")

    return render(request, "placeorder.html", context)

@loginrequired
def my_order(request, *args, **kwargs):
    orders = Orders.objects.filter(user=request.user)
    context={
        "orders":orders
    }
    return render(request,"myorders.html",context)



@loginrequired
# @permissionrequired_order
def remove_order(request, *args, **kwargs):
    id = kwargs.get("id")
    order = Orders.objects.get(id=id)
    order.delete()
    return redirect("myorder")










