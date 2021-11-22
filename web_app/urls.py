from django.urls import path

from web_app import views

urlpatterns = [
    path('', views.home, name = "Home"),
    path('tienda', views.tienda, name = "Tienda"),
    path('blog', views.blog, name = "Blog"),
    path('contacto', views.contacto, name = "Contacto"),

]