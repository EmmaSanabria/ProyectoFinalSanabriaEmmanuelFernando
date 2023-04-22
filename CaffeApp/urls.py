from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index_page/', index, name= 'index'),
    path('formsucess/', success, name= 'success'),
    path('contact/', contact_us, name= 'contact_us'),
    path('lists-product/', ProductList.as_view(), name= 'lists-product'),
    path('detail-product/<pk>/', ProductDetail.as_view(), name= 'detail-product'),
    path('create-product/', ProductCreate.as_view(), name= 'create-product'),
    path('update-product/<pk>/', ProductUpdate.as_view(), name= 'update-product'),
    path('delete-product/<pk>/', ProductDelete.as_view(), name= 'delete-product'),
    path('', login_form , name= 'login'),
    path('register/', register_form , name= 'register'),
    path('logout/', LogoutView.as_view(template_name= 'logout.html'), name= 'logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)