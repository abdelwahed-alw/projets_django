from django import forms
from .models import Etudiant, Absence, Notification

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email', 'telephone', 'date_naissance', 'formation', 'actif']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
        }

class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['etudiant', 'date_absence', 'justification', 'justifiee']
        widgets = {
            'date_absence': forms.DateInput(attrs={'type': 'date'}),
        }

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['etudiant', 'canal', 'message']