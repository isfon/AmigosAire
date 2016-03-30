from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class PlanView(TemplateView):
    template_name = "plan.html"