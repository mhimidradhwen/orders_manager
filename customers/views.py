from django.shortcuts import render , get_object_or_404 , redirect
from .models import Customer
from orders.models import Order
from .filters import CustomerFilter
# Create your views here.

def customer_list(request):
    customers = Customer.objects.all()
    myfilter = CustomerFilter(request.GET,queryset=customers)
    customers = myfilter.qs
    context = {
        'customers':customers,
        'myfilter':myfilter
    }
    return render(request, 'customers/customer_list.html', context)

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    orders=Order.objects.filter(customer=customer)
    context ={
        'cs':customer,
        'orders':orders
    }
    return render(request, 'customers/customer_detail.html', context)
def add_customer(request):
    if request.method =="POST":
        name = request.POST.get('name',False)
        address = request.POST.get('address',False)
        phone = request.POST.get('phone',False)
        email = request.POST.get('email',False)
        new_customer = Customer(name=name,email=email,address=address,phone=phone)
        new_customer.save()
        return redirect('customer_list')
    return render(request, 'customers/add_customer.html')

def delete_customer(request,pk):
    customer1 = Customer.objects.get(id=pk)
    customer1.delete()
    return redirect('customer_list')


def search_customer(request):
    value = request.POST.get('value',False)
    if len(Customer.objects.filter(id=value))>0:
        customer = Customer.objects.filter(id=int(value)).first()
    elif len(Customer.objects.filter(name=value))>0:
        customer = Customer.objects.filter(name=value).first()
    else:
        return redirect('customer_list')
    return render(request,'customers/search_result.html',{'css':customer})

