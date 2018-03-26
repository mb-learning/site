from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('general.urls') ),
	#, namespace='general'),

    # url(r'^/', include('general.urls', namespace='general')),
]
