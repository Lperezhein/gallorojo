from django.shortcuts import render, get_object_or_404
from .models import Noticia, Evento
from datetime import date

def home(request):
    """
    Vista para la página de inicio.
    Muestra las últimas noticias y los eventos próximos.
    """
    # Obtener las últimas 6 noticias ordenadas por fecha de publicación (más recientes primero)
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')[:6]

    # Obtener los próximos 3 eventos ordenados por fecha (más cercanos primero)
    eventos_proximos = Evento.objects.filter(fecha__gte=date.today()).order_by('fecha')[:3]

    # Contexto para pasar datos al template
    contexto = {
        'noticias': noticias,
        'fecha_actual': date.today(),
        'eventos_proximos': eventos_proximos,
    }
    return render(request, 'core/home.html', contexto)

def about(request):
    """
    Vista para la página "Acerca de".
    """
    return render(request, 'core/about.html')

def contact(request):
    """
    Vista para la página de contacto.
    """
    return render(request, 'core/contact.html')

def noticia_detalle(request, pk):
    """
    Vista para mostrar el detalle de una noticia.
    """
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'core/noticia_detalle.html', {'noticia': noticia})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    contexto = {
        'evento': evento,
        'fecha_actual': date.today(),  # Pasar la fecha actual
    }
    return render(request, 'evento/detalle_evento.html', contexto)