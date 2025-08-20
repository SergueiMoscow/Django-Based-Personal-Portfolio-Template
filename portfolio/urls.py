from django.conf.urls.static import static
from django.urls import path

from portfolio_site import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='home'), 
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('certificates/', views.certificates, name='certificates'),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
