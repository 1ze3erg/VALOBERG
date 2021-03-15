from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    image = models.ImageField(upload_to="../uploads/weapons", null=True)
    name = models.CharField(max_length=200, null=True)
    types = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    fire_mode = models.CharField(max_length=200, null=True)
    creds = models.CharField(max_length=200, null=True)
    magazine = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name


class Skin(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="../uploads/skins")
    collection = models.CharField(max_length=200, null=True)
    unlock = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.collection
