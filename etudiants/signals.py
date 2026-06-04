from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Absence
from .notifications import envoyer_notification

@receiver(post_save, sender=Absence)
def notifier_absence(sender, instance, created, **kwargs):
    """Envoyer une notification automatique quand une absence est créée"""
    if created:
        message = f"Absence enregistrée le {instance.date_absence}. Justification: {instance.justification or 'Aucune'}"
        
        # Notification interne toujours envoyée
        envoyer_notification(instance.etudiant, message, 'interne')
        
        # Notification email aussi
        envoyer_notification(instance.etudiant, message, 'email')
        