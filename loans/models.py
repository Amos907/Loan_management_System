from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
#import pandas as pd


# Create your models here.


class LoanType(models.Model):
    # REDUCING_BALANCE = 'Reducing Balance'
    # FIXED_INTEREST = 'Fixed Interest'

    # INTEREST_CHOICES = [
    #     (REDUCING_BALANCE, 'Reducing Balance'),
    #     (FIXED_INTEREST, 'Fixed Interest'),
    # ]

    loan_type_id = models.AutoField(primary_key=True)

    loan_type_name = models.CharField(
        max_length=200)
    description = models.CharField(max_length=500, null=True)
    interest_rate = models.IntegerField(default=0, null=True, blank=True)
    duration = models.IntegerField(
        default=0, null=True, blank=True)

    # interest_type = models.CharField(
    #     max_length=200,
    #     choices=INTEREST_CHOICES,
    #     default=REDUCING_BALANCE

    # )

    # fixed_interest_duration = models.IntegerField(
    #     default=0, blank=True, null=True)
    # fixed_interest_rate = models.IntegerField(default=0, null=True, blank=True)
    # fixed_penalty_rate = models.IntegerField(default=0, blank=True, null=True)

    # reducing_rate = models.IntegerField(default=0, blank=True, null=True)
    # reducing_penalty_rate = models.IntegerField(
    #     default=0, blank=True, null=True)

    # reducing_monthly_payables = models.IntegerField()

    def __str__(self):
        return self.loan_type_name

    @property
    def get_duration(self):
        return str(self.duration)


class Loan(models.Model):
    PERSONAL = 'Personal Loan'
    SMALL = 'Small Business Loan'
    MORTGAGE = 'Mortgage'

    LOAN_CHOICES = [
        (PERSONAL, 'Personal Loan'),
        (SMALL, 'Small Business Loan'),
        (MORTGAGE, 'Mortgage'),

    ]

    loan_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, db_column="username",
                             on_delete=models.SET_DEFAULT, default='')
    loan_type = models.CharField(
        max_length=200,
        choices=LOAN_CHOICES,
        default=PERSONAL

    )

    principal = models.IntegerField(blank=True, null=True, default=0)
    date_created = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.loan_type

    def get_duration(self):
        num_months = 0
        for i in LoanType.objects.filter(loan_type_name=self.loan_type):
            num_months = i.duration

        return num_months

    def get_interest(self):
        interest = 0
        for i in LoanType.objects.filter(loan_type_name=self.loan_type):
            interest = i.interest_rate
        return interest

    def calc_dueDate(self):
        date_format = '%Y/%m/%d'
        #dtObj = datetime.strptime(str(self.date_created), date_format)
        dur = int(self.get_duration())

        c_date = self.date_created.date()
        new_date = c_date + timedelta(dur*31)
        return new_date

    def amount_paid(self):
        # The interest is calculated yearly hence T has to be in years...
        amount_payable = self.principal + \
            (self.principal * (self.get_duration()/12)
             * (self.get_interest()/100))
        return int(amount_payable)
