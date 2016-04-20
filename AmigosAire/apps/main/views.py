from django.shortcuts import render, HttpResponse, render_to_response, RequestContext
import json
from django.views.generic import TemplateView, DetailView
from .models import(
	DatosGenerales,
	Carrusel,
	Galeria,
	Servicios,
	Mensajes,
        Promocion
	)
from .forms import MensajesForm

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['datos'] = DatosGenerales.objects.all()[:1].get()
        context['galeria'] = Galeria.objects.all()[:10]
        context['servicios'] = Servicios.objects.all()
        context['carrusel'] = Carrusel.objects.all()[:5]
        context['promociones'] = Promocion.objects.filter(publicar=True)
        context['form'] = MensajesForm()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if "btn-enviar" in request.POST:
            form = MensajesForm(request.POST)
            if form.is_valid():
                mensaje = Mensajes()
                mensaje.nombre = request.POST['nombre']
                mensaje.telefono = request.POST['telefono']
                mensaje.mensaje = request.POST['mensaje']
                mensaje.save()
                context['mensaje'] = '¡Su mensaje fué enviado exitosamente, pronto nos comunicaremos con usted gracias!'
            else:
                context['mensaje'] = 'Por favor llene todos los datos'
            return render_to_response('index.html',context, context_instance=RequestContext(request))


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

class GaleriaView(TemplateView):

    template_name = "galeria.html"

    def get_context_data(self, **kwargs):
        context = super(GaleriaView, self).get_context_data(**kwargs)
        context['datos'] = DatosGenerales.objects.all()[:1].get()
        context['galeria'] = Galeria.objects.all()[:10]
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

class ContactoView(TemplateView):

    template_name = "contacto.html"

    def get_context_data(self, **kwargs):
        context = super(ContactoView, self).get_context_data(**kwargs)
        context['datos'] = DatosGenerales.objects.all()[:1].get()
        return context

class EnviarMensaje(TemplateView):
    
    def get(self, request, *args, **kwargs):
        x = Mensajes()
        aux = False
        if request.GET['nombre']:
            x.nombre = request.GET['nombre']
            aux = True
            mensaje = 'Tu información fué enviada con exito, pronto nos pondremos en contacto con usted.'
        else:
            mensaje = 'Por Favor llena todos los datos'
            aux = False
        if request.GET['telefono']:
            x.telefono = request.GET['telefono']
            aux = True
            mensaje = 'Tu información fué enviada con exito, pronto nos pondremos en contacto con usted.'
        else:
            mensaje = 'Por Favor llena todos los datos'
            aux = False
        if request.GET['correo']:
            x.email = request.GET['correo']
            aux = True
            mensaje = 'Tu información fué enviada con exito, pronto nos pondremos en contacto con usted.'
        else:
            mensaje = 'Por Favor llena todos los datos'
            aux = False
        if request.GET['mensaje']:
            x.mensaje = request.GET['mensaje']
            aux = True
            mensaje = 'Tu información fué enviada con exito, pronto nos pondremos en contacto con usted.'
        else:
            mensaje = 'Por Favor llena todos los datos'
            aux = False
        if aux:
            x.save()
        ctx = {
            'mensaje':mensaje,
        }
        return HttpResponse(json.dumps(ctx), content_type='application/json')
