from django.db import models

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="../uploads/agents", null=True)

    def __str__(self):
        return self.name


class Agent(models.Model):
    image = models.ImageField(upload_to="../uploads/agents", null=True)
    name = models.CharField(max_length=200, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    origin = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.name


class Ability(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="../uploads/abilities", null=True)
    name = models.CharField(max_length=200, null=True)
    creds = models.CharField(max_length=200, null=True)
    duration = models.CharField(max_length=200, blank=True)
    ult_points = models.PositiveSmallIntegerField(blank=True)
    detail = models.TextField(null=True)

    def __str__(self):
        return self.name



