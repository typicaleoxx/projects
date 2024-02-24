from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    # menu bhanna le book haina but
    # different datas that group food
    # like tea-milk tea,black tea
    # coffee-espresso, machiato


# menu and food has relationship
# menu-to define different group data
# food - grp ko bhitra parne data, sub grp data
class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    # menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    # cascade rakhda if menu class ma its deleted then menu field ma ni it gets deleted
    # but if set null rakhda, euta ma del bhayepachi aru ma null bhanera bascha
    # ondelete is a required argument
