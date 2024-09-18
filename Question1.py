# By default, Django signals are executed synchronously. 
"""This means when a signal is sent, the execution of the code waits until the signal's receivers 
have finished executing before moving on."""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

# Need to write this code in app/models.py
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print("Signal started")    
    time.sleep(5)
    print("Signal finished")



    
# Then in Django shell we need to import the model and create an instance to trigger the post_save signal    
from myapp.models import MyModel

print("Creating MyModel instance")    
instance = MyModel.objects.create(name="Test")
print("MyModel instance created")

# or we can write a view to trigger the signal