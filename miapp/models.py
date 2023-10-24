from django.db import models


class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="logos",null=True)

    def __str__(self) -> str:
        return self.nombre
    
class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo= models.CharField(max_length=30)
    detalle = models.CharField(max_length=100)
    detalle_corto = models.CharField(max_length=30)
    tipos=[
        ('S','Suspernsión de actividades'),
        ('C','Suspensión de clase'),
        ('I','Información')
    ]
    tipo=models.CharField(max_length=1,choices=tipos,default='I')
    entidad= models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible= models.BooleanField(default=True)
    fecha_publicacion=models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion=models.DateTimeField(auto_now=True)
    

    
    def __str__(self) -> str:
        return self.titulo

# Create your models here.