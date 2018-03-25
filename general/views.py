from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'general/home.htm'
