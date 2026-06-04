from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from etudiants.models import Etudiant

class Command(BaseCommand):
    help = 'Envoie des rappels de cours aux étudiants'

    def handle(self, *args, **options):
        etudiants = Etudiant.objects.filter(actif=True)
        sujet = "Rappel: Cours aujourd'hui"
        message = "Ceci est un rappel pour vos cours programmés aujourd'hui."
        
        for etudiant in etudiants:
            try:
                send_mail(
                    sujet,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [etudiant.email],
                    fail_silently=False,
                )
                self.stdout.write(f"Email envoyé à {etudiant.email}")
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erreur pour {etudiant.email}: {e}"))