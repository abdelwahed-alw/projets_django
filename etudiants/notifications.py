from django.core.mail import send_mail
from django.conf import settings
from .models import Notification

def envoyer_email(etudiant, sujet, message):
    """Envoyer un email à l'étudiant"""
    try:
        send_mail(
            sujet,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [etudiant.email],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Erreur email: {e}")
        return False

def envoyer_sms(etudiant, message):
    """Envoyer un SMS avec Twilio"""
    try:
        from twilio.rest import Client
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message[:160],  # Limite de caractères SMS
            from_=settings.TWILIO_PHONE_NUMBER,
            to=etudiant.telephone
        )
        return True
    except Exception as e:
        print(f"Erreur SMS: {e}")
        return False

def envoyer_notification(etudiant, message, canal='interne'):
    """Fonction principale d'envoi de notification"""
    
    # Créer la notification dans la base de données
    notification = Notification.objects.create(
        etudiant=etudiant,
        message=message,
        canal=canal
    )
    
    # Envoyer selon le canal
    if canal == 'email':
        envoyer_email(etudiant, "Notification", message)
    elif canal == 'sms' and etudiant.telephone:
        envoyer_sms(etudiant, message)
    
    return notification