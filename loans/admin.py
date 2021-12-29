from django.contrib import admin
from django.db.models import fields
from .models import LoanType, Loan


class LoanAdminSite(admin.ModelAdmin):
    model = Loan
    fields = ['user', 'loan_type', 'principal', 'date_created']
    list_display = ('user', 'loan_type', 'principal',
                    'date_created',   'calc_dueDate', 'amount_paid')

    readonly_fields = ['date_created']


admin.site.register(LoanType)
admin.site.register(Loan, LoanAdminSite)
# Register your models here.
