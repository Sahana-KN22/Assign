# Django signals run in the same thread as the caller by default.

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

# Need to write this code in app/models.py
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")





# In shell or view
from myapp.models import MyModel
import threading

print(f"Caller thread: {threading.current_thread().name}")
my_instance = MyModel.objects.create(name="Test")
