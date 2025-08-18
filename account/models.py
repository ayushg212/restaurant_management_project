from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete= models.CASCADE)
    full_name = models.CharField(max_length = 150 , blank = True )
    email = models.EmailField(blank = True)
    phone_number = models.CharField(max_length = 20 , blank = True)

    def __str__(self):
        return self.full_name or self.user.username

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_or_save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, email = getattr(instance, 'email', ''))
    else:
        instance.Profile.save() if hasattr(instance, 'profile') else none
