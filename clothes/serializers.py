from rest_framework import serializers
from .models import Clothing, Outfit


class ClothingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clothing
        fields = "__all__"
        read_only_fields = ["user"]


class OutfitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Outfit
        fields = ("name",)


class OutfitStep2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Outfit
        fields = "__all__"
