from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    deadline = serializers.ReadOnlyField(source='calc_dueDate')
    user = serializers.CharField(source='user.username', read_only=True)
    amount_payable = serializers.ReadOnlyField(source='amount_paid')
    first_name = serializers.CharField(source = 'user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Loan
        fields = ['user','first_name','last_name','email', 'loan_type', 'principal',
                  'date_created', 'deadline', 'amount_payable']
