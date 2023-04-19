from django.shortcuts import render
from CaffeApp.models import *
from .forms import *

def shop(request):
    if request.method == 'POST':
        
        miFormulario = ReservationForm(request.POST)
        
        if miFormulario.is_valid():

            data_formulario = miFormulario.cleaned_data

            inscripcion = Reservation(name=data_formulario['name'], 
                                      email=data_formulario['email'], 
                                      phone=data_formulario['phone'], 
                                      number_guests= data_formulario['number_guests'],
                                      date= data_formulario['date'], 
                                      time=data_formulario['time'],
                                      message=data_formulario['message']
                                      )
            inscripcion.save()
            return render(request, 'reservation_success.html')
        
    else:
        miFormulario = ReservationForm()

        return render(request, 'shop.html',{'miFormulario': miFormulario})

def success(request):
    return render(request, "reservation_success.html")

def contact_us(request):
    return render(request, "contact_us.html")

def index(request):
    return render(request, "index.html")

def add_product_view(request):
    if request.method == 'POST':
        formulario_producto = AddProductForm(request.POST, request.FILES)
        if formulario_producto.is_valid():
            data_formulario = formulario_producto.cleaned_data
            inscripcion = Product(name=data_formulario['name'], 
                                  description=data_formulario['description'],
                                  price=data_formulario['price'], 
                                  image=data_formulario['image']
                                  )
            inscripcion.save()
            
            return render(request, 'add_products_success.html')
    else:
        formulario_producto = AddProductForm()
    return render(request, 'add_products.html', {'formulario_producto': formulario_producto})    

def all_product_list(request):
    
    products = Product.objects.all()
    
    return render (request, "show_products.html", {"products": products})