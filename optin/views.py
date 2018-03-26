from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import FormView

from validate_email import validate_email

from .forms import EmailOptinForm, TrialOptinForm



class EmailValidationView(View):
	email_address = None

	def __init__(self, **kwargs):
		self.email_address = request.POST.get('email_address', None)
		return

	def post(self, request, *args, **kwargs):
		if self.email_address:
			is_valid = validate_email(self.email_address,verify=True)

		if not is_valid:
			is_valid = False		

		data = {
				'is_valid': is_valid,
		}
		return JsonResponse(data)





class EmailOptinView(FormView):
	form_class = EmailOptinForm
	email_optin_form = None

	def __init__(self, **kwargs):
		print("here")
		self.email_optin_form = None
		pass

	def get_context_data(self, request, **kwargs):
		# Call the base implementation first to get a context
		print("1HERE: ")
		context = {}#super(FormView, self).get_context_data(**kwargs)
		self.email_optin_form = EmailOptinForm()
		print("self.email_optin_form: ", self.email_optin_form)
		self.email_optin_form.prefix = 'email_optin_form'

		context['email_optin_form'] = self.email_optin_form

		print("1context: ", context)
		return context

	def get(self, request, *args, **kwargs):

		

		self.email_optin_form.prefix = 'email_optin_form'
		context = self.get_context_data(request)
		return self.render_to_response(self.context)

	def post(self, request, *args, **kwargs):
		self.email_optin_form = EmailOptinForm(self.request.POST, prefix='email_optin_form ')

		if  self.email_optin_form.is_valid():
			return HttpResponseRedirect("google.com")
		else:
			self.email_optin_form.prefix='email_optin_form'
			context = self.get_context_data(request)
			return self.render_to_response(context)





class TrialOptinView(FormView):
	form_class = TrialOptinForm
	trial_optin_form = None

	def __init__(self, **kwargs):
		print("here")
		self.trial_optin_form = None
		pass

	def get_context_data(self, request, **kwargs):
		# Call the base implementation first to get a context
		print("2HERE: ")
		context = {}#super(FormView, self).get_context_data(**kwargs)
		
		self.trial_optin_form = TrialOptinForm()
		print("self.trial_optin_form: ", self.trial_optin_form)
		self.trial_optin_form.prefix = 'trial_optin_form'
		context['trial_optin_form'] = self.trial_optin_form

		print("2context: ", context)
		return context

	def get(self, request, *args, **kwargs):
		self.trial_optin_form = TrialOptinForm()
		print("self.trial_optin_form: ", self.trial_optin_form)
		self.trial_optin_form.prefix = 'trial_optin_form'
		context = self.get_context_data(request)
		return self.render_to_response(self.context)

	def post(self, request, *args, **kwargs):
		self.trial_optin_form = TrialOptinForm(self.request.POST, prefix='trial_optin_form ')

		if  self.trial_optin_form.is_valid():
			return HttpResponseRedirect("google.com")
		else:
			self.trial_optin_form.prefix='trial_optin_form'
			context = self.get_context_data(request)
			return self.render_to_response(context)


	
# class HomeOptinView(FormView):
#     def get(self, request, *args, **kwargs):
#         contact_form = ContactForm()
#         contact_form.prefix = 'contact_form'
#         social_form = SocialForm()
#         social_form.prefix = 'social_form'
#         return self.render_to_response(self.get_context_data('contact_form':contact_form, 'social_form':social_form ))

#     def post(self, request, *args, **kwargs):
#         contact_form = ContactForm(self.request.POST, prefix='contact_form')
#         social_form = SocialForm(self.request.POST, prefix='social_form ')

#         if contact_form.is_valid() and social_form.is_valid():
#             ### do something
#             return HttpResponseRedirect(>>> redirect url <<<)
#         else:
#             return self.form_invalid(contact_form,social_form , **kwargs)


#     def form_invalid(self, contact_form, social_form, **kwargs):
#         contact_form.prefix='contact_form'
#         social_form.prefix='social_form'
#                 return self.render_to_response(self.get_context_data('contact_form':contact_form, 'social_form':social_form ))








