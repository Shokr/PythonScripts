from phonenumbers import parse, geocoder, carrier

from test import number

ch_number = parse(number, "CH")

print(geocoder.description_for_number(ch_number, "en"))

service_number = parse(number, "RO")

print(carrier.name_for_number(service_number, "en"))
