from .models import Product
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):
    title=serializers.CharField(max_length=20)
    desc=serializers.CharField(max_length=50)
    categories=serializers.CharField(max_length=20)
    price=serializers.IntegerField()

    class Meta:
        model=Product
        fields=['id','title','desc','categories','price','created_at','updated_at']

class OrderDetailSerializer(serializers.ModelSerializer):
    title=serializers.CharField(max_length=20)
    desc=serializers.CharField(max_length=50)
    categories=serializers.CharField(max_length=20)
    price=serializers.IntegerField()

    class Meta:
        model=Product
        fields=['id','title','desc','categories','price','created_at','updated_at']