from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from core.models import Well
from core.serializers import WellSerializer


# Create your views here.
class WellViewset(ModelViewSet):
    queryset = Well.objects.all()
    serializer_class = WellSerializer
    permission_classes = [AllowAny,]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['well',]
    search_fields = ['well',]
    ordering_fields = ['well',]
    pagination_class  = PageNumberPagination