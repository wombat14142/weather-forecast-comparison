import requests

def get_weather_data(lat, lon, api_key):
    # API-Endpunkt und Parameter
    #base_url = "http://api.openweathermap.org/data/2.5/weather?" # current weather
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"  # weather forecast 3 hour steps, 5 days
    #complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    complete_url = f"{base_url}lat={lat}&lon={lon}&appid={api_key}"

    # Anfrage an die OpenWeatherMap API senden
    response = requests.get(complete_url)

    # Antwort im JSON-Format
    data = response.json()

    # Überprüfen, ob die Anfrage erfolgreich war
    if data["cod"] != "404":
        # Daten extrahieren
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]

        # Wetterinformationen anzeigen
        print(f"Stadt: {city_name}")
        print(f"Temperatur: {main['temp']}°C")
        print(f"Gefühlte Temperatur: {main['feels_like']}°C")
        print(f"Luftfeuchtigkeit: {main['humidity']}%")
        print(f"Wetterbeschreibung: {weather['description']}")
        print(f"Windgeschwindigkeit: {wind['speed']} m/s")
    else:
        print("Stadt nicht gefunden.")

# Deine API-Schlüssel und die Stadt
api_key = "8eca9d1bfe0e3f44a51b72c6e4ade2d2"
#city_name = input("Gib den Namen der Stadt ein: ")
# example london
lat = 51.5073219
lon = -0.1276474


# Wetterdaten abrufen
get_weather_data(lat, lon, api_key)
