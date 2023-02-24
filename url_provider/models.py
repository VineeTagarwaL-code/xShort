from django.db import models

# Create your models here.
class input_taker(models.Model):
    user_link = models.CharField(max_length=30)
    user_linkname = models.CharField(max_length=300)
    