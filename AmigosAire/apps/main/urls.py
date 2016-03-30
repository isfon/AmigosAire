from django.conf.urls import url, include
from .views import(
	IndexView,
	PlanView,
	)

urlpatterns = [   
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^plan/$', PlanView.as_view(), name='plan'),
]