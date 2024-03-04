from rest_framework import serializers
from .models import RoomType, Room, User
from django.contrib.auth.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


# everymodel ko lagi everysingle serializer class huncha
class RoomTypeSerializer(serializers.ModelSerializer):
    # this is used to serialize RoomType model
    # serializers.modelserializer user garera chai huncha conversion
    class Meta:
        # yo bhaneko serializer ra model class ma mostly use huncha
        # parent class ko extra nature, behavious define garcha class meta le
        model = RoomType  # kun model ko object lai json ma convert garcha bhanera model atrribute ma define garne
        fields = "__all__"  # field attribute ma chai kun kunfield lai convert garne bhanera lekhne
        # sabai object lai serialize garna __all__ bhanera define gareko


class RoomSerializer(serializers.ModelSerializer):
    from rest_framework import serializers


from .models import RoomType, Room


# everymodel ko lagi everysingle serializer class huncha
class RoomTypeSerializer(serializers.ModelSerializer):
    # this is used to serialize RoomType model
    # serializers.modelserializer user garera chai huncha conversion
    class Meta:
        # yo bhaneko serializer ra model class ma mostly use huncha
        # parent class ko extra nature, behavious define garcha class meta le
        model = RoomType  # kun model ko object lai json ma convert garcha bhanera model atrribute ma define garne
        fields = "__all__"  # field attribute ma chai kun kunfield lai convert garne bhanera lekhne
        # sabai object lai serialize garna __all__ bhanera define gareko


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password","groups"]
