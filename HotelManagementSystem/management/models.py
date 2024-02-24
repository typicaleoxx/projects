from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class RoomType(models.Model):
    name = models.CharField(max_length=200)


class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # type field is a relationship field
    # since type field has OTM relation, Foreignkey class is being used
    # foreignkey defines relationship between table RoomType and Room in the Type field
    # type field ma onetomany relationship cha

    type = models.ForeignKey(
        RoomType, on_delete=models.CASCADE
    )  # roomtype sanga chai type field ko relation cha, so we're using it
    # ondelete le chai if kunai id ko roomtype data roomtype table bata delete bhayo bhane, bhanera were defining on_delete rakhhera cascade rakheko so
    # cascade rakhera chai is RoomType bata delete bhayo bhane type ma pani delete huncha
    # if we dont want it to delete then we write models.SET_NULL, null=True
    floor = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
