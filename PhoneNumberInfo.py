import phonenumbers
from phonenumbers import geocoder, carrier

phone = input("[+] Enter Your Phone Number: ")
phoneNumber = phonenumbers.parse(phone)
  
Carrier = carrier.name_for_number(phoneNumber, 'en')
  
Region = geocoder.description_for_number(phoneNumber, 'en')
  
print("[*] Carrier: ",Carrier)
print("[*] Region: ",Region)

