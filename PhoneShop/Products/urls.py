from django.urls import path
from .views import main_page, product_brand_list, phone_model
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',  main_page, name='home_page'),
    path('<int:pk>', phone_model, name='phone_model'),
    path('<brand>', product_brand_list, name='product_brand_list'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
