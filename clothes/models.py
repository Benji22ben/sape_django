from django.db import models
from enum import Enum
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Season(Enum):
    WINTER = "winter"
    SUMMER = "summer"
    SPRING = "spring"
    FALL = "fall"
    ALL = "all"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def get_season(cls, temperature):
        if temperature < 4:
            return cls.WINTER.value
        elif temperature >= 25:
            return cls.SUMMER.value
        elif temperature > 15 and temperature < 25:
            return cls.SPRING.value
        elif temperature >= 4 and temperature < 15:
            return cls.FALL.value
        else:
            return cls.ALL.value


class ClothesType(models.Model):
    name = models.CharField(max_length=100)
    season = models.CharField(
        max_length=1, choices=Season.choices(), default=Season.ALL.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Pattern(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="patterns")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    why_its_bad = models.TextField()
    why_its_good = models.TextField()
    score = models.IntegerField(max=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    reputation = models.IntegerField(max=100)
    ecoreputation = models.IntegerField(max=100)
    description = models.TextField()
    why_its_bad = models.TextField()
    why_its_good = models.TextField()
    material_used = models.TextField()
    fabrication_location = models.CharField(max_length=100)
    material = models.ManyToManyField(Material)
    logo = models.ImageField(upload_to="brands")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Clothing(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="clothes")
    type = models.ForeignKey(ClothesType, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    color = ArrayField(models.CharField(max_length=6), default=list)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    principal_material = models.ManyToManyField(Material)
    secondary_material = models.ManyToManyField(
        Material, related_name="secondary_material"
    )
    weather = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
