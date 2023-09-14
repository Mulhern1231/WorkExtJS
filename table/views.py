from rest_framework import viewsets
from .models import DataRow
from .serializers import DataRowSerializer

class DataRowViewSet(viewsets.ModelViewSet):
    queryset = DataRow.objects.all()
    serializer_class = DataRowSerializer


from django.shortcuts import render

def table_view(request):
    return render(request, 'table/index.html')