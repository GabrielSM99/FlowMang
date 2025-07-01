from django import forms
from .models import Estado, Cidade, Rio, Estacao, VazaoDiaria, ResumoMensal, ReportEtl, ConfigEtl

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nome']

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['estado', 'nome']

class RioForm(forms.ModelForm):
    class Meta:
        model = Rio
        fields = ['nome', 'descricao']

class EstacaoForm(forms.ModelForm):
    class Meta:
        model = Estacao
        fields = ['rio', 'cidade', 'codigo_estacao', 'codigo_bacia', 'codigo_sub_bacia', 'nome', 'latitude', 'longitude', 'altitude', 'operando', 'ultima_atualizacao']

class ResumoMensalForm(forms.ModelForm):
    class Meta:
        model = ResumoMensal
        fields = ['estacao', 'data_inicial', 'data_insercao_ana', 'metodo_obtencao', 'nivel_consistencia', 'vazao_media', 'vazao_maxima', 'vazao_minima', 'vazao_media_real', 'vazao_maxima_real', 'vazao_minima_real']

class VazaoDiariaForm(forms.ModelForm):
    class Meta:
        model = VazaoDiaria
        fields = ['resumo_mensal', 'vazao', 'vazao_status', 'data_vazao']

class ReportEtlForm(forms.ModelForm):
    class Meta:
        model = ReportEtl
        fields = ['data_inicio', 'data_fim', 'erro']

class ConfigEtlForm(forms.ModelForm):
    class Meta:
        model = ConfigEtl
        fields = ['ativo', 'data_atualizacao_inicial']