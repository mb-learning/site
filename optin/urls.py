from django.urls import path

from .views import (
	EmailValidationView,
	EmailOptinView,
	# TrialOptinView,
)

urlpatterns = [
	path('validation/new/email/', EmailValidationView.as_view()),
	path('validation/email/', EmailOptinView.as_view()),
	# path('validation/trial/', TrialOptinView.as_view()),

]


