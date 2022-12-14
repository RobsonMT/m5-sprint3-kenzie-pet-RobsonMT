from tokenize import group
from uuid import uuid4
from django.db import models


class Animal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15)

    group = models.ForeignKey(
        to="groups.Group", on_delete=models.CASCADE, related_name="animals"
    )

    characteristics = models.ManyToManyField(to="characteristics.Characteristic")
