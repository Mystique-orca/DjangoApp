from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import CredentialSerializer
from .models import Credential

class CredentialViewSet(viewsets.ModelViewSet):
	queryset = Credential.objects.all().order_by('username')
	serializer_class = CredentialSerializer
