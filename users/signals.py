from django.contrib.auth.models import User
from .models import ProfileModel
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# quando cadastrar um User, automaticamente ser criado um ProfileModel object

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)

@receiver(post_delete, sender=ProfileModel)
def delete_profile(sender, instance, *args, **kwargs):
    try:
        user = instance.user        
        print(user.username + 'SENDO DELETADO')
        user.delete()
    except User.DoesNotExist:
        pass