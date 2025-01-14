from unittest import result
import uuid 
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='./documents/')
class Documentexp(models.Model):
    docfileexp = models.FileField(upload_to='./export/')

class Experimentos(models.Model):
    id_experimento = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='../documents/')
    numero_repeticoes = models.IntegerField()
    tamanhos_reducao = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Experimento(models.Model):
    nome = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='documents/')
    numero_repeticoes = models.IntegerField()
    tamanhos_reducao = models.CharField(max_length=200)
    salvarDf_O = models.FileField(upload_to='../export/')
    salvarDf_R = models.FileField(upload_to='../export/')

    def __str__(self):
        return self.nome
    
class Original(models.Model):
    id_original = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attr_conc_max   = models.FloatField()
    attr_conc_mean  = models.FloatField()
    attr_conc_median = models.FloatField()
    attr_conc_min   = models.FloatField()
    attr_conc_sd = models.FloatField()
    attr_ent_max= models.FloatField()
    attr_ent_mean= models.FloatField()
    attr_ent_median= models.FloatField()
    attr_ent_min = models.FloatField()
    attr_ent_sd = models.FloatField()
    attr_to_inst = models.FloatField()
    cat_to_num = models.FloatField()
    cor_max = models.FloatField()
    cor_mean= models.FloatField()
    cor_median= models.FloatField()
    cor_min= models.FloatField()
    cor_sd= models.FloatField()
    cov_max= models.FloatField()
    cov_mean= models.FloatField()
    cov_median= models.FloatField()
    cov_min= models.FloatField()
    cov_sd= models.FloatField()
    eigenvalues_max= models.FloatField()
    eigenvalues_mean= models.FloatField()
    eigenvalues_median= models.FloatField()
    eigenvalues_min= models.FloatField()
    eigenvalues_sd= models.FloatField()
    g_mean_max= models.FloatField()
    g_mean_mean= models.FloatField()
    g_mean_median= models.FloatField()
    g_mean_min= models.FloatField()
    g_mean_sd= models.FloatField()
    h_mean_max= models.FloatField()
    h_mean_mean= models.FloatField()
    h_mean_median= models.FloatField()
    h_mean_min= models.FloatField()
    h_mean_sd= models.FloatField()
    inst_to_attr= models.FloatField()
    iq_range_max= models.FloatField()
    iq_range_mean= models.FloatField()
    iq_range_median= models.FloatField()
    iq_range_min= models.FloatField()
    iq_range_sd= models.FloatField()
    kurtosis_max= models.FloatField()
    kurtosis_mean= models.FloatField()
    kurtosis_median= models.FloatField()
    kurtosis_min= models.FloatField()
    kurtosis_sd= models.FloatField()
    mad_max= models.FloatField()
    mad_mean= models.FloatField()
    mad_median= models.FloatField()
    mad_min= models.FloatField()
    mad_sd= models.FloatField()
    max_max= models.FloatField()
    max_mean= models.FloatField()
    max_median= models.FloatField()
    max_min= models.FloatField()
    max_sd= models.FloatField()
    mean_max= models.FloatField()
    mean_mean= models.FloatField()
    mean_median= models.FloatField()
    mean_min= models.FloatField()
    mean_sd= models.FloatField()
    median_max= models.FloatField()
    median_mean= models.FloatField()
    median_median= models.FloatField()
    median_min= models.FloatField()
    median_sd= models.FloatField()
    min_max= models.FloatField()
    min_mean= models.FloatField()
    min_median= models.FloatField()
    min_min= models.FloatField()
    min_sd= models.FloatField()
    nr_attr= models.FloatField()
    nr_bin= models.FloatField()
    nr_cat= models.FloatField()
    nr_cor_attr= models.FloatField()
    nr_norm= models.FloatField()
    nr_num= models.FloatField()
    nr_outliers= models.FloatField()
    num_to_cat= models.FloatField()
    range_max= models.FloatField()
    range_mean= models.FloatField()
    range_median= models.FloatField()
    range_min= models.FloatField()
    range_sd= models.FloatField()
    sd_max= models.FloatField()
    sd_mean= models.FloatField()
    sd_median= models.FloatField()
    sd_min= models.FloatField()
    sd_sd= models.FloatField()
    skewness_max= models.FloatField()
    skewness_mean= models.FloatField()
    skewness_median= models.FloatField()
    skewness_min= models.FloatField()
    skewness_sd= models.FloatField()
    sparsity_max= models.FloatField()
    sparsity_mean= models.FloatField()
    sparsity_median= models.FloatField()
    sparsity_min= models.FloatField()
    sparsity_sd= models.FloatField()
    t_mean_max= models.FloatField()
    t_mean_mean= models.FloatField()
    t_mean_median= models.FloatField()
    t_mean_min= models.FloatField()
    t_mean_sd= models.FloatField()
    var_max= models.FloatField()
    var_mean= models.FloatField()
    var_median = models.FloatField()
    var_min = models.FloatField()
    var_sd= models.FloatField()
    def __str__(self):
        return self.id_original
