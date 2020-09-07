from django.dispatch import receiver

from djoser.signals import user_activated
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(user_activated)
def create_user_profile_receiver(sender, **kwargs):
    user = kwargs['user']
    User.objects.create_user_profile(user=user)
