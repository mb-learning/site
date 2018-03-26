from django import forms
from .models import EmailOptin, TrialOptin

class EmailOptinForm(forms.ModelForm):
	email_address = forms.EmailField(label='Email', max_length=254, widget=forms.TextInput(attrs={'autocomplete':'off',
																									'placeholder':"Parent's Email",
																									'aria-label':"Parent's Email",
																									'aria-describedby':'basic-addon2',
																									'id': 'id_parent_email',
																									'class':'form-control',
																								}))

	class Meta:
		model = EmailOptin
		fields = [
			"email_address",
		]



class TrialOptinForm(forms.ModelForm):
	email_address = forms.EmailField(label='Email', max_length=254, widget=forms.TextInput(attrs={'autocomplete':'off',
																									'placeholder':'Parent Email',
																									'id': 'id_parent_email',
																									'class':'formfields',
																								}))

	class Meta:
		model = TrialOptin
		fields = [
			"email_address",
		]
