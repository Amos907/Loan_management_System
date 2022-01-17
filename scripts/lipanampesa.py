import requests
from scripts.access_token import generate_access_token
from scripts.utils import generate_timestamp
from scripts.password import generate_password
from decouple import Csv, config

# Execute all functions
formatted_time = generate_timestamp()
password = generate_password(formatted_time)
my_access_token = generate_access_token()


def lipa_na_mpesa(phonenumber, amount):
    print(my_access_token)
    print('Start excecuting the Simulate LNMOnline function:::')
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": config('MPESA_SHORTCODE'),
        "Password": password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phonenumber,
        "PartyB": config('MPESA_SHORTCODE'),
        "PhoneNumber":phonenumber,
        "CallBackURL": "http://1509-197-156-137-157.ngrok.io/daraja/",
        "AccountReference": "AMOS",
        "TransactionDesc": "Pay for internet"
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    return response.text
    
