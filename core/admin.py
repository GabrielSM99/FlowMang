from django.contrib import admin

from .models import (
    Estado, Cidade, Rio, RioCidade, Estacao,
    ReportEtl, ConfigEtl, ResumoMensal, VazaoDiaria
)
admin.site.register([
    Estado, Cidade, Rio, RioCidade, Estacao,
    ReportEtl, ConfigEtl, ResumoMensal, VazaoDiaria
])
