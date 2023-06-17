from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from . import serializers
from .models import Product
from django.contrib.auth import get_user_model
# Create your views here.
User=get_user_model()

class OrderCreateListView(generics.GenericAPIView):
    serializer_class=serializers.OrderCreationSerializer
    queryset=Product.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get(self,request):
        products=Product.objects.all()
        serializer=self.serializer_class(instance=products,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        user=request.user
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(generics.GenericAPIView):
    serializer_class=serializers.OrderDetailSerializer
    permission_classes=[IsAdminUser]
    # queryset=Product.objects.all()
    def get(self,request,id):
        product=get_object_or_404(Product,pk=id)
        serializer=self.serializer_class(instance=product)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        data=request.data
        product=get_object_or_404(Product,pk=id)
        serializer=self.serializer_class(data=data,instance=product)
        # user=request.user
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        product=get_object_or_404(Product,pk=id)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class UserOrdersView(generics.GenericAPIView):
    serializer_class=serializers.OrderDetailSerializer
    def get(self,request,user_id):
        user=User.objects.get(pk=user_id)
        products=Product.objects.all().filter(customer=user)
        serializer=self.serializer_class(instance=products,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
class UserOrderDetail(generics.GenericAPIView):
    serializer_class=serializers.OrderDetailSerializer

    def get(self,request,user_id,order_id):
        user=User.objects.get(pk=user_id)
        product=Product.objects.all().filter(customer=user).get(pk=order_id)
        serializer=self.serializer_class(instance=product)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    