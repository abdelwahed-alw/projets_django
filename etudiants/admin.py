from django.contrib import admin
from .models import Formation, Formateur, Etudiant, Absence, Notification

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'duree_mois')
    search_fields = ('nom',)

@admin.register(Formateur)
class FormateurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'specialite')
    search_fields = ('nom', 'prenom', 'email')

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'formation', 'date_inscription', 'actif')
    list_filter = ('formation', 'actif', 'date_inscription')
    search_fields = ('nom', 'prenom', 'email')

@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'date_absence', 'justifiee', 'creation_date')
    list_filter = ('justifiee', 'date_absence')
    search_fields = ('etudiant__nom', 'etudiant__prenom')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'canal', 'date_envoi', 'lue')
    list_filter = ('canal', 'lue', 'date_envoi')