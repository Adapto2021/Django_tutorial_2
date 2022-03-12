from django.db import models

# Create your models here.

class BookNumber(models.Model):
    isbn_10=models.CharField(max_length=10)
    isbn_13=models.CharField(max_length=13)



class Book(models.Model):
    #title=models.CharField(max_length=36)#CharField is simple text. Max lenght 36
     title=models.CharField(blank=False,unique=True,max_length=36)
     description=models.TextField(max_length=256,blank=True)
     price=models.DecimalField(default=0,max_digits=10,decimal_places=2)# can have max_digit param, you can also use FloatFields
     #published=models.DateField(auto_now=True,auto_now_add=True)
     published = models.DateField(blank=True,null=True,default=None)
     is_published=models.BooleanField(default=False)
     cover=models.ImageField(upload_to='covers/',blank=True)
     #One to One
     number=models.OneToOneField(BookNumber,null=True,blank=True,on_delete=models.CASCADE)


     def __str__(self):
         return self.title


class Character(models.Model):
    name=models.CharField(max_length=30)
    # One to Many
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='characters')


class Authors(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    # Many to Many
    books = models.ManyToManyField(Book, related_name='authors')