from django.db import models
from drivers.models import Driver
from auto.models import Auto


class Route(models.Model):
    start_time = models.DateTimeField()
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='routs')
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='routs')

    def __str__(self):
        return f"Auto from {self.start_location} to {self.end_location}"
