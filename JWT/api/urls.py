from django.urls import path
from .views import *

urlpatterns = [
    path('orders/', OrderList.as_view(), name='orders'),
    path('orders/<int:pk>/', OrderAPIUpdate.as_view(), name='order-detail'),
    path('orders-add/', OrderCreate.as_view(), name='order-create'),
    path('books/', BookList.as_view(), name='books'),
    path('books/<int:pk>/', BookAPIUpdate.as_view(), name='book-detail'),
    path('books-add/', BookCreate.as_view(), name='book-create'),
]