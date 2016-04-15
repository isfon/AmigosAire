from django.conf.urls import url, include
from .views import(
	IndexView,
	PlanDetailView,
	PreguntasView,
	PrivacidadView,
	PlanesView,
	GaleriaView,
	ContactoView,
	EnviarMensaje
	)

urlpatterns = [   
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^faq/$', PreguntasView.as_view(), name='faq'),
	url(r'^privacidad/$', PrivacidadView.as_view(), name='privacidad'),
	url(r'^planes/$', PlanesView.as_view(), name='planes'),
	url(r'^galeria/$', GaleriaView.as_view(), name='galeria'),
	url(r'^contacto/$', ContactoView.as_view(), name='contacto'),
	url(r'^enviar/$', EnviarMensaje.as_view()),
	url(r'^plan/(?P<slug>.*)/$', PlanDetailView.as_view(), name='plan_detalle'),
]