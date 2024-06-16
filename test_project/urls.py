from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/')

def redirect_to_explorer(request):
    return HttpResponseRedirect('/explorer/')

def redirect_to_current_page(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def redirect_to_logout_page(request):
    return HttpResponseRedirect('/admin/logout/')

urlpatterns = [
    path("explorer/", include("explorer.urls")),
    path('', redirect_to_explorer),
    path('accounts/profile/', redirect_to_current_page),
    path("admin/", admin.site.urls),
    path('logout/', logout_view, name='logout')
]

admin.autodiscover()

urlpatterns += staticfiles_urlpatterns()
