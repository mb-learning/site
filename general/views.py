from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from optin.views import EmailOptinView, TrialOptinView

class HomeView(TemplateView, EmailOptinView, TrialOptinView):
	template_name = 'general/home.htm'

	def __init__(self, **kwargs):
		print("Init HomeView")



	def get_context_data(self, request, **kwargs):
		# Call the base implementation first to get a context
		context = super(TemplateView, self).get_context_data(request, **kwargs)
		print("1.0context: ", context)

		context.update(super(EmailOptinView, self).get_context_data(request, **kwargs))
		print("1.1context: ", context)
		context.update(super(TrialOptinView, self).get_context_data( **kwargs))

		# context = super(TrialOptinView, self).get_context_data( **kwargs)
		print("context: ", context)
		context['test'] = "form" 
		print("context: ", context)

		return context




	def get(self, request, *args, **kwargs):


		context = self.get_context_data(request)
		return render(request, self.template_name, context)
