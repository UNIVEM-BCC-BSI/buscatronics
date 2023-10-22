from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = format_suffix_patterns([
    path('kabum/', views.kabum_list),
    path('terabyte/', views.terabyte_list),
    # path('steam/', views.steam_list),
    path('plataforma_loja/', views.plataforma_e_loja),
])