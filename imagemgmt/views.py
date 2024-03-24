from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rembg import remove
from rest_framework.views import APIView
import PIL.Image

# Create your views here.
class RemoveBGImage(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # NEED CUDA NOT WORKING
    def post(self, request, format=None):
        image = request.data["image"]
        image = PIL.Image.open(image)
        # image = remove(image)
        return Response({"image": image})
