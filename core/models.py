from django.db import models

# Create your models here.
class Greedfall(models.Model):
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class Witcher(models.Model):
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class Untildawn(models.Model):
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class Acvalhalla(models.Model):
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class Cyberpunk(models.Model):
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class Godofwar(models.Model):
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class Daysgone(models.Model):
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class Immortals(models.Model):
    price = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

class Update(models.Model):
    date = models.DateTimeField(auto_now_add=True)