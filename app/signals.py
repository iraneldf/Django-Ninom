from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from app.models import fruit


@receiver(post_save, sender=fruit)
def create_fruit(sender, instance, **kwargs):
    try:
        print('Funciona el signaaaaaaaaaaaaaaaaaal')
    except:
        pass
