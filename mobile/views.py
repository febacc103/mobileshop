from django.shortcuts import render,redirect
from .forms import ProductCreateForm
from .models import Product


# Create your views here.


def Create_Product(request):
    form=ProductCreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProductCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("fetchitems")
        else :
            context["form"]=form
            return render(request, "product_create.html", context)

    return render(request,"product_create.html",context)




def list_products(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"product_list.html",context)


def get_object(id):
    return Product.objects.get(id=id)

def edit_item(request,*args,**kwarges):
    id=kwarges.get("id")
    product=get_object(id)

    form=ProductCreateForm(instance=product)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProductCreateForm(instance=product,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("fetchitems")
    return render(request,"edit_product.html",context)


def product_detail(request,*args,**kwarges):
    id = kwarges.get("id")
    product = get_object(id)
    context={}
    context["product"]=product

    return render(request,"product_detail.html",context)


def delete_product(request,*args,**kwarges):
    id=kwarges.get("id")
    product=get_object(id)
    product.delete()
    return redirect("fetchitems")




