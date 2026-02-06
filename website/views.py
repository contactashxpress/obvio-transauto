from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import ContactMessage


def home(request):
    """Page d'accueil avec showroom."""
    return render(request, 'website/index.html')


def services(request):
    """Page des services."""
    return render(request, 'website/services.html')


def about(request):
    """Page À propos."""
    return render(request, 'website/about.html')


def contact(request):
    """Page de contact avec formulaire."""
    context = {
        'form_submitted': False,
        'form_success': False,
        'form_errors': []
    }
    
    if request.method == 'POST':
        # Récupération des données du formulaire
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        country = request.POST.get('country', '').strip()
        vehicle_type = request.POST.get('vehicle_type', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Validation basique
        errors = []
        if not name:
            errors.append('Le nom est requis.')
        if not email:
            errors.append('L\'email est requis.')
        if not phone:
            errors.append('Le téléphone est requis.')
        if not vehicle_type:
            errors.append('Le type de véhicule est requis.')
        if not message:
            errors.append('Le message est requis.')
        
        if errors:
            context['form_submitted'] = True
            context['form_success'] = False
            context['form_errors'] = errors
        else:
            # Sauvegarde dans la base de données
            try:
                ContactMessage.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    country=country,
                    vehicle_type=vehicle_type,
                    message=message
                )
                context['form_submitted'] = True
                context['form_success'] = True
            except Exception as e:
                context['form_submitted'] = True
                context['form_success'] = False
                context['form_errors'] = ['Une erreur est survenue. Veuillez réessayer.']
    
    return render(request, 'website/contact.html', context)
