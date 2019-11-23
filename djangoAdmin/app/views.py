from django.core import paginator
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from . models import Veiculo

# Create your views here.


def veiculo_list(request, categoria, template_name='veiculo_list.html'):
    query = request.GET.get('busca', '')
    ordenar = request.GET.get('ordenar', '')
    page = request.GET.get('page', '')
    if query:
        if categoria != 'todos':
            veiculo = Veiculo.objects.filter(modelo__icontains=query, tipo=categoria)
        else:
            veiculo = Veiculo.objects.filter(modelo__icontains=query)
    else:
        try:
            if categoria != 'todos':
                if ordenar:
                    veiculo = Veiculo.objects.filter(tipo=categoria).order_by(ordenar)
                else:
                    veiculo = Veiculo.objects.filter(tipo=categoria)
            else:
                if ordenar:
                    veiculo = Veiculo.objects.all().order_by(ordenar)
                else:
                    veiculo = Veiculo.objects.all()
            veiculo = Paginator(veiculo, 1)
            veiculo = veiculo.page(page)
        except PageNotAnInteger:
            veiculo = veiculo.page(1)
        except EmptyPage:
            veiculo = paginator.page(paginator.num_pages)
    veiculos = {'lista': veiculo}
    return render(request, template_name, veiculos)


def veiculo_profile(request, pk, template_name='veiculo_profile.html'):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    return render(request, template_name, {'veiculo': veiculo})
