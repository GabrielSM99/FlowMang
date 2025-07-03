from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf import settings 
import requests


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Conta criada com sucesso!")
            return redirect('core:home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'core/register.html', {'form': form})

class CustomLoginView(auth_views.LoginView):
    template_name = 'core/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['RECAPTCHA_SITE_KEY'] = settings.RECAPTCHA_SITE_KEY
        return context

    def post(self, request, *args, **kwargs):
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if not result.get('success'):
            return render(request, self.template_name, {
                'form': self.get_form(),
                'recaptcha_error': 'Confirme o captcha para continuar.',
                'RECAPTCHA_SITE_KEY': settings.RECAPTCHA_SITE_KEY
            })

        return super().post(request, *args, **kwargs)
    
def home(request):
    return render(request, 'core/home.html')

@login_required
def listar_objetos(request, model, template, context_name):
    lista = model.objects.all()
    paginator = Paginator(lista, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, template, {context_name: page_obj})

@login_required
def criar_objeto(request, form_class, template, redirect_url):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class()
    return render(request, template, {'form': form})

@login_required
def editar_objeto(request, pk, model, form_class, template, redirect_url):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = form_class(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=obj)
    return render(request, template, {'form': form, 'object': obj})

@login_required
def apagar_objeto(request, pk, model, template, redirect_url, context_name):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_url)
    return render(request, template, {context_name: obj})

@login_required
def listar_estados(request):
    return listar_objetos(request, Estado, 'core/estado_list.html', 'estados')
@login_required
def criar_estado(request):
    return criar_objeto(request, EstadoForm, 'core/estado_form.html', 'core:estado_list')
@login_required
def editar_estado(request, pk):
    return editar_objeto(request, pk, Estado, EstadoForm, 'core/estado_form.html', 'core:estado_list')
@login_required
def apagar_estado(request, pk):
    return apagar_objeto(request, pk, Estado, 'core/estado_confirm_delete.html', 'core:estado_list', 'estado')
@login_required
def listar_cidades(request):
    return listar_objetos(request, Cidade, 'core/cidade_list.html', 'cidades')
@login_required
def criar_cidade(request):
    return criar_objeto(request, CidadeForm, 'core/cidade_form.html', 'core:cidade_list')
@login_required
def editar_cidade(request, pk):
    return editar_objeto(request, pk, Cidade, CidadeForm, 'core:cidade_form.html', 'core:cidade_list')
@login_required
def apagar_cidade(request, pk):
    return apagar_objeto(request, pk, Cidade, 'core/cidade_confirm_delete.html', 'core:cidade_list', 'cidade')
@login_required
def listar_rios(request):
    return listar_objetos(request, Rio, 'core/rio_list.html', 'rios')
@login_required
def criar_rio(request):
    return criar_objeto(request, RioForm, 'core/rio_form.html', 'core:rio_list')
@login_required
def editar_rio(request, pk):
    return editar_objeto(request, pk, Rio, RioForm, 'core:rio_form.html', 'core:rio_list')
@login_required
def apagar_rio(request, pk):
    return apagar_objeto(request, pk, Rio, 'core/rio_confirm_delete.html', 'core:rio_list', 'rio')
@login_required
def listar_estacoes(request):
    return listar_objetos(request, Estacao, 'core/estacao_list.html', 'estacoes')
@login_required
def criar_estacao(request):
    return criar_objeto(request, EstacaoForm, 'core/estacao_form.html', 'core:estacao_list')
@login_required
def editar_estacao(request, pk):
    return editar_objeto(request, pk, Estacao, EstacaoForm, 'core/estacao_form.html', 'core:estacao_list')
@login_required
def apagar_estacao(request, pk):
    return apagar_objeto(request, pk, Estacao, 'core/estacao_confirm_delete.html', 'core:estacao_list', 'estacao')
@login_required
def listar_resumos(request):
    return listar_objetos(request, ResumoMensal, 'core/resumo_list.html', 'resumos')
@login_required
def criar_resumo(request):
    return criar_objeto(request, ResumoMensalForm, 'core/resumo_form.html', 'core:resumo_list')
@login_required
def editar_resumo(request, pk):
    return editar_objeto(request, pk, ResumoMensal, ResumoMensalForm, 'core/resumo_form.html', 'core:resumo_list')
@login_required
def apagar_resumo(request, pk):
    return apagar_objeto(request, pk, ResumoMensal, 'core/resumo_confirm_delete.html', 'core:resumo_list', 'resumo')
@login_required
def listar_vazoes(request):
    return listar_objetos(request, VazaoDiaria, 'core/vazao_list.html', 'vazoes')
@login_required
def criar_vazao(request):
    return criar_objeto(request, VazaoDiariaForm, 'core/vazao_form.html', 'core:vazao_list')
@login_required
def editar_vazao(request, pk):
    return editar_objeto(request, pk, VazaoDiaria, VazaoDiariaForm, 'core/vazao_form.html', 'core:vazao_list')
@login_required
def apagar_vazao(request, pk):
    return apagar_objeto(request, pk, VazaoDiaria, 'core/vazao_confirm_delete.html', 'core:vazao_list', 'vazao')
@login_required
def listar_reports(request):
    return listar_objetos(request, ReportEtl, 'core/report_list.html', 'reports')
@login_required
def criar_report(request):
    return criar_objeto(request, ReportEtlForm, 'core/report_form.html', 'core:report_list')
@login_required
def editar_report(request, pk):
    return editar_objeto(request, pk, ReportEtl, ReportEtlForm, 'core:report_form.html', 'core:report_list')
@login_required
def apagar_report(request, pk):
    return apagar_objeto(request, pk, ReportEtl, 'core/report_confirm_delete.html', 'core:report_list', 'report')
@login_required
def listar_configs(request):
    return listar_objetos(request, ConfigEtl, 'core/config_list.html', 'configs')
@login_required
def criar_config(request):
    return criar_objeto(request, ConfigEtlForm, 'core/config_form.html', 'core:config_list')
@login_required
def editar_config(request, pk):
    return editar_objeto(request, pk, ConfigEtl, ConfigEtlForm, 'core:config_form.html', 'core:config_list')
@login_required
def apagar_config(request, pk):
    return apagar_objeto(request, pk, ConfigEtl, 'core/config_confirm_delete.html', 'core:config_list', 'config')
def erro_teste(request):
    raise Exception("Erro 500!")
