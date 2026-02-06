from django.db import models


class ContactMessage(models.Model):
    """Modèle pour stocker les messages du formulaire de contact."""
    
    VEHICLE_CHOICES = [
        ('tout-terrain', 'Véhicule Tout-Terrain'),
        ('poids-lourd', 'Poids Lourd / Camion'),
        ('engin-btp', 'Engin BTP / Chantier'),
        ('autre', 'Autre'),
    ]
    
    STATUS_CHOICES = [
        ('new', 'Nouveau'),
        ('read', 'Lu'),
        ('in_progress', 'En cours de traitement'),
        ('replied', 'Répondu'),
        ('closed', 'Clôturé'),
    ]
    
    # Informations du contact
    name = models.CharField(max_length=100, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=30, verbose_name="Téléphone")
    country = models.CharField(max_length=100, blank=True, verbose_name="Pays")
    
    # Détails de la demande
    vehicle_type = models.CharField(
        max_length=50, 
        choices=VEHICLE_CHOICES, 
        verbose_name="Type de véhicule"
    )
    message = models.TextField(verbose_name="Message")
    
    # Métadonnées
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='new',
        verbose_name="Statut"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de réception")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")
    notes = models.TextField(blank=True, verbose_name="Notes internes")
    
    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.get_vehicle_type_display()} ({self.created_at.strftime('%d/%m/%Y')})"
