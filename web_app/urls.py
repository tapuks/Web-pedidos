from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from web_app import views

urlpatterns = [
    path('', views.home, name = "Home"),
    path('tienda', views.tienda, name = "Tienda"),

]

# CONFIGURAMOS LA PATH PARA QUE CUANDO BUSQUE UNA IMAGEN EN EL ADMINISTRADOR NOS LA MUESTRE
urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)