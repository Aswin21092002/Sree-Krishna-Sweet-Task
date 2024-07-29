# sweets_shop/models.py

from django.db import models

class Zone(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=100)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Complaint(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Complaint for {self.shop.name}"
