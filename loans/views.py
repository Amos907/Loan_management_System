from django.shortcuts import render
from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import LoanSerializer
from .models import Loan


class LoansView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permision_classes = [permissions.IsAuthenticated, ]

    def get(self, request, format=None):
        queryset = Loan.objects.all()
        serializer = LoanSerializer(queryset, many=True)
        return Response(serializer.data)


# Create your views here.
