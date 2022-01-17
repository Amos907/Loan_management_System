from decouple import config, Csv

consumer_key = config("MPESA_CONSUMER_KEY")
consumer_secret = config("MPESA_CONSUMER_SECRET")

business_shortCode = config("MPESA_SHORTCODE")  # Lipa Na Mpesa Shortcode
lipa_na_mpesa_passkey = config("MPESA_PASSKEY")
c2b_shortcode = config('C2B_SHORTCODE')
msisnd = config('LNM_PHONE_NUMBER')
