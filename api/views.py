from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import LogEntry
from .serializers import LogEntrySerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000
    
    
class LogEntryViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    pagination_class = LargeResultsSetPagination