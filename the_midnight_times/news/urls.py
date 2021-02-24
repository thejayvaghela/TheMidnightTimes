from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('home/',views.home_page),
    path('search/',views.search),
    # path('search_history/',views.search_history),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="signup.html")),
]
