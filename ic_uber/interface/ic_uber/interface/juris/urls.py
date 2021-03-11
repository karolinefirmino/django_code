from django.urls import path, include
from . import views 
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
import juris.views
from django.conf import settings
import os
from django.conf.urls import  url

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'juris'

urlpatterns = [

    path('', views.MainView.as_view(), name='all'),
    #path('accounts/', views.MyView.as_view(), name='login'),
    path('protect', views.ProtectView.as_view(), name='protect'),
    path('python', views.DumpPython.as_view(), name='python'),

    path('empresa/', views.EmpresaView.as_view(), name='empresa_list'),
    path('empresa/create/', views.EmpresaCreate.as_view(), name='empresa_create'),
    path('empresa/<int:pk>/update/', views.EmpresaUpdate.as_view(), name='empresa_update'),
    path('empresa/<int:pk>/delete/', views.EmpresaDelete.as_view(), name='empresa_delete'),

    path('busca/', views.TermoBuscaView.as_view(), name='busca_list'),
    path('busca/create/', views.TermoBuscaCreate.as_view(), name='busca_create'),
    path('busca/<int:pk>/update/', views.TermoBuscaUpdate.as_view(), name='busca_update'),
    path('busca/<int:pk>/delete/', views.TermoBuscaDelete.as_view(), name='busca_delete'),

    path('arquivo/', views.arquivo_list, name='arquivo_list'),
    path('arquivo/create/', views.TermoBuscaCreate.as_view(), name='arquivo_create'),
    path('arquivo/<int:pk>/update/', views.TermoBuscaUpdate.as_view(), name='arquivo_update'),
    path('arquivo/<int:pk>/delete/', views.TermoBuscaDelete.as_view(), name='arquivo_delete'),

    path('cadastro/',  views.CadastroView.as_view(), name='cadastro_list'),
    path('cadastro/create/', views.CadastroCreate.as_view(), name='cadastro_create'),
    path('cadastro/<int:pk>/update/', views.CadastroUpdate.as_view(), name='cadastro_update'),
    path('cadastro/<int:pk>/delete/', views.CadastroDelete.as_view(), name='cadastro_delete'),

    path('upload/', views.upload, name='upload'),
    path('index/', views.index, name= 'index'),
    #path('cadastro/json/', views.cadastro_json, name='json'),

    #path('arquivo/files/', views.upload_file, name='upload_file'),
    #url(r'^my/datatable/data/$', views.OrderListJson.as_view(), name='order_list_json'),

    #path('d/', views.cadastroformpage, name='cadastro_create'),

    
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

