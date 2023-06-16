from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
# router =DefaultRouter()
# router.register('user',views.ProductViewSet,basename='product')
urlpatterns = [
    path('signup/', views.ProductCreateAPIView.as_view()),
]