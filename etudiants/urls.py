from django.urls import path
from . import views

app_name = 'etudiants'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    
    # Étudiants
    path('etudiants/', views.liste_etudiants, name='liste_etudiants'),
    path('etudiants/ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('etudiants/<int:pk>/modifier/', views.modifier_etudiant, name='modifier_etudiant'),
    path('etudiants/<int:pk>/supprimer/', views.supprimer_etudiant, name='supprimer_etudiant'),
    path('etudiants/<int:pk>/', views.detail_etudiant, name='detail_etudiant'),
    
    # Formations
    path('formations/', views.liste_formations, name='liste_formations'),
    
    # Absences
    path('absences/', views.liste_absences, name='liste_absences'),
    path('absences/ajouter/', views.ajouter_absence, name='ajouter_absence'),
    
    # Notifications
    path('notifications/', views.liste_notifications, name='liste_notifications'),
    path('notifications/envoyer/', views.envoyer_notification_view, name='envoyer_notification'),
    path('notifications/<int:pk>/lue/', views.marquer_lue, name='marquer_lue'),
    path('notifications/<int:pk>/supprimer/', views.supprimer_notification, name='supprimer_notification'),
]