from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'restaurant',RestaurantViewSet)
router.register(r'menuitem',MenuItemViewSet)
router.register(r'customer',CustomerViewSet)
router.register(r'deliveryperson',DeliveryPersonViewSet)
router.register(r'order',OrderViewSet)
router.register(r'payment',PaymentViewSet)
urlpatterns=[
    path('',include(router.urls))
]