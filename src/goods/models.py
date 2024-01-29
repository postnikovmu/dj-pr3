from uuid import uuid4

from django.db import models


# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()


class Token(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
