from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Formation(models.Model):
    nom = models.CharField(max_length=200)
    duree_mois = models.IntegerField(default=12)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"

class Formateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    specialite = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    class Meta:
        verbose_name = "Formateur"
        verbose_name_plural = "Formateurs"

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True)
    date_naissance = models.DateField()
    formation = models.ForeignKey(Formation, on_delete=models.SET_NULL, null=True, related_name='etudiants')
    date_inscription = models.DateField(auto_now_add=True)
    actif = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"
    
    def get_absolute_url(self):
        return reverse('etudiant_detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"

class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='absences')
    date_absence = models.DateField()
    justification = models.TextField(blank=True, null=True)
    justifiee = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.etudiant} - {self.date_absence}"
    
    class Meta:
        verbose_name = "Absence"
        verbose_name_plural = "Absences"
        ordering = ['-date_absence']

class Notification(models.Model):
    CANAL_CHOICES = [
        ('interne', 'Interne (App)'),
        ('email', 'Email (Gmail)'),
        ('sms', 'SMS (Twilio)'),
    ]
    
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    canal = models.CharField(max_length=10, choices=CANAL_CHOICES, default='interne')
    date_envoi = models.DateTimeField(auto_now_add=True)
    lue = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Notification pour {self.etudiant} - {self.get_canal_display()}"
    
    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ['-date_envoi']