from django.db import models

# Create your models here.


class Details(models.Model):

    name = models.CharField(max_length=50)
    dob = models.DateField()
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    height = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.name