class Resultados(models.Model):
    id_resultado = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tamanho_reducao = models.IntegerField()
    attr_conc_max   = models.FloatField()
    attr_conc_mean  = models.FloatField()
    attr_conc_median = models.FloatField()
    attr_conc_min   = models.FloatField()
    attr_conc_sd = models.FloatField()
    attr_ent_max= models.FloatField()
    attr_ent_mean= models.FloatField()
    attr_ent_median= models.FloatField()
    attr_ent_min = models.FloatField()
    attr_ent_sd = models.FloatField()
    attr_to_inst = models.FloatField()
    cat_to_num = models.FloatField()
    cor_max = models.FloatField()
    cor_mean= models.FloatField()
    cor_median= models.FloatField()
    cor_min= models.FloatField()
    cor_sd= models.FloatField()
    cov_max= models.FloatField()
    cov_mean= models.FloatField()
    cov_median= models.FloatField()
    cov_min= models.FloatField()
    cov_sd= models.FloatField()
    eigenvalues_max= models.FloatField()
    eigenvalues_mean= models.FloatField()
    eigenvalues_median= models.FloatField()
    eigenvalues_min= models.FloatField()
    eigenvalues_sd= models.FloatField()
    g_mean_max= models.FloatField()
    g_mean_mean= models.FloatField()
    g_mean_median= models.FloatField()
    g_mean_min= models.FloatField()
    g_mean_sd= models.FloatField()
    h_mean_max= models.FloatField()
    h_mean_mean= models.FloatField()
    h_mean_median= models.FloatField()
    h_mean_min= models.FloatField()
    h_mean_sd= models.FloatField()
    inst_to_attr= models.FloatField()
    iq_range_max= models.FloatField()
    iq_range_mean= models.FloatField()
    iq_range_median= models.FloatField()
    iq_range_min= models.FloatField()
    iq_range_sd= models.FloatField()
    kurtosis_max= models.FloatField()
    kurtosis_mean= models.FloatField()
    kurtosis_median= models.FloatField()
    kurtosis_min= models.FloatField()
    kurtosis_sd= models.FloatField()
    mad_max= models.FloatField()
    mad_mean= models.FloatField()
    mad_median= models.FloatField()
    mad_min= models.FloatField()
    mad_sd= models.FloatField()
    max_max= models.FloatField()
    max_mean= models.FloatField()
    max_median= models.FloatField()
    max_min= models.FloatField()
    max_sd= models.FloatField()
    mean_max= models.FloatField()
    mean_mean= models.FloatField()
    mean_median= models.FloatField()
    mean_min= models.FloatField()
    mean_sd= models.FloatField()
    median_max= models.FloatField()
    median_mean= models.FloatField()
    median_median= models.FloatField()
    median_min= models.FloatField()
    median_sd= models.FloatField()
    min_max= models.FloatField()
    min_mean= models.FloatField()
    min_median= models.FloatField()
    min_min= models.FloatField()
    min_sd= models.FloatField()
    nr_attr= models.FloatField()
    nr_bin= models.FloatField()
    nr_cat= models.FloatField()
    nr_cor_attr= models.FloatField()
    nr_norm= models.FloatField()
    nr_num= models.FloatField()
    nr_outliers= models.FloatField()
    num_to_cat= models.FloatField()
    range_max= models.FloatField()
    range_mean= models.FloatField()
    range_median= models.FloatField()
    range_min= models.FloatField()
    range_sd= models.FloatField()
    sd_max= models.FloatField()
    sd_mean= models.FloatField()
    sd_median= models.FloatField()
    sd_min= models.FloatField()
    sd_sd= models.FloatField()
    skewness_max= models.FloatField()
    skewness_mean= models.FloatField()
    skewness_median= models.FloatField()
    skewness_min= models.FloatField()
    skewness_sd= models.FloatField()
    sparsity_max= models.FloatField()
    sparsity_mean= models.FloatField()
    sparsity_median= models.FloatField()
    sparsity_min= models.FloatField()
    sparsity_sd= models.FloatField()
    t_mean_max= models.FloatField()
    t_mean_mean= models.FloatField()
    t_mean_median= models.FloatField()
    t_mean_min= models.FloatField()
    t_mean_sd= models.FloatField()
    var_max= models.FloatField()
    var_mean= models.FloatField()
    var_median = models.FloatField()
    var_min = models.FloatField()
    var_sd= models.FloatField()
    
    def __str__(self):
        return self.id_resultado
    
