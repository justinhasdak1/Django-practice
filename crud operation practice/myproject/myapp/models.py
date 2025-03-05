from django.db import models

# Create your models here.
class Borders(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
