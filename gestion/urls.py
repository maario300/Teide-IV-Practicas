from django.urls import path
from . import views  # Aquí SÍ funcionará porque views.py está en esta misma carpeta

urlpatterns = [
# Cambia la línea 5 de tu archivo gestion/urls.py
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('administrador/', views.admin_dashboard, name='admin_dashboard'),
    path('profesor/', views.profesor_dashboard, name='profesor_dashboard'),
    path('api/get-datos-fct/', views.get_datos_fct, name='get_datos_fct'),
]