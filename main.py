#NOTE:before running this code
#pip install phonenumbers
#pip install geopy
#pip install folium

import phonenumbers
import folium

from test import number

from geopy.geocoders import Nominatim
#from opencage.geocoders import OpenCageGeocode

#from phonenumbers import timezone
from phonenumbers import geocoder

try:
    theNumber = phonenumbers.parse(number)#converting string to ph. no. format
    

    yourLoc = geocoder.description_for_number(theNumber, "en")#get geographical location
    print("Location = ", yourLoc,"\n")    
    
    
    
    #an API without a key
    loc = Nominatim(user_agent="GetLoc")
    

    # entering the location name
    getLoc = loc.geocode(yourLoc)
    
    
    # getting address
    yourLoc = getLoc.address

 
    # printing latitude and longitude
    lat = getLoc.latitude
    lng = getLoc.longitude
    print("Latitude = ", lat, "\n")
    print("Longitude = ", lng)


    myMap = folium.Map(location = [lat, lng], zoom_start = 3)

    folium.CircleMarker(
        location=[lat, lng],
        radius=50,
        popup=yourLoc,
        color="#3186cc",
        fill=True,
        fill_color="#3186cc",
    ).add_to((myMap))
    myMap.save("mylocation.html")

except:
    print("-----INVALID PHONE NUMBER-----")

#open the newly added html file in browser