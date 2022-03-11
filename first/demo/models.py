from django.db import models

# Create your models here.
class Book(models.Model):
    #title=models.CharField(max_length=36)#CharField is simple text. Max lenght 36
     title=models.CharField(blank=False,unique=True,max_length=36)
     description=models.TextField(max_length=256,blank=True)
     price=models.DecimalField(default=0,max_digits=10,decimal_places=2)# can have max_digit param, you can also use FloatFields
     #published=models.DateField(auto_now=True,auto_now_add=True)
     published = models.DateField(blank=True,null=True,default=None)
     is_published=models.BooleanField(default=False)
     cover=models.ImageField(upload_to='covers/',blank=True)

     def __str__(self):
         return self.title


