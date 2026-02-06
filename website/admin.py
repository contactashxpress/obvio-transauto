from django.contrib import admin
from django.utils.html import format_html
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Configuration de l'interface admin pour les messages de contact."""
    
    list_display = [
        'name', 
        'email', 
        'phone', 
        'vehicle_type_display', 
        'status_badge', 
        'created_at'
    ]
    list_filter = ['status', 'vehicle_type', 'created_at']
    search_fields = ['name', 'email', 'phone', 'country', 'message']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 25
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Informations du Contact', {
            'fields': ('name', 'email', 'phone', 'country')
        }),
        ('Détails de la Demande', {
            'fields': ('vehicle_type', 'message')
        }),
        ('Gestion', {
            'fields': ('status', 'notes')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def vehicle_type_display(self, obj):
        """Affiche le type de véhicule avec une icône."""
        icons = {
            'tout-terrain': '🚙',
            'poids-lourd': '🚛',
            'engin-btp': '🚜',
            'autre': '📋',
        }
        icon = icons.get(obj.vehicle_type, '📋')
        return f"{icon} {obj.get_vehicle_type_display()}"
    vehicle_type_display.short_description = "Type de véhicule"
    
    def status_badge(self, obj):
        """Affiche le statut avec un badge coloré."""
        colors = {
            'new': '#E31B23',        # Rouge - Nouveau
            'read': '#3B82F6',       # Bleu - Lu
            'in_progress': '#F59E0B', # Orange - En cours
            'replied': '#10B981',    # Vert - Répondu
            'closed': '#6B7280',     # Gris - Clôturé
        }
        color = colors.get(obj.status, '#6B7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; '
            'border-radius: 3px; font-size: 11px; font-weight: bold;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_badge.short_description = "Statut"
    
    def get_queryset(self, request):
        """Optimise les requêtes."""
        return super().get_queryset(request)
    
    # Actions personnalisées
    actions = ['mark_as_read', 'mark_as_replied', 'mark_as_closed']
    
    @admin.action(description="Marquer comme lu")
    def mark_as_read(self, request, queryset):
        updated = queryset.update(status='read')
        self.message_user(request, f"{updated} message(s) marqué(s) comme lu(s).")
    
    @admin.action(description="Marquer comme répondu")
    def mark_as_replied(self, request, queryset):
        updated = queryset.update(status='replied')
        self.message_user(request, f"{updated} message(s) marqué(s) comme répondu(s).")
    
    @admin.action(description="Marquer comme clôturé")
    def mark_as_closed(self, request, queryset):
        updated = queryset.update(status='closed')
        self.message_user(request, f"{updated} message(s) clôturé(s).")
