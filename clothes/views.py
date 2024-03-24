from itertools import chain
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.views import APIView
from .models import Clothing, Outfit
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ClothingSerializer, OutfitSerializer, OutfitStep2Serializer
from random import sample


class UserClothing(APIView):
    model = Clothing
    serializer_class = ClothingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, format=None):
        data = Clothing.objects.filter(user=self.request.user)
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)


class AppClothing(APIView):
    model = Clothing
    serializer_class = ClothingSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, format=None):
        data = Clothing.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)


class CoherentOutfit(APIView):
    model = Outfit
    serializer_class = OutfitSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, format=None):

        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        serializer.is_valid(raise_exception=True)
        user = self.request.user
        top = Clothing.objects.filter(user=user, type=1)
        bottom = Clothing.objects.filter(user=user, type=2)
        shoes = Clothing.objects.filter(user=user, type=5)

        outfit_clothes = list(
            chain(sample(list(top), 1), sample(list(bottom), 1), sample(list(shoes), 1))
        )

        outfit_ids = [clothes.id for clothes in outfit_clothes]

        serializerStep2 = OutfitStep2Serializer(
            data={
                "user": user.id,
                "clothes": outfit_ids,
                "name": request.data["name"],
            }
        )
        serializerStep2.is_valid(raise_exception=True)

        # Debug
        # for name, value in vars(serializerStep2.data).items():
        #     print(f"{name}: {value}")
        # return Response({"outfit": outfit_ids, "name": request.data["name"]})

        serializerStep2.save()

        return Response(serializerStep2.data)

    def get(self, request, format=None):
        data = Outfit.objects.filter(user=self.request.user)
        serializer = OutfitStep2Serializer(data, many=True)
        return Response(serializer.data)
