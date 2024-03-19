from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import Account
from accounts.serializers import AccountSerializer

# Create your views here.


class CreateAccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
