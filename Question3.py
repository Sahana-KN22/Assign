# By default Django signals run within the same transaction as the caller

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Need to write this code in app/models.py
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print("Signal started")
    raise Exception("Error in signal")




# In Shell or views file
from myapp.models import MyModel

try:
    my_instance - MyModel.objects.create(name="Test")
except Exception as e:
    print(f"Exception: {e}")    

print(MyModel.objects.all())    # To check if the object saved or not