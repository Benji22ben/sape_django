from rest_framework import serializers
from .models import UserData


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "firstname", "lastname", "password"]

    def create(self, validated_data):
        user = UserData.objects.create(
            email=validated_data["email"],
            firstname=validated_data["firstname"],
            lastname=validated_data["lastname"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

class UserGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "firstname", "lastname"]