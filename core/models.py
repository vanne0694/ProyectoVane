from django.db import models
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.







# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='Nombre (s)')
    lastname = models.CharField(max_length=50, verbose_name='Apellidos')
    birthday = models.DateField(verbose_name='Fecha de nacimiento')
    height = models.DecimalField(verbose_name='Estatura (en metros)', max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return "Persona: {0} {1}".format(self.firstname, self.lastname)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


STORETYPE = [('Abarrotes', 'Abarrotes'), ('Autoservicio', 'Autoservicio')]


class Store(models.Model):
    name = models.CharField(verbose_name='Tienda', max_length=100)
    type = models.CharField(choices=STORETYPE, verbose_name='Tipo de tienda', max_length=15, default='Autoservicio')

    def __str__(self):
        return "{0} {1}".format(self.type, self.name)

    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"


CLIENTTYPE = [('Distinguido', 'Distinguido'), ('Miembro', 'Miembro')]


class Client(models.Model):
    Person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Persona")
    Store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name="Tienda")
    type = models.CharField(choices=CLIENTTYPE, verbose_name='Tipo de cliente', max_length=30)
    member = models.BooleanField(default=False, verbose_name='¿Es mienbro?')

    def __str__(self):
        return "{0}".format(self.type)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Category(models.Model):
    name = models.CharField(verbose_name='Categoria', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural= 'Categorias'





class Product(models.Model):
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Seleccione la categoria del producto')
    name = models.CharField(verbose_name='Producto', max_length=100, unique=True)
    description = models.TextField(verbose_name='Descripción del producto', max_length=600)
    price = models.DecimalField(verbose_name='Precio', max_digits=8, decimal_places=2, default=0.00)
    foto = models.ImageField(verbose_name='Agregar imagen', null=True, upload_to='imgProducts')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'

