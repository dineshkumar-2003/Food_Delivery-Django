from django.urls import path,include
from .views import *

urlpatterns = [
    # User Endpoints
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    # Restaurant Endpoints
    path('restaurants/', RestaurantListCreate.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),

    # Menu Item Endpoints
    path('menu_items/', MenuItemListCreate.as_view(), name='menu-item-list-create'),
    path('menu_items/<int:pk>/', MenuItemDetail.as_view(), name='menu-item-detail'),

    # Customer Endpoints
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),

    # Delivery Person Endpoints
    path('delivery_persons/', DeliveryPersonListCreate.as_view(), name='delivery-person-list-create'),
    path('delivery_persons/<int:pk>/', DeliveryPersonDetail.as_view(), name='delivery-person-detail'),

    # Order Endpoints
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('orders/<int:pk>/actions/<str:action>/', OrderActionsView.as_view(), name='order-actions'),
    path('orders/filter_by_status/', OrderFilterView.as_view(), name='order-filter'),

    # Delivery Endpoints
    path('deliveries/', DeliveryListCreate.as_view(), name='delivery-list-create'),
    path('deliveries/<int:pk>/', DeliveryDetail.as_view(), name='delivery-detail'),

    # Payment Endpoints
    path('payments/', PaymentListCreate.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentDetail.as_view(), name='payment-detail'),
]

