from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
from .models import Absence
from .notifications import envoyer_notification

@receiver(post_save, sender=Absence)
def notifier_absence(sender, instance, created, **kwargs):
    """Envoyer une notification automatique quand une absence est créée"""
    if created:
        justification = instance.justification or _('None')
        message = _('Absence recorded on %(date)s. Justification: %(justification)s') % {'date': instance.date_absence, 'justification': justification}
        
        # Notification interne toujours envoyée
        envoyer_notification(instance.etudiant, message, 'interne')
        
        # Notification email aussi
        envoyer_notification(instance.etudiant, message, 'email')
        