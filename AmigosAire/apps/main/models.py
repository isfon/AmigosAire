from django.db import models

class DatosGenerales(models.Model):

	logo = models.ImageField(upload_to="logo",null=True,blank=True)
	nombre_empresa = models.CharField(max_length=50)
	telefono_1 = models.CharField(max_length=50,null=True,blank=True)
	telefono_2 = models.CharField(max_length=50,null=True,blank=True)
	domicilio = models.CharField(max_length=100,null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
	video = models.URLField(null=True,blank=True,help_text='El formato es el siguiente "https://www.youtube.com/embed/Cu4UsFqz6Q8"')
	facebook = models.URLField(null=True,blank=True)
	twitter = models.URLField(null=True,blank=True)
	instagram = models.URLField(null=True,blank=True)
	fondo = models.ImageField(upload_to="fondo",null=True,blank=True,help_text='Esta imagen es la de fondo donde esta el menú')
	privacidad = models.TextField(null=True,blank=True)
	preguntas = models.TextField(null=True,blank=True)

	class Meta:
		verbose_name = "Datos Generales"
		verbose_name_plural = "Datos Generales"


	def __str__(self):
		return '%s'%self.nombre_empresa

class Carrusel(models.Model):

	titulo = models.CharField(max_length=50,null=True,blank=True)
	imagen = models.ImageField(upload_to="carrusel")

	class Meta:
		verbose_name = "Imagenes Carrusel"
		verbose_name_plural = "Imagenes Carrusel"

	def __str__(self):
		return '%s'%self.titulo


class Galeria(models.Model):

	titulo = models.CharField(max_length=50,null=True,blank=True)
	imagen = models.ImageField(upload_to="galleria")

	class Meta:
		verbose_name = "Imagenes Galeria"
		verbose_name_plural = "Imagenes Galeria"

	def __str__(self):
		return '%s'%self.titulo

class Servicios(models.Model):

	titulo = models.CharField(max_length=70)
	slug = models.CharField(max_length=70,null=True,blank=True)
	descripcion = models.TextField()
	incluye = models.TextField()
	precio = models.TextField()
	imagen_1 = models.ImageField(upload_to="servicios",help_text='Esta imagen es la que se mostrará en la pagina de inicio')
	imagen_2 = models.ImageField(upload_to="servicios")
	imagen_3 = models.ImageField(upload_to="servicios")

	class Meta:
		verbose_name = "Servicios y Precios"
		verbose_name_plural = "Servicios y Precios"

	def __str__(self):
		return '%s'%self.titulo

class Mensajes(models.Model):

	nombre = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)
	email = models.EmailField()
	mensaje = models.TextField()

	class Meta:
		verbose_name = "Mensajes"
		verbose_name_plural = "Mensajes"

	def __str__(self):
		return '%s'%self.nombre