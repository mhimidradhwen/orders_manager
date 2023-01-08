from django.shortcuts import render ,get_object_or_404 , redirect
from .models import Product
from orders.models import Order
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product1=Product.objects.get(id=pk)
    orders = Order.objects.filter(product=product1)
    total = orders.count()
    context = {
        'pr':product,
        'total':total,
    }
    return render(request, 'products/product_detail.html',context)

def add_product(request):
    if request.method == 'POST':
        namep = request.POST.get('namep',False)
        price = request.POST.get('Price',False)
        description = request.POST.get('Description',False)
        product = Product(name=namep, price=price, description=description)
        product.save()
        return redirect('product_list')
    return render(request, 'products/add.html')


def update_product(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        namep = request.POST.get('namep',False)
        price = request.POST.get('Price',False)
        description = request.POST.get('Description',False)
        product_updated = Product(id=pk,name=namep, price=price, description=description)
        product_updated.save()
        return redirect('product_list')
    return render(request, 'products/update_product.html',{'product':product})


def delete_product(request,pk):
    p = Product.objects.get(id=pk)
    p.delete()
    return redirect('product_list')
    return render(request, 'products/delete_product.html',{'product':p})
