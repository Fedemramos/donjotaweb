from django.contrib import admin
from .models import *
# Register your models here.

class Sandwicheadmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    search_fields = ('nombre','descripcion')
class Hamburguesaadmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    search_fields = ('nombre','descripcion')    
class Tapeoeadmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    search_fields = ('nombre','descripcion')    
 

class Bebidaadmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    search_fields = ('nombre','descripcion')  
class Tragoadmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    search_fields = ('nombre','descripcion') 


class Desayunoadmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    search_fields = ('nombre','descripcion')  
class Meriendadmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    search_fields = ('nombre','descripcion') 
class Brusquetadmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    search_fields = ('nombre','descripcion') 


class Caferiaadmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    search_fields = ('nombre','descripcion') 


class Ensaladaadmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    search_fields = ('nombre','descripcion') 

class Postreadmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio')
    search_fields = ('nombre','descripcion') 



admin.site.register(Sandwiches,Sandwicheadmin)
admin.site.register(Hamburguesas,Hamburguesaadmin)
admin.site.register(Tapeo,Tapeoeadmin)

admin.site.register(Merienda,Meriendadmin)
admin.site.register(Desayuno,Desayunoadmin)
admin.site.register(Brusquetas,Brusquetadmin)

admin.site.register(Bedidas,Bebidaadmin)
admin.site.register(Tragos,Tragoadmin)

admin.site.register(Cafeteria,Caferiaadmin)

admin.site.register(Ensaladas,Ensaladaadmin)

admin.site.register(Postres,Postreadmin)