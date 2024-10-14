from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandModelViewSet, CarModelViewSet


router = DefaultRouter()
router.register('brands', BrandModelViewSet)
router.register('cars', CarModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]