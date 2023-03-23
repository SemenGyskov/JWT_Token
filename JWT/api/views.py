from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class BookCreate(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminUser,)
class BookList(APIView):
    def get(self,request):
        w = Book.objects.all()
        return Response({'Books':BookSerializer(w,many=True).data})
    permission_classes = (IsAuthenticatedOrReadOnly,)

class BookAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminUser,)

class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
class OrderList(APIView):
    def get(self,request):
        w = Order.objects.all()
        return Response({'Orders':OrderSerializer(w,many=True).data})
    permission_classes = (IsAuthenticated,)

class OrderAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)