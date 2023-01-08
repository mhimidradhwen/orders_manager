from django.urls import path
from . import views

urlpatterns = [

    path('orders/', views.order_list, name='order_list'),
    path('orders/add',views.add_order,name='add_order'),
    path('orders/delete/<int:pk>/',views.delete_order,name='delete_order'),
    path('orders/view/<int:pk>/',views.order_detail,name='order_detail'),
    path('orders/deliver/<int:pk>/',views.deliver_order,name='deliver_order'),
    
   
]
