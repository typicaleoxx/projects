from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import RoomType, Room
from .serializers import RoomTypeSerializer, RoomSerializer

# Create your views here.
# everymodel ko CRUD operation  garna
# views ma define garne
# restframework ko class banaunu parcha
# sothat API class huncha, ani url ma user le request gareko anusar pass garna milcha
# WE USE DJANGO REST FRAMEWORK
# api ma hune everything all the logic is inside rest framework
# so we use djangorest framework
# to use it we must also define in settings


class RoomTypeView(ModelViewSet):
    # modelviewset lai inherit garera normal class lai we made api view class
    # crud operation ko lagi afai le define nai garna pardaina everything is inside rest framework
    # it has two requirement i.e query_set and serializer_class
    # queryset=   #kun model ma crud garne ho define garne yeta
    # serializer_class=#component where object lai json and json lai object ma convert garna milcha
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
