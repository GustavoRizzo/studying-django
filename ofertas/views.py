from django.shortcuts import render
from ofertas.models import Oferta

def home(request):
    ofertas_list = Oferta.objects.order_by('name')[:10]
    context = {'ofertas_list': ofertas_list}
    return render(request, 'ofertas/home.html', context)