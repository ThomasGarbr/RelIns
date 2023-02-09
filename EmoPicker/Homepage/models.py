from django.db import models

# Create your models here.

class DataSetText(models.Model):
    text = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return str(self.pk) + "|" +self.text[:50] + "..."