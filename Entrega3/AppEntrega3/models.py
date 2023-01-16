from django.db import models

# Create your models here.

class Destino(models.Model):

    pais=models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)

    def __str__(self):
            return f"Nombre: {self.pais}, Ciudad {self.ciudad}"
   
class Hospedaje(models.Model):

    Hoteles= models.CharField(max_length=30)
    Zona= models.CharField(max_length=30)
    Personas= models.IntegerField()
    
    def __str__(self):
            return f"Hoteles: {self.Hoteles} - Zona: {self.Zona} - Casas: {self.Personas} "

class Alquiler_Coches(models.Model):
    Alta_Gama=models.CharField(max_length=30)
    Media_Gama= models.CharField(max_length=30)
    Compacto= models.CharField(max_length=30)
    
    def __str__(self):
            return f"Alta_Gama: {self.Alta_Gama} - Media_Gama {self.Media_Gama} - Compacto {self.Compacto} "
   

   