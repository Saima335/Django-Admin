from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = (
        (1, 'Customer'),
        (2, 'Supplier'),
        (3, 'Admin'),
        (3, 'SuperAdmin')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def email(self):
        return "%s"%(self.user.email)

    def __str__(self):
        return self.user.username

class Movie(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Customer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name