from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.siteuser.models import User
from apps.siteuser.tasks import SendConfirmationEmail


@receiver(post_save, sender=User)
def create_lawyer_details(sender, instance, created, **kwargs):
    if created:
        task = SendConfirmationEmail(username=instance.first_name, id=instance.id, hash=instance.hash,
                                 email=instance.email)
        task.delay()