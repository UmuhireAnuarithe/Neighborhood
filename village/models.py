from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
   Profile_picture= models.ImageField(upload_to = 'pictures/')
   email = models.EmailField()
   user_bio = models.CharField(max_length =30)
   location = models.CharField(max_length =30)
   def __str__(self):
      return self.location
   def save_profile(self):
      self.save()

   def update_profile(self):
      self.update()

   def delete(self):
      self.delete()

class Village(models.Model):
   village = models.CharField(max_length =30 )
   location = models.CharField(max_length =70 )
   population = models.IntegerField(default=0)
   village_image= models.ImageField(upload_to = 'pictures/',null=True)
   def __str__(self):
      return self.location
   def save_village(self):
      self.save()

   def update_village(self):
      self.update()

   def delete(self):
      self.delete()

   @classmethod
   def get_village_by_id(cls, id):
      village = Village.objects.filter(id=Village.id)
      return village


class Events(models.Model):
   name = models.CharField(max_length =30 )
   description = models.TextField(max_length= 300)
   username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
   event_image= models.ImageField(upload_to = 'pictures/',null=True)

   def __str__(self):
      return self.name
   def save_events(self):
      self.save()

   def update_events(self):
      self.update()

   def delete(self):
      self.delete()
class Business(models.Model):
   business_image= models.ImageField(upload_to = 'pictures/',null=True)
   name = models.CharField(max_length =300)
   description = models.TextField(max_length= 300)
   owner = models.CharField(max_length =30) 

   def __str__(self):
      return self.name
   def save_business(self):
      self.save()

   def update_business(self):
      self.update()

   def delete(self):
      self.delete()
