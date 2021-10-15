from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(verbose_name='Nombre del producto', max_length=100, unique=True)
    description = models.TextField(verbose_name='Descrionción del producto', max_length=1000)
    foto = models.ImageField(verbose_name='Seleccione una imagen', upload_to='inventario', null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name= 'Producto a inventariar'
        verbose_name_plural= 'Productos a inventriar'




class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Seleccione el producto')
    fechaIngreso = models.DateTimeField(verbose_name='Fecha y hora de ingreso')
    perecedero = models.BooleanField(verbose_name='¿Es perecedero?', default=False)

    def __str__(self):
        return 'Producto {0}, se ingreso el {1}'.format(self.producto, self.fechaIngreso)

    class Meta:
        verbose_name= 'Inventario'
        verbose_name_plural= 'Inventarios'