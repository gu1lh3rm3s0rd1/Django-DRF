from django.shortcuts import render
from cars.models import Brand, Car
from rest_framework import viewsets
from .serializers import BrandModelSerializer, CarModelSerializer
from dj_rql.drf import RQLFilterBackend
from .filters import BrandFilterClass, CarFilterClass

# Create your views here.


class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    filter_backends = (RQLFilterBackend,)
    rql_filter_class = BrandFilterClass


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = (RQLFilterBackend,)
    rql_filter_class = CarFilterClass

# get
class CarList(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = (RQLFilterBackend,)
    rql_filter_class = CarFilterClass