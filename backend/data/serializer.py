from rest_framework import serializers
from .models import *

class SuperMarketSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperMarketSales
        fields = ('id','unit_price','quantity','date','branch','country','customer_type','gender', 'product_line','payment')


