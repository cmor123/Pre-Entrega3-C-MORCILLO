
from AppEntrega3 import views
 
from django.urls import path

urlpatterns = [
    
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('destino', views.destino, name="Destino"),
    path('hospedaje', views.hospedaje, name="Hospedaje"),
    path('alquiler-coches', views.alquiler_coches, name="Alquiler_Coches"),
    path('alquiler-cochesFormulario', views.alquiler_cochesFormulario, name="Alquiler_CochesFormulario"),
    path('destinoFormulario', views.destinoFormulario, name="DestinoFormulario"),
    path('hospedajeFormulario', views.hospedajeFormulario, name="HospedajeFormulario"),
    path('busquedaCiudad', views.busquedaCiudad, name="BusquedaCiudad"),
    path('buscar/', views.buscar)
 ]
