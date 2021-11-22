"""David_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from web_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # ENLAZAMOS LAS URLS DE LA WEB_APP
    path('servicios', include('servicios.urls')),
    path('blog', include('blog.urls')),

    path('', include('web_app.urls')),

]

# CONFIGURAMOS LA PATH PARA QUE CUANDO BUSQUE UNA IMAGEN EN EL ADMINISTRADOR NOS LA MUESTRE
urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
