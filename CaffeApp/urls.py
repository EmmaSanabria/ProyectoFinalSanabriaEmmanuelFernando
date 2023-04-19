from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', index, name= 'index'),
    path('shop/', shop, name= 'shop'),
    path('formsucess/', success, name= 'success'),
    path('add-product/', add_product_view, name= 'add-product'),
    path('contact/', contact_us, name= 'contact_us'),
    path('show-products/', all_product_list, name= 'show-product'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)