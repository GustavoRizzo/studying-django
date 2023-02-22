from rest_framework.response import Response
from rest_framework.decorators import api_view

from company.models import Company
from .serializers import CompanySerializer

# Create your views here.
@api_view(['GET'])
def getData(request):
    person = {'name':'Dennis', 'age':28}
    return Response(person)

@api_view(['GET'])
def getCompanys(request):
    companys = Company.objects.all()
    serializer = CompanySerializer(companys, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addCompany(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()
