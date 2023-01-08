from django.urls import path
from . import views

urlpatterns = [

    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/add/',views.add_customer,name='add_customer'),
    path('customers/delete/<int:pk>/',views.delete_customer,name='delete_customer'),
    path('customers/result/',views.search_customer,name='search_customer'),
]
