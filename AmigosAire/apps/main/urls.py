from django.conf.urls import url, include
from .views import(
	IndexView,
	PlanDetailView,
	PreguntasView,
	PrivacidadView,
	PlanesView,
	)

urlpatterns = [   
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^faq/$', PreguntasView.as_view(), name='faq'),
	url(r'^privacidad/$', PrivacidadView.as_view(), name='privacidad'),
	url(r'^planes/$', PlanesView.as_view(), name='planes'),
	url(r'^plan/(?P<slug>.*)/$', PlanDetailView.as_view(), name='plan_detalle'),
]