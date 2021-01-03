# https://github.com/geopy/geopy

# Measuring Distance
from geopy.distance import geodesic

newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(geodesic(newport_ri, cleveland_oh).miles)

print("------------------------------------------")

# # geolocate a query to an address and coordinates
#
# from geopy.geocoders import Nominatim
#
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
# location = geolocator.geocode("175 5th Avenue NYC")
#
# print(location.address)
# print((location.latitude, location.longitude))
# print(location.raw)
