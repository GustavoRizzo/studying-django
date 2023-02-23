from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from company.models import Company, Member
from .serializers import CompanySerializer, MemberSerializer

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

class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows member to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

