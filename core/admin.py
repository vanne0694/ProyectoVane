from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Store)
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Product)