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


def contact_us(request):
    return render(request, "contact_us.html")

def carousel(request):
    return render(request, "modals.html")

def no_pages(request, page):
    context = {'page': page}
    return render(request, 'no_pages.html', context)


#Inicio del sector de Reservacion


def index(request):
    if request.method == 'POST':
        
        miFormulario = MessagesForm(request.POST)
        
        if miFormulario.is_valid():

            data_formulario = miFormulario.cleaned_data

            inscripcion = Messages(name=data_formulario['name'], 
                                      email=data_formulario['email'], 
                                      phone=data_formulario['phone'], 
                                      number_guests= data_formulario['number_guests'],
                                      date= data_formulario['date'], 
                                      time=data_formulario['time'],
                                      message=data_formulario['message']
                                      )
            inscripcion.save()
            return render (request, "messages/messages_success.html")
        
    else:
        miFormulario = MessagesForm()
        return render(request, 'messages/index_page.html',{'miFormulario': miFormulario})
    
@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class MessagesList(LoginRequiredMixin, ListView):
    model= Messages
    template_name= "messages/show_messages.html"
    context_object_name= "messages"
    
@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class MessagesDelete(LoginRequiredMixin, DeleteView):
    model= Messages
    template_name= "messages/delete_messages.html"   
    success_url= '/CaffeApp/lists-messages/'
    context_object_name= 'messages'

@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class MessagesDetail(LoginRequiredMixin, DetailView):
    model= Messages
    template_name= "messages/detail_messages.html"
    context_object_name= "messages"

def success(request):
    return render(request, "messages/messages_success.html")

#Final del sertor de Reservacion

#Inicio del sertor de Producto

@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class ProductList(LoginRequiredMixin, ListView):
    model= Product
    template_name= "product/show_products.html"
    context_object_name= "products"
    
@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class ProductDetail(LoginRequiredMixin, DetailView):
    model= Product
    template_name= "product/detail_product.html"
    context_object_name= "product"
    
@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class ProductCreate(LoginRequiredMixin, CreateView):
    model= Product
    template_name= "product/add_products.html"
    fields = ['name', 'description', 'price', 'available', 'veggie_option', 'image']
    success_url= '/CaffeApp/lists-product/'

@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class ProductUpdate(LoginRequiredMixin, UpdateView):
    model= Product
    template_name= "product/update_products.html"   
    fields= ['description','price', 'available', 'veggie_option']
    success_url= '/CaffeApp/lists-product/'
    context_object_name= 'product'
    
@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class ProductDelete(LoginRequiredMixin, DeleteView):
    model= Product
    template_name= "product/delete_products.html"   
    success_url= '/CaffeApp/lists-product/'
    context_object_name= 'product'

#Final del sertor de Producto

#Inicio del sector de Usuarios
    
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
                return redirect(reverse('login'), {"mensaje": 'Error en los datos'})
        else:
            return redirect(reverse('login'), {"mensaje": 'Formulario invalido'})
    else:
        miFormulario = AuthenticationForm()
        return render(request, 'users/login.html', {'miFormulario': miFormulario})
    
def register_form(request):
    if request.method == 'POST':  
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            
            data = user_creation_form.cleaned_data
            username = data["username"]
            user_creation_form.save()
            return redirect(reverse('login') , {'mensaje': f'Usuario {username} creado'}) 

        else:
            return render (request, "users/login.html", {"mensaje": 'Formulario invalido'})
    else:
        user_creation_form = UserCreationForm()
        return render(request, 'users/register.html',{'user_creation_form': user_creation_form })

@login_required
def edit_user(request):
    
    acount = request.user  
    
    if request.method == 'POST':  
        miFormulario = EditUserForm(request.POST, instance= request.user)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            acount.email = data['email']
            acount.first_name = data['first_name']
            acount.last_name = data['last_name']
            acount.set_password(data["password1"])
            acount.save()
            return render (request, "messages/index_page.html", {"mensaje": 'Datos actualizados!'})           
        else:
            return render (request, "messages/index_page.html", {"mensaje": 'Formulario invalido'})
    else:
        miFormulario = EditUserForm(instance= request.user)
        return render(request, 'users/edit_user.html', {'miFormulario': miFormulario})
    
#Final del sector de Usuarios    

#Inicio del sector de Staff

@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class StaffList(LoginRequiredMixin, ListView):
    model= Staff
    template_name= "staff/show_staff.html"
    context_object_name= "Staff"
    
@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class StaffDetail(LoginRequiredMixin, DetailView):
    model= Staff
    template_name= "staff/detail_staff.html"
    context_object_name= "Staff"
    
@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class StaffCreate(LoginRequiredMixin, CreateView):
    model= Staff
    template_name= "staff/add_staff.html"
    fields = ('name','last_name', 'job', 'workshift', 'age', 'image')
    success_url= '/CaffeApp/lists-staff/'

@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class StaffUpdate(LoginRequiredMixin, UpdateView):
    model= Staff
    template_name= "staff/update_staff.html"   
    fields= ['job', 'workshift']
    success_url= '/CaffeApp/lists-staff/'
    context_object_name= 'Staff'
    
@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class StaffDelete(LoginRequiredMixin, DeleteView):
    model= Staff
    template_name= "staff/delete_staff.html"   
    success_url= '/CaffeApp/lists-staff/'
    context_object_name= 'Staff'

#Final del sector de Staff   

#Inicio del sector de Promo

@method_decorator(staff_member_required(login_url='/CaffeApp/index_page/'), name='dispatch')
class PromoList(LoginRequiredMixin, ListView):
    model= Promo_menu
    template_name= "promo/show_promo.html"
    context_object_name= "promo"
    
@method_decorator(staff_member_required(login_url='/CaffeApp/index_page/'), name='dispatch')
class PromoDetail(LoginRequiredMixin, DetailView):
    model= Promo_menu
    template_name= "promo/detail_promo.html"
    context_object_name= "promo"
    
@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class PromoCreate(LoginRequiredMixin, CreateView):
    model= Promo_menu
    template_name= "promo/add_promo.html"
    fields = ['name', 'description', 'price', 'available', 'veggie_option', 'image']
    success_url= '/CaffeApp/lists-promo/'

@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class PromoUpdate(LoginRequiredMixin, UpdateView):
    model= Promo_menu
    template_name= "promo/update_promo.html"   
    fields= ['description','price', 'available', 'veggie_option']
    success_url= '/CaffeApp/lists-promo/'
    context_object_name= 'promo'
    
@method_decorator(staff_member_required(login_url='/CaffeApp/'), name='dispatch')
class PromoDelete(LoginRequiredMixin, DeleteView):
    model= Promo_menu
    template_name= "promo/delete_promo.html"   
    success_url= '/CaffeApp/lists-promo/'
    context_object_name= 'promo'

#Final del sector de Promo  