from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import GrupoMuscular, Ejercicio

class HomeView(ListView):
    model = GrupoMuscular
    template_name = 'home.html'
    context_object_name = 'grupos_musculares'

class GrupoMuscularDetailView(DetailView):
    model = GrupoMuscular
    template_name = 'grupo_muscular_detalle.html'
    context_object_name = 'grupos_musculares'

class EjercicioCreateView(LoginRequiredMixin, CreateView):
    model = Ejercicio
    template_name = 'ejercicio_form.html'
    fields = ['nombre', 'descripcion', 'grupo_muscular', 'musculos_trabajados', 'imagen', 'imagen_url', 'orden']
    success_url = reverse_lazy('home')

class EjercicioUpdateView(LoginRequiredMixin, UpdateView):
    model = Ejercicio
    template_name = 'ejercicio_form.html'
    fields = ['nombre', 'descripcion', 'grupo_muscular', 'musculos_trabajados', 'imagen', 'imagen_url', 'orden']
    success_url = reverse_lazy('home')

class EjercicioDeleteView(LoginRequiredMixin, DeleteView):
    model = Ejercicio
    template_name = 'ejercicio_confirm_delete.html'
    success_url = reverse_lazy('home')
