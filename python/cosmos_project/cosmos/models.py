from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    type = models.CharField(max_length=100, verbose_name="Тип")
    distance_from_sun = models.FloatField(verbose_name="Расстояние от Солнца (млн км)")

    def __str__(self):
        return self.name

class Satellite(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name="satellites", verbose_name="Планета")

    def __str__(self):
        return self.name

class Mission(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название миссии")
    description = models.TextField(verbose_name="Описание")
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name="missions", verbose_name="Целевая планета")
    date = models.DateField(verbose_name="Дата запуска")

    def __str__(self):
        return self.name
