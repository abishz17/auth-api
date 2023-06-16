from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from rest_framework import viewsets,generics,status
from .import serializers
# Create your views here.
class ProductCreateAPIView(generics.GenericAPIView):
    serializer_class=serializers.CreateUserSerializer
    # def get(self,request):
    #     return Response(data={"msg":"From the user"})
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)