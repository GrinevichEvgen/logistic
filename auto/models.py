from django.db import models
from drivers.models import Driver


class Auto(models.Model):

    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    state_number = models.IntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='autos')

    def __str__(self):
        return f"{self.state_number} {self.make} {self.model}"
