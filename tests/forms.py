from django import forms
from .models import Producto, Empleado, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['created_at', 'updated_at']
        fields = ['name', 'description', 'price', 'category', 'stock', 'is_available']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        exclude = ['created_at', 'updated_at']
        fields = ['name', 'position', 'department', 'hire_date', 'salary', 'is_active', 'address', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['created_at', 'updated_at']
        fields = ['name', 'email', 'phone_number', 'address', 'company', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})