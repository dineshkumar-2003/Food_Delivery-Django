from .models import *
from .serializers import * 
from rest_framework import viewsets

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset=Restaurant.objects.all()
    serializer_class=RestaurantSerilaizer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class DeliveryPersonViewSet(viewsets.ModelViewSet):
    queryset=DeliveryPerson.objects.all()
    serializer_class=DeliveryPersonSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
