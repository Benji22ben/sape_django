from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rembg import remove
from rest_framework.views import APIView
from PIL import Image
from io import BytesIO
import re, base64

# Create your views here.
class RemoveBGImage(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # NEED CUDA NOT WORKING
    def post(self, request, format=None):
        image_file = request.data["image"]
        base64_data = re.sub('^data:image/.+;base64,', '', image_file)
        byte_data = base64.b64decode(base64_data)
        image_data = BytesIO(byte_data)
        img = Image.open(image_data)
        image = remove(img)
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())

        print(image)
        return Response({"image": img_str})

