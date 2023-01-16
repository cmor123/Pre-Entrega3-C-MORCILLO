# Create your views here.
from django.shortcuts import render, HttpResponse 
from django.http import HttpResponse
from AppEntrega3.models import Hospedaje, Destino, Alquiler_Coches

          # Create your views here.

def iniciar(request):
      return render(
            request = request,
            template_name='AppEntrega3/bienvenido.html',
      )

def destinos(request):
      destino = destino(pais="Argentina", ciudad="Santa Fe")
      destino.save()
      documentoDeTexto = f"--->Pais: {destino.pais}   Ciudad: {destino.ciudad}"
      

      return HttpResponse(documentoDeTexto)

def hospedajes(request):

      hospedaje = hospedaje(Hoteles="Hoteles", Zona="Centro", Personas=" 4 adultos" )
      hospedaje.save()
      documentoDeTexto = f"--->Hoteles: {hospedaje.Hoteles}   Zona: {hospedaje.Zona} Personas: {hospedaje.Personas}"

      return HttpResponse(documentoDeTexto)

def alquiler_coche(request):

      alquiler_coches = alquiler_coches(Alta_Gama="Toyota Corolla", Media_Gama="Siena", Compacto="Fiat up" )
      alquiler_coches.save()
      documentoDeTexto = f"--->Alta_Gama: {alquiler_coches.Alta_Gama}   Meia_Gama: {alquiler_coches.Media_Gama} Compacto: {alquiler_coches.Compacto}"

      return HttpResponse(documentoDeTexto)

def inicio(request):

      return render(request, "AppEntrega3/inicio.html")

def destino(request):

      return render(request, "AppEntrega3/destino.html")

def hospedaje(request):

      return render(request, "AppEntrega3/hospedaje.html")


def alquiler_coches(request):

      return render(request, "AppEntrega3/alquiler_coches.html")


from AppEntrega3.forms import Alquiler_CochesFormulario, DestinoFormulario, HospedajeFormulario

def destinoFormulario(request):

      if request.method == "POST":

            miFormulario = DestinoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  destino = Destino(pais=informacion["pais"], ciudad=informacion["ciudad"])
                  destino.save()
                  return render(request, "AppEntrega3/inicio.html")
      else:
            miFormulario = DestinoFormulario()

      return render(request, "AppEntrega3/destinoFormulario.html", {"miFormulario": miFormulario})

def hospedajeFormulario(request):

      if request.method == "POST":

            miFormulario = HospedajeFormulario(request.POST) # Aqui me llega la informacion del html
            
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                 
                  hospedaje = Hospedaje(Hoteles=informacion["hoteles"], Apartamentos=informacion["apartamentos"], Casas=informacion["Casas"] )
                 
                  hospedaje.save()
                 
                  return render(request, "AppEntrega3/inicio.html")
      else:
            miFormulario = HospedajeFormulario()

      return render(request, "AppEntrega3/hospedajeFormulario.html", {"miFormulario": miFormulario})

def alquiler_cochesFormulario(request):

      if request.method == "POST":

            miFormulario = alquiler_cochesFormulario(request.POST) # Aqui me llega la informacion del html
            
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                 
                  Alquiler_Coches = Alquiler_CochesFormulario(Alta_Gama=informacion["alta gama"], Media_Gama=informacion["media gama"], Compactos=informacion["compactos"])
                 
                  Alquiler_Coches.save()
                 
                  return render(request, "AppEntrega3/inicio.html")
      else:
            miFormulario = Alquiler_CochesFormulario()

      return render(request, "AppEntrega3/alquiler_cochesFormulario.html", {"miFormulario": miFormulario})


def busquedaCiudad(request):
      return render(request, "AppEntrega3/busquedaCiudad.html")

def buscar(request):
     
      respuesta = f"Estoy buscando la Ciudad: {request.GET['ciudad']}"

      #No olvidar from django.http import HttpResponsereturn HttpResponse(respuesta)
      
      return HttpResponse(respuesta)
