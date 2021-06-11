from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    satuts = models.BooleanField(default=True)

    class Meta:
        abstract = True



class ListContact(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null = True , blank=True)
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    photo = models.FileField(upload_to='images')



# Create your models here.
