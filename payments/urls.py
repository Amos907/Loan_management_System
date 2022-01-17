from django.urls import path, include
from .views import MakeLNMPayment ,make_payment,LNMCallbackUrlApiView, C2BConfirmationApiView, C2BValidationApiView

urlpatterns = [
    path('ln/<int:phone_no>/<int:amount>/',make_payment,name = 'makepayment'),
    path('daraja/', LNMCallbackUrlApiView.as_view(), name='lnm_callback_url'),
    path('validation_url/', C2BValidationApiView.as_view(), name='c2b_validation_url'),
    path('confirmation_url/', C2BConfirmationApiView.as_view(), name='c2b_confirmation_url'),
]

