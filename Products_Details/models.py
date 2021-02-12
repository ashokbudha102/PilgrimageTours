from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Add_Feature(models.Model):
    title=models.CharField(max_length=20)
    price=models.IntegerField()

    def __str__(self):
        return self.title

class Destination(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image1=models.ImageField(upload_to='product_image',null=True,blank=True)
    image2=models.ImageField(upload_to='product_image',null=True,blank=True)
    image3=models.ImageField(upload_to='product_image',null=True,blank=True)
    feature_image=models.ImageField(upload_to='product_image',null=True,blank=True)
    other_details=models.TextField(null=True,blank=True)
    number_of_people=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    guide=models.BooleanField(default=True)
    additional_feature=models.ManyToManyField(Add_Feature,null=True,blank=True)
    slug=models.SlugField(null=True,blank=True,unique=True)

    def save(self, *args,**kwargs):
        self.slug=slugify(self.title)
        super(Destination,self).save(*args,**kwargs)

    # def get_absolute_url(self):
    #     return reverse('article_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title

