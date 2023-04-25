from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    # Url relacionados a Reservation
    path('', index, name= 'index'),
    path('lists-messages/', MessagesList.as_view(), name= 'lists-messages'),
    path('detail-messages/<pk>/', MessagesDetail.as_view(), name= 'detail-messages'),
    path('formsucess/', success, name= 'success'),
    path('delete-messages/<pk>/', MessagesDelete.as_view(), name= 'delete-messages'),
    # Url relacionados a Product
    path('lists-product/', ProductList.as_view(), name= 'lists-product'),
    path('detail-product/<pk>/', ProductDetail.as_view(), name= 'detail-product'),
    path('create-product/', ProductCreate.as_view(), name= 'create-product'),
    path('update-product/<pk>/', ProductUpdate.as_view(), name= 'update-product'),
    path('delete-product/<pk>/', ProductDelete.as_view(), name= 'delete-product'),
    # Url relacionados a Login
    path('login', login_form , name= 'login'),
    path('register/', register_form , name= 'register'),
    path('logout/', LogoutView.as_view(template_name= 'users/logout.html'), name= 'logout'),
    path('edit-user/', edit_user, name= 'edit-user'),
    # Url relacionados a Staff
    path('lists-staff/', StaffList.as_view(), name= 'lists-staff'),
    path('detail-staff/<pk>/', StaffDetail.as_view(), name= 'detail-staff'),
    path('create-staff/', StaffCreate.as_view(), name= 'create-staff'),
    path('update-staff/<pk>/', StaffUpdate.as_view(), name= 'update-staff'),
    path('delete-staff/<pk>/', StaffDelete.as_view(), name= 'delete-staff'),
    # Url relacionados a Promo
    path('lists-promo/', PromoList.as_view(), name= 'lists-promo'),
    path('detail-promo/<pk>/', PromoDetail.as_view(), name= 'detail-promo'),
    path('create-promo/', PromoCreate.as_view(), name= 'create-promo'),
    path('update-promo/<pk>/', PromoUpdate.as_view(), name= 'update-promo'),
    path('delete-promo/<pk>/', PromoDelete.as_view(), name= 'delete-promo'),
    #Url Paginas genericas
    path('contact/', contact_us, name= 'contact_us'),
    path('carousel/', carousel, name= 'carousel'), #temporal
    path('<str:page>/', views.no_pages, name='no_pages'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)