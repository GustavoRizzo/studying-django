from django.shortcuts import get_object_or_404, render
from .models import Company

def home(request):
    return render(request, 'company/home.html')

def company(request):
    company_list = Company.objects.order_by('name')[:10]
    context = {'company_list': company_list}
    return render(request, 'company/company.html', context)

def detail(request, company_id):
    company = get_object_or_404( Company, pk=company_id)
    return render(request, 'company/detail.html', {'company': company})