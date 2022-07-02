from django.db import models

# Create your models here.
class ProductList(models.Model):
    pro_name = models.TextField()
    pro_description = models.TextField()
    pro_rate = models.IntegerField()
    pro_img = models.ImageField()