from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.OrderCreateListView.as_view()),
    path('<int:id>/', views.OrderDetailView.as_view()),
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view()),
    path('user/<int:user_id>/order/<int:order_id>',views.UserOrderDetail.as_view()),
]