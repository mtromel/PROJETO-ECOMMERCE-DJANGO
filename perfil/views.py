from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


class Criar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Criar perfil')


class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar perfil')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')
