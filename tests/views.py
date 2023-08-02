from django.shortcuts import render, redirect
from .models import Producto, Empleado, Cliente
from .forms import ProductoForm, EmpleadoForm, ClienteForm

def create_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_productos')
    else:
        form = ProductoForm()
    return render(request, 'tests/partials/create_form.html', {'form': form, 'model_name': 'Producto'})

def create_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'tests/partials/create_form.html', {'form': form, 'model_name': 'Empleado'})

def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_clientes')
    else:
        form = ClienteForm()
    return render(request, 'tests/partials/create_form.html', {'form': form, 'model_name': 'Cliente'})

def list_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tests/partials/list_objects.html', {'objects': productos, 'model_name': 'Producto'})

def list_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'tests/partials/list_objects.html', {'objects': empleados, 'model_name': 'Empleado'})

def list_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'tests/partials/list_objects.html', {'objects': clientes, 'model_name': 'Cliente'})
