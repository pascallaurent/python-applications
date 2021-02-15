from folium import Map, Marker, Popup
from geo import Geopoint

# Location coordinates
locations = [[18.6390, -74.1181],
             [18.598334, -73.960801],
             [18.608997, -74.384686],
             [18.549278, -74.271252],
             [18.19922, -73.75169]]

# Folium Map instance
mymap = Map(location=[18.6390, -74.1181])

# house the content for the popup
popup_content = ""

for lat, lon in locations:
    # create a geo point instance
    geopoint = Geopoint(latitude=lat, longitude=lon)

    for weather in geopoint.get_weather():
        hr = '<hr style="margin: 1px;">'
        text = f'{weather[0][11:13]}h: {round(weather[1])}°F <img src="http://openweathermap.org/img/wn/{weather[3]}@2x.png" width="35">'
        popup_content += text + hr

    popup = Popup(popup_content, max_width=300)
    popup.add_to(geopoint)
    geopoint.add_to(mymap)
    popup_content = ""

# add a marker to the map
# jeremie = Marker(location = [latitude, longitude], popup = 'Jeremie')
# jeremie.add_to(mymap)

# save map instance
mymap.save('map.html')
