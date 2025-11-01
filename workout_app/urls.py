from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('grupo/<int:pk>/', views.GrupoMuscularDetailView.as_view(), name='grupo_muscular_detalle'),
    path('ejercicio/nuevo/', views.EjercicioCreateView.as_view(), name='ejercicio_nuevo'),
    path('ejercicio/<int:pk>/editar/', views.EjercicioUpdateView.as_view(), name='ejercicio_editar'),
    path('ejercicio/<int:pk>/eliminar/', views.EjercicioDeleteView.as_view(), name='ejercicio_eliminar'),
]