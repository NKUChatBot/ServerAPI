"""ServerAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView, TemplateView

from .views import ask, greet
from . import settings

favicon_view = RedirectView.as_view(url='/media/favicon.ico', permanent=True)

urlpatterns = \
    [
        path('favicon.ico', favicon_view),
        path('ask/', ask),
        path('greet/', greet),

        path('teacher_msg/', include("TeacherMsg.urls")),
        path('fixed_conv/', include("FixedConv.urls")),
        path('nlp_component/', include("NlpComponent.urls")),
        path('third_party/', include('ThridParty.urls')),

        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
