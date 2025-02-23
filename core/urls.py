from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # Ruta para 'about'.
    path('contact/', views.contact, name='contact'),
    path('noticia/<int:pk>/', views.noticia_detalle, name='noticia_detalle'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
]
