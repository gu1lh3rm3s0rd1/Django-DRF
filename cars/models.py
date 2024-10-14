from django.db import models
from django.contrib.auth.models import User # usuarios

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Marca')
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        #campo string principal da tabela
        return self.name
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['name']


class Car(models.Model):
    model = models.CharField(max_length=100, verbose_name='Nome')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Marca')
    factory_year = models.IntegerField(verbose_name='Ano de Fabricação', null=True)
    model_year = models.IntegerField(verbose_name='Ano do Modelo', null=True)
    color = models.CharField(max_length=50, verbose_name='Cor')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, max_length=100, verbose_name='Proprietário')
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['model']