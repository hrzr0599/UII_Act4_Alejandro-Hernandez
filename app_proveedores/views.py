from django.shortcuts import render

# Create your views here.

def index(request):
    proveedores = [
        {
            'nombre': 'Proveedor A',
            'contacto': 'info@proveedora.com',
            'telefono': '555-123-4567'
        },
        {
            'nombre': 'Proveedor B',
            'contacto': 'ventas@proveedorb.net',
            'telefono': '555-987-6543'
        },
        {
            'nombre': 'Proveedor C',
            'contacto': 'soporte@proveedorc.org',
            'telefono': '555-111-2222'
        }
    ]

    # El contexto que se enviará a la plantilla
    context = {
        'lista_proveedores': proveedores
    }

    # Renderiza la plantilla index.html con los datos de los proveedores
    return render(request, 'index.html', context)