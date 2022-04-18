"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from produto.views import ProdutoViewSets
from ig.views import IgViewSets
from camareira.views import CamareiraViewSet
from emeil.views import EmeilViewSet
from quartos.views import QuartoViewSet
from ocupacoes.views import OcupacaoViewSet
from index.views import DadosViewSet
from comanda.views import ComandaViewSet
from patio.views import PatioViewSet
from usuarios.views import UsuarioViewSet
from caixa.views import CaixaViewSet
from painel.views import PainelViewSet
from infos.views import CabecaViewSet

router = routers.DefaultRouter()
router.register('produtos', ProdutoViewSets, basename='produtos')
router.register('igs', IgViewSets, basename='ig')
router.register('camareiras', CamareiraViewSet, basename='camareira')
router.register('emails', EmeilViewSet, basename='email')
router.register('quartos', QuartoViewSet, basename='quarto')
router.register('ocupacoes', OcupacaoViewSet, basename='ocupacao')
router.register('dados', DadosViewSet, basename='dados')
router.register('comanda', ComandaViewSet, basename='comanda')
router.register('patio', PatioViewSet, basename='patio')
router.register('usuarios', UsuarioViewSet, basename='usuario')
router.register('caixa', CaixaViewSet, basename='caixa')
router.register('painel', PainelViewSet, basename='painel')
router.register('header', CabecaViewSet, basename='header')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
