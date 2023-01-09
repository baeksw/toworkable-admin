from django.urls import path
from django.views.generic.base import RedirectView

from .views import index


urlpatterns = [
#    path('', index, name='index'),
    path('', RedirectView.as_view(url='admin', permanent=False), name='index'), 
]
