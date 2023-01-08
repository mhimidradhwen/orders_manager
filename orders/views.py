from django.shortcuts import render ,redirect
from .models import Order
from customers.models import Customer
from products.models import Product
# Create your views here.
def order_list(request):
    orders = Order.objects.all()
    delivred = Order.objects.filter(state="green")
    all_orders = orders.count()
    delivred_number = delivred.count()    
    context={
        'delivred':delivred,
        'orders':orders,
        'delivred_number':delivred_number,
        'all_orders_number':all_orders
    }
    
    return render(request,'orders/order_list.html',context)

def add_order(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    context = {
        'products':products,
        'customers':customers
    }
    quantity = request.POST.get('quantity',False)
    customer_name = request.POST.get('customer',False)
    product_name = request.POST.get('product',False) 
    
    if product_name and product_name != '':
    
        customer = Customer.objects.filter(name=customer_name).first()
        product = Product.objects.filter(name=product_name).first()
    
        new_order = Order(customer=customer,product=product,quantity=quantity)
        new_order.calculate_price()
        new_order.save()   
    return render(request, 'orders/add_order.html',context)

def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('order_list')

def order_detail(request,pk):
    order = Order.objects.get(id=pk)
    product =Product.objects.get(id=order.product.id)
    customer =Customer.objects.get(id=order.customer.id)
    context ={
        'order':order,
        'pr':product,
        'cs':customer,
    }
    return render(request, 'orders/order_detail.html',context)

def deliver_order(request,pk):
    order = Order.objects.get(id=pk)
    order.state="green"
    order.save()
    return redirect('order_list')