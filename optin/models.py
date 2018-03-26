


from django.db import models

class EmailOptin(models.Model):
	email_address = models.CharField(max_length=100, blank=True, null=True)


class TrialOptin(models.Model):
	email_address		= models.ForeignKey(EmailOptin, null=True, blank=True)
	parent_first_name 	= models.CharField(max_length=100, blank=True, null=True)
	parent_last_name 	= models.CharField(max_length=100, blank=True, null=True)
	parent_last_name 	= models.CharField(max_length=100, blank=True, null=True)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

	child_first_name	= models.CharField(max_length=100, blank=True, null=True)
	# trial_time 			= models.DateTimeField(auto_now=False, auto_now_add=True)

	created 			= models.DateTimeField(auto_now=False, auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True, auto_now_add=False)
