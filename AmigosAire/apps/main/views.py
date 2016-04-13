from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import(
	DatosGenerales,
	Carrusel,
	Galeria,
	Servicios,
	Mensajes
	)

class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['datos'] = DatosGenerales.objects.all()[:1].get()
        context['carrusel'] = Carrusel.objects.all()[:4]
        context['galeria'] = Galeria.objects.all()[:10]
        return context

    def post(self, request, *args, **kwargs):
    	if "btn-mensaje" in request.POST:
    		x = Mensajes()
    		x.nombre = request.POST['nombre']
    		x.telefono = request.POST['telefono']
    		x.email = request.POST['email']
    		x.mensaje = request.POST['mensaje']
    		x.save()
    		mensaje = 'Tu información fué enviada con exito, pronto nos pondremos en contacto con usted.'
    		datos = DatosGenerales.objects.all()[:1].get()
    		carrusel = Carrusel.objects.all()[:4]
    		galeria = Galeria.objects.all()[:10]
    		servicios = Servicios.objects.all()
    		ctx = {
	        	'datos':datos,
	        	'carrusel':carrusel,
	        	'galeria':galeria,
	        	'servicios':servicios,
	        	'mensaje':mensaje,
	        }
    		return render(request, 'index.html',ctx)

class PlanesView(TemplateView):

    template_name = "planes.html"

    def get_context_data(self, **kwargs):
        context = super(PlanesView, self).get_context_data(**kwargs)
        context['datos'] = DatosGenerales.objects.all()[:1].get()
        context['servicios'] = Servicios.objects.all()
        return context

class PlanDetailView(DetailView):

    model = Servicios
    slug_field = 'slug'
    template_name = "plan.html"
    context_object_name = 'plan'

    def get_context_data(self, **kwargs):
        context = super(PlanDetailView, self).get_context_data(**kwargs)
        context['datos'] = DatosGenerales.objects.all()[:1].get()
        return context

class PrivacidadView(TemplateView):

    template_name = "privacidad.html"

    def get_context_data(self, **kwargs):
        context = super(PrivacidadView, self).get_context_data(**kwargs)
        context['datos'] = DatosGenerales.objects.all()[:1].get()
        return context

class PreguntasView(TemplateView):
	
    template_name = "preguntas.html"

    def get_context_data(self, **kwargs):
        context = super(PreguntasView, self).get_context_data(**kwargs)
        context['datos'] = DatosGenerales.objects.all()[:1].get()
        return context