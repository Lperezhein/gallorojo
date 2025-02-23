from django.contrib import admin
from .models import Noticia, Evento
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.urls import reverse
from django.utils.html import format_html

class NoticiaAdminForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'descripcion': CKEditorWidget(),
            'contenido': CKEditorWidget(),
        }

class NoticiaAdmin(admin.ModelAdmin):
    form = NoticiaAdminForm

admin.site.register(Noticia, NoticiaAdmin)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'descripcion', 'enlace_detalle')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha',)

    def enlace_detalle(self, obj):
        url = reverse('detalle_evento', args=[obj.id])
        return format_html('<a href="{}">Ver detalles</a>', url)
    enlace_detalle.short_description = 'Detalles'