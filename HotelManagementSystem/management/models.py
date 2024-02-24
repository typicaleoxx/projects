from django.db import models
from django.contrib.auth.models import AbstractUser

# django ko user table modify garera use garna lako
# for that we're using abstract user


# this is custom user table
class User(AbstractUser):
    email = models.EmailField(
        unique=True
    )  # using unique argument to avoid conflicts later if any user uses same email
    password = models.CharField(max_length=200)
    # password field stays encrypted, and after encription it has longer value
    # thats why we're using max length 200
    username = models.CharField(max_length=200, null=True)
    # we're overwriting django user table to user USERNAME_FIELD
    # DJANGO ask for username and password field for user indentification
    # when any variable is in all upper
    # it is called CONSTANT VARIABLE
    # value is not constant but only name is
    # if we use django default user table it does
    # USERNAME_FIELD="username"(username field chai password pachi ko arko field ho)
    # so we change it with email
    # (email field chai password pachi ko arko field)#this is the modification we did by creating our own user table
    # because username bhanda it feels more secure to use email field
    USERNAME_FIELD = "email"  # password pachi magne bhanera email field define gareko
    # after this username field seems like neglected so required field bhanera define gareko
    REQUIRED_FIELDS = ["username"]#superuser create garda username field magcha nai so error dincha if not inserted, thats why required


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
