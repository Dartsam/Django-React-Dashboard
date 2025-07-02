from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from .serializer import *
from .models import *
from rest_framework.response import Response

class SuperMarketSalesViewSet(viewsets.ModelViewSet):
    queryset = SuperMarketSales.objects.all()
    serializer_class = SuperMarketSalesSerializer
    permission_classes = [permissions.AllowAny]

def list(self,request):
    queryset = SuperMarketSales.objects.all()
    serializer = self.serializer_class(queryset, many=True)
    return Response(serializer.data)


