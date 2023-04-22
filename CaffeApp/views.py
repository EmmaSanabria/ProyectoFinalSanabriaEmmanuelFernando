from django.shortcuts import render, redirect
from CaffeApp.models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

@login_required
def index(request):
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
            return render (request, "reservation_success.html")
        
    else:
        miFormulario = ReservationForm()

        return render(request, 'index_page.html',{'miFormulario': miFormulario})
    
def success(request):
    return render(request, "reservation_success.html")

def contact_us(request):
    return render(request, "contact_us.html")

@method_decorator(staff_member_required(login_url='/CaffeApp/index_page/'), name='dispatch')
class ProductList(LoginRequiredMixin, ListView):
    model= Product
    template_name= "show_products.html"
    context_object_name= "products"
    
@method_decorator(staff_member_required(login_url='/CaffeApp/index_page/'), name='dispatch')
class ProductDetail(LoginRequiredMixin, DetailView):
    model= Product
    template_name= "detail_product.html"
    context_object_name= "product"
    
@method_decorator(staff_member_required(login_url='/CaffeApp/index_page/'), name='dispatch')
class ProductCreate(LoginRequiredMixin, CreateView):
    model= Product
    template_name= "add_products.html"
    fields= ['name','price','description','image']
    success_url= '/CaffeApp/'

@method_decorator(staff_member_required(login_url='/CaffeApp/index_page/'), name='dispatch')
class ProductUpdate(LoginRequiredMixin, UpdateView):
    model= Product
    template_name= "update_products.html"   
    fields= ['description','price']
    success_url= '/CaffeApp/'
    context_object_name= 'product'
    
@method_decorator(staff_member_required(login_url='/CaffeApp/index_page/'), name='dispatch')
class ProductDelete(LoginRequiredMixin, DeleteView):
    model= Product
    template_name= "delete_products.html"   
    fields= ['description','price']
    success_url= '/CaffeApp/'
    context_object_name= 'product'
    
def login_form(request):
    if request.method == 'POST':  
        miFormulario = AuthenticationForm(request, data=request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            user = data['username']
            psw= data['password']
            
            user_data = authenticate(username= user, password= psw )
            
            if user_data:
                login(request, user_data)
                return redirect(reverse('index'))            
            else:
                return render (request, "index_page.html", {"mensaje": 'Error en los datos'})
        else:
            return render (request, "index_page.html", {"mensaje": 'Formulario invalido'})
    else:
        miFormulario = AuthenticationForm()
        return render(request, 'login.html',{'miFormulario': miFormulario})
    
def register_form(request):
    if request.method == 'POST':  
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            
            data = user_creation_form.cleaned_data
            username = data["username"]
            user_creation_form.save()
            return render(request, 'index_page.html', {'mensaje': f'Usuario {username} creado'}) 

        else:
            return render (request, "index_page.html", {"mensaje": 'Formulario invalido'})
    else:
        user_creation_form = UserCreationForm()
        return render(request, 'register.html',{'user_creation_form': user_creation_form })