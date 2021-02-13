from django.db import models

# Create your models here.
class about(models.Model):
    name=models.CharField(default='NULL',max_length = 50)
    image = models.ImageField(null=True,blank=True,upload_to='legal_document')
    text = models.TextField(default="Null")



