from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=70)
    occupants = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Client(models.Model):
    profile = CloudinaryField('image',null=True)
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    email = models.EmailField()
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.SET_NULL, null=True)
    national_id = models.IntegerField()

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    author = models.ForeignKey(Client,on_delete=models.SET_NULL, null=True)
    body = models.TextField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author)


class Business(models.Model):
    name = models.CharField(max_length=90)
    client = models.ForeignKey(Client,on_delete=models.SET_NULL, null=True)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-updated','-created']

