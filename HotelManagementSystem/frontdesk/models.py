from django.db import models
from management.models import Room


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    contact_no = models.IntegerField()


# hamle table create gareko bhayera if customer comes again, feri define garirakhnu parena
REQUIRED_FIELD = ["email"]


class CustomerRoom(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
