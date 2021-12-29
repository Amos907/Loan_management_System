from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    deadline = serializers.ReadOnlyField(source='calc_dueDate')
    user = serializers.CharField(source='user.username', read_only=True)
    amount_payable = serializers.ReadOnlyField(source='amount_paid')

    class Meta:
        model = Loan
        fields = ['user', 'loan_type', 'principal',
                  'date_created', 'deadline', 'amount_payable']
