from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views
app_name = 'core'

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='core:login'), name='logout'),
    path('erro-teste/', views.erro_teste, name='erro_teste'),

    path('estados/', views.listar_estados, name='estado_list'),
    path('estados/add/', views.criar_estado, name='estado_add'),
    path('estados/<int:pk>/edit/', views.editar_estado, name='estado_edit'),
    path('estados/<int:pk>/delete/', views.apagar_estado, name='estado_delete'),

   
    path('cidades/', views.listar_cidades, name='cidade_list'),
    path('cidades/add/', views.criar_cidade, name='cidade_add'),
    path('cidades/<int:pk>/edit/', views.editar_cidade, name='cidade_edit'),
    path('cidades/<int:pk>/delete/', views.apagar_cidade, name='cidade_delete'),

    
    path('rios/', views.listar_rios, name='rio_list'),
    path('rios/add/', views.criar_rio, name='rio_add'),
    path('rios/<int:pk>/edit/', views.editar_rio, name='rio_edit'),
    path('rios/<int:pk>/delete/', views.apagar_rio, name='rio_delete'),

   
    path('estacoes/', views.listar_estacoes, name='estacao_list'),
    path('estacoes/add/', views.criar_estacao, name='estacao_add'),
    path('estacoes/<int:pk>/edit/', views.editar_estacao, name='estacao_edit'),
    path('estacoes/<int:pk>/delete/', views.apagar_estacao, name='estacao_delete'),

   
    path('resumos/', views.listar_resumos, name='resumo_list'),
    path('resumos/add/', views.criar_resumo, name='resumo_add'),
    path('resumos/<int:pk>/edit/', views.editar_resumo, name='resumo_edit'),
    path('resumos/<int:pk>/delete/', views.apagar_resumo, name='resumo_delete'),

   
    path('vazoes/', views.listar_vazoes, name='vazao_list'),
    path('vazoes/add/', views.criar_vazao, name='vazao_add'),
    path('vazoes/<int:pk>/edit/', views.editar_vazao, name='vazao_edit'),
    path('vazoes/<int:pk>/delete/', views.apagar_vazao, name='vazao_delete'),

    
    path('reports/', views.listar_reports, name='report_list'),
    path('reports/add/', views.criar_report, name='report_add'),
    path('reports/<int:pk>/edit/', views.editar_report, name='report_edit'),
    path('reports/<int:pk>/delete/', views.apagar_report, name='report_delete'),

    
    path('configs/', views.listar_configs, name='config_list'),
    path('configs/add/', views.criar_config, name='config_add'),
    path('configs/<int:pk>/edit/', views.editar_config, name='config_edit'),
    path('configs/<int:pk>/delete/', views.apagar_config, name='config_delete'),


    
]
