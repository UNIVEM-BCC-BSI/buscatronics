from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = format_suffix_patterns([
    path('kabum/', views.kabum_list),
    path('terabyte/', views.terabyte_list),
    path('americanas/', views.americanas_list),
    path('buscape/', views.buscape_list),
    path('casas-bahia/', views.casasbahia_list),
    path('epic/', views.epicgames_list),
    path('gog/', views.gog_list),
    path('magalu/', views.magalu_list),
    path('nuuvem/', views.nuuvem_list),
    path('steam/', views.steam_list),
    path('submarino/', views.submarino_list),
    path('zoom/', views.zoom_list),
    path('plataforma_loja/', views.plataforma_e_loja),
])