from django.contrib import admin
from .models import(
	DatosGenerales,
	Carrusel,
	Galeria,
	Servicios,
	Mensajes
	)

class DatosAdmin(admin.ModelAdmin):

	list_display =('nombre_empresa',)

	fieldsets = (
		('Datos Generales', {'fields': ('nombre_empresa','logo','telefono_1','telefono_2','domicilio','email','video',
			'facebook','twitter','instagram','fondo')}),
		('Aviso Privacidad', {'fields': ('privacidad',)}),
        ('Preguntas Frecuentes', {'fields': ('preguntas',)}),
    )

	class Media:
		js =('js/tiny_mce/tinymce.min.js','js/basic_config.js')

class ServiciosAdmin(admin.ModelAdmin):

	prepopulated_fields ={"slug":("titulo",)}
	list_display =('titulo','descripcion')

	fieldsets = (
        ('titulo', {'fields': ('titulo', 'slug')}),
        ('descripcion', {'fields': ('descripcion',)}),
        ('incluye', {'fields': ('incluye',)}),
        ('precio', {'fields': ('precio',)}),
        ('imagenes', {'fields': ('imagen_1', 'imagen_2', 'imagen_3')}),
    )

	class Media:
		js =('js/tiny_mce/tinymce.min.js','js/basic_config.js')

class MensajesAdmin(admin.ModelAdmin):

	list_display =('nombre','telefono', 'email', 'mensaje')

admin.site.register(DatosGenerales,DatosAdmin)
admin.site.register(Carrusel)
admin.site.register(Galeria)
admin.site.register(Servicios,ServiciosAdmin)
admin.site.register(Mensajes,MensajesAdmin)