from django.urls import path
from apps.users.api.api import *
urlpatterns = [
    path('usuarios/', user_api_view, name= 'usuarios_api'),
    path('usuarios/<int:pk>/', user_detalles_view, name= 'usuarios_api_detalle')
    
]