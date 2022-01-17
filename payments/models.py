from django.db import models

# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     class Meta:
#         abstract = True

# M-pesa Payment models
class LNMOnline(models.Model):
    merchant_request_id = models.CharField(max_length=50)
    checkout_request_id = models.CharField(max_length=120)
    result_code = models.IntegerField()
    result_desc = models.TextField()
    amount = models.FloatField()
    mpesa_receipt_number = models.CharField(max_length=15)
    balance = models.CharField(blank=True, null=True , max_length=12)
    transaction_date = models.DateTimeField()
    phonenumber = models.CharField(max_length=13)

    def __repr__(self):
        return f'{self.mpesa_receipt_number}'

class C2BPayments(models.Model):
    TransactionType = models.CharField(max_length=50, blank=True, null=True)
    TransID = models.CharField(max_length=30, blank=True, null=True)
    TransTime = models.CharField(max_length=50, blank=True, null=True)
    TransAmount = models.CharField(max_length=120, blank=True, null=True)
    BusinessShortCode = models.CharField(max_length=50, blank=True, null=True)
    BillRefNumber = models.CharField(max_length=120, blank=True, null=True)
    InvoiceNumber = models.CharField(max_length=120, blank=True, null=True)
    OrgAccountBalance = models.CharField(max_length=120, blank=True, null=True)
    ThirdPartyTransID = models.CharField(max_length=120, blank=True, null=True)
    MSISDN = models.CharField(max_length=25, blank=True, null=True)
    FirstName = models.CharField(max_length=50, blank=True, null=True)
    MiddleName = models.CharField(max_length=50, blank=True, null=True)
    LastName = models.CharField(max_length=50, blank=True, null=True)

    def __repr__(self):
        return f'{self.InvoiceNumber}'