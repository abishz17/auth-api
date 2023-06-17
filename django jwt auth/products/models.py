from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()

class Product(models.Model):

    CATEGORIES=(
        ('CLOTHING','clothing'),
        ('ACCESSORIES','accessories'),
    )

    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    desc=models.CharField(max_length=50)
    categories=models.CharField(max_length=20,choices=CATEGORIES)
    price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product {self.title} by {self.customer}"