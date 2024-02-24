from django.db import models
from frontdesk.models import Customer


# Create your models here.
class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    total_amount = models.IntegerField()


class Payment(models.Model):
    bill = models.OneToOneField(Bill, on_delete=models.SET_NULL, null=True)


# euta bill lai ekchoti matra pay garne bhayera onetoone relationship bhako
# so tyo relationship use garna onetoonefield user gareko
