from django.db import models

class Estado(models.Model):
    id = models.AutoField("ID", primary_key=True)
    nome = models.CharField("Nome", max_length=44)

    class Meta:
        db_table = "tb_estado"

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    id = models.AutoField("ID", primary_key=True)
    estado = models.ForeignKey(
        Estado,
        verbose_name="Estado",
        on_delete=models.CASCADE,
        db_column="co_estado",
        related_name="cidades"
    )
    nome = models.CharField("Nome", max_length=44)

    class Meta:
        db_table = "tb_cidade"

    def __str__(self):
        return self.nome


class Rio(models.Model):
    id = models.AutoField("ID", primary_key=True)
    nome = models.CharField("Nome", max_length=144)
    descricao = models.CharField("Descrição", max_length=88, blank=True, null=True)

    class Meta:
        db_table = "tb_rio"

    def __str__(self):
        return self.nome


class RioCidade(models.Model):
    rio = models.ForeignKey(
        Rio,
        verbose_name="Rio",
        on_delete=models.CASCADE,
        db_column="co_rio",
        related_name="rios_cidade"
    )
    cidade = models.ForeignKey(
        Cidade,
        verbose_name="Cidade",
        on_delete=models.CASCADE,
        db_column="co_cidade",
        related_name="rios_cidade"
    )

    class Meta:
        db_table = "tb_rio_cidade"
        unique_together = (("rio", "cidade"),)

    def __str__(self):
        return f"{self.rio.nome} – {self.cidade.nome}"


class Estacao(models.Model):
    id = models.AutoField("ID", primary_key=True)
    rio = models.ForeignKey(
        Rio,
        verbose_name="Rio",
        on_delete=models.CASCADE,
        db_column="co_rio",
        related_name="estacoes"
    )
    cidade = models.ForeignKey(
        Cidade,
        verbose_name="Cidade",
        on_delete=models.CASCADE,
        db_column="co_cidade",
        related_name="estacoes"
    )
    codigo_estacao = models.BigIntegerField("Código da Estação")
    codigo_bacia = models.BigIntegerField("Código da Bacia", blank=True, null=True)
    codigo_sub_bacia = models.BigIntegerField("Código da Sub-Bacia", blank=True, null=True)
    nome = models.CharField("Nome", max_length=144, blank=True, null=True)
    latitude = models.CharField("Latitude", max_length=44, blank=True, null=True)
    longitude = models.CharField("Longitude", max_length=44, blank=True, null=True)
    altitude = models.CharField("Altitude", max_length=44, blank=True, null=True)
    operando = models.IntegerField("Operando", blank=True, null=True)
    ultima_atualizacao = models.DateTimeField("Última Atualização", blank=True, null=True)

    class Meta:
        db_table = "tb_estacao"

    def __str__(self):
        return self.nome or f"Estação {self.id}"


class ReportEtl(models.Model):
    id = models.AutoField("ID", primary_key=True)
    data_inicio = models.DateTimeField("Início ETL")
    data_fim = models.DateTimeField("Fim ETL")
    erro = models.CharField("Erro", max_length=128, blank=True, null=True)

    class Meta:
        db_table = "tb_report_etl"

    def __str__(self):
        return f"ETL {self.id}: {self.data_inicio:%Y-%m-%d %H:%M}"


class ConfigEtl(models.Model):
    id = models.AutoField("ID", primary_key=True)
    ativo = models.BooleanField("Ativo")
    data_atualizacao_inicial = models.DateField("Data Inicial", blank=True, null=True)

    class Meta:
        db_table = "tb_config_etl"

    def __str__(self):
        return f"Config ETL {self.id} – {'Ativo' if self.ativo else 'Inativo'}"


class ResumoMensal(models.Model):
    id = models.AutoField("ID", primary_key=True)
    estacao = models.ForeignKey(
        Estacao,
        verbose_name="Estação",
        on_delete=models.CASCADE,
        db_column="co_estacao",
        related_name="resumos_mensal"
    )
    data_inicial = models.DateTimeField("Data Inicial", blank=True, null=True)
    data_insercao_ana = models.DateTimeField("Data Inserção ANA", blank=True, null=True)
    metodo_obtencao = models.IntegerField("Método de Obtenção", blank=True, null=True)
    nivel_consistencia = models.IntegerField("Nível de Consistência", blank=True, null=True)
    vazao_media = models.FloatField("Vazão Média", blank=True, null=True)
    vazao_maxima = models.FloatField("Vazão Máxima", blank=True, null=True)
    vazao_minima = models.FloatField("Vazão Mínima", blank=True, null=True)
    vazao_media_real = models.FloatField("Vazão Média Real", blank=True, null=True)
    vazao_maxima_real = models.FloatField("Vazão Máxima Real", blank=True, null=True)
    vazao_minima_real = models.FloatField("Vazão Mínima Real", blank=True, null=True)

    class Meta:
        db_table = "tb_resumo_mensal"

    def __str__(self):
        return f"Resumo {self.id} – {self.estacao}"


class VazaoDiaria(models.Model):
    id = models.AutoField("ID", primary_key=True)
    resumo_mensal = models.ForeignKey(
        ResumoMensal,
        verbose_name="Resumo Mensal",
        on_delete=models.CASCADE,
        db_column="co_resumo_mensal",
        related_name="vazoes_diarias"
    )
    vazao = models.FloatField("Vazão", blank=True, null=True)
    vazao_status = models.IntegerField("Status da Vazão", blank=True, null=True)
    data_vazao = models.DateField("Data da Vazão")

    class Meta:
        db_table = "tb_vazao_diaria"

    def __str__(self):
        return f"{self.resumo_mensal} – {self.data_vazao}"