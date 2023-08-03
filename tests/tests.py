from django.test import TestCase
from .models import Producto, Empleado, Cliente

class MyappTests(TestCase):
    def test_create_producto(self):
        producto = Producto.objects.create(
            name="Product 1",
            description="Producto 1 descripcion",
            price=19.99,
            category="Electronicos",
            stock=100,
            is_available=True
        )
        self.assertEqual(Producto.objects.count(), 1)

    def test_create_empleado(self):
        empleado = Empleado.objects.create(
            name="Jose Perez",
            position="Jefe de Operacion",
            department="Operations",
            hire_date="2023-07-18",
            salary=50000.00,
            is_active=True,
            address="123 Av Beni",
            phone_number="555-123-4567"
        )
        self.assertEqual(Empleado.objects.count(), 1)

    def test_create_cliente(self):
        cliente = Cliente.objects.create(
            name="Sergio Suarez",
            email="sergio@suarez.com",
            phone_number="555-987-6543",
            address="456 Oaker Ave",
            company="ABC Compania",
            is_active=True
        )
        self.assertEqual(Cliente.objects.count(), 1)




