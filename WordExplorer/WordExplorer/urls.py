﻿"""
Definition of urls for WordExplorer.
"""

from datetime import datetime
from django.conf.urls import patterns, url, include
from django.contrib import admin
from app.forms import BootstrapAuthenticationForm
from DictonaryBuilder.views import RegistrationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^', include('WordApp.urls', namespace='WordApp')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    #url(r'^login/$',
    #    'django.contrib.auth.views.login',
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title':'Log in',
    #            'year':datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    'django.contrib.auth.views.logout',
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'DictonaryBuilder.views.UserRegistration'),
    url(r'^login/$', 'DictonaryBuilder.views.LoginRequest', name = 'login'),
    url(r'^logout/$', 'DictonaryBuilder.views.LogoutRequest', name = 'logout'),
)
