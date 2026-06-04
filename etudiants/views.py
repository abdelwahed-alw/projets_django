from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils.translation import gettext as _
from .models import Etudiant, Formation, Formateur, Absence, Notification
from .forms import EtudiantForm, AbsenceForm, NotificationForm
from .notifications import envoyer_notification

def accueil(request):
    """Page d'accueil"""
    total_etudiants = Etudiant.objects.count()
    total_formations = Formation.objects.count()
    total_absences = Absence.objects.count()
    notifications_non_lues = Notification.objects.filter(lue=False).count() if request.user.is_authenticated else 0
    
    context = {
        'total_etudiants': total_etudiants,
        'total_formations': total_formations,
        'total_absences': total_absences,
        'notifications_non_lues': notifications_non_lues,
    }
    return render(request, 'etudiants/accueil.html', context)

# CRUD Étudiants
def liste_etudiants(request):
    etudiants = Etudiant.objects.all().order_by('-date_inscription')
    paginator = Paginator(etudiants, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'etudiants/liste_etudiants.html', {'page_obj': page_obj})

def ajouter_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Student added successfully!'))
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'etudiants/ajouter_etudiant.html', {'form': form})

def modifier_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            messages.success(request, _('Student updated successfully!'))
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'etudiants/modifier_etudiant.html', {'form': form, 'etudiant': etudiant})

def supprimer_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        etudiant.delete()
        messages.success(request, _('Student deleted successfully!'))
        return redirect('liste_etudiants')
    return render(request, 'etudiants/supprimer_etudiant.html', {'etudiant': etudiant})

def detail_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    absences = etudiant.absences.all()
    notifications = etudiant.notifications.all()[:10]
    return render(request, 'etudiants/detail_etudiant.html', {
        'etudiant': etudiant,
        'absences': absences,
        'notifications': notifications
    })

# Gestion des formations
def liste_formations(request):
    formations = Formation.objects.all()
    return render(request, 'etudiants/liste_formations.html', {'formations': formations})

# Gestion des absences
def liste_absences(request):
    absences = Absence.objects.all()
    return render(request, 'etudiants/liste_absences.html', {'absences': absences})

def ajouter_absence(request):
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Absence recorded successfully!'))
            return redirect('liste_absences')
    else:
        form = AbsenceForm()
    return render(request, 'etudiants/ajouter_absence.html', {'form': form})

# Gestion des notifications
def liste_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'etudiants/liste_notifications.html', {'notifications': notifications})

def envoyer_notification_view(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            etudiant = form.cleaned_data['etudiant']
            canal = form.cleaned_data['canal']
            message = form.cleaned_data['message']
            envoyer_notification(etudiant, message, canal)
            messages.success(request, _('Notification sent via %(canal)s!') % {'canal': canal})
            return redirect('liste_notifications')
    else:
        form = NotificationForm()
    return render(request, 'etudiants/envoyer_notification.html', {'form': form})

def marquer_lue(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    notification.lue = True
    notification.save()
    return redirect('liste_notifications')

def supprimer_notification(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    notification.delete()
    return redirect('liste_notifications')