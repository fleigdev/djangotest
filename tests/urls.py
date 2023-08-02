from django.urls import path
from . import views

urlpatterns = [
    path('create/producto/', views.create_producto, name='create_producto'),
    path('create/empleado/', views.create_empleado, name='create_empleado'),
    path('create/cliente/', views.create_cliente, name='create_cliente'),
    path('list/productos/', views.list_productos, name='list_productos'),
    path('list/empleados/', views.list_empleados, name='list_empleados'),
    path('list/clientes/', views.list_clientes, name='list_clientes'),
]