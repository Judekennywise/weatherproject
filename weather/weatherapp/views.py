from django.shortcuts import render

# Create your views here.
import urllib.request
import json

def index(request):
   return(render(request, 'index.html'))

   """ if request.method== 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&APPID=3eb3e2e6a06817b3e14b2862ef367bac').read()
        list_of_data = json.loads(source)
        data = {
        "name": str(list_of_data['name']),
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + 
        str(list_of_data['coord']['lat']),
        "temp":str(list_of_data['main']['temp']) + '°C',
        "timezone": int(list_of_data['timezone']/3600),
        "pressure" :str(list_of_data['main']['pressure']),
        "humidity":str(list_of_data['main']['humidity']),
        "main":str(list_of_data['weather'][0]['main']),
        "description" :str(list_of_data['weather'][0]['description']),
        "icon":list_of_data['weather'][0]['icon'],
        }
        print(list_of_data)
    else:
        data= {}"""





