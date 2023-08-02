from django.test import TestCase
from .models import Producto, Empleado, Cliente

class MyappTests(TestCase):
    def test_create_producto(self):
        producto = Producto.objects.create(name="Product 1", description="Producto 1 descripcion!!!")
        self.assertEqual(Producto.objects.count(), 1)

    def test_create_empleado(self):
        empleado = Empleado.objects.create(name="Jose Perez", position="Jefe de Operacion")
        self.assertEqual(Empleado.objects.count(), 1)

    def test_create_cliente(self):
        cliente = Cliente.objects.create(name="Sergio Suarez", email="sergio@suarez.com")
        self.assertEqual(Cliente.objects.count(), 1)
