import requests

base_url = "https://wttr.in/"
def get_weather_details(locations: str):
    data = []
    loc = locations.split(",")
    for place in loc:
        place = place.strip()
        res = requests.get(url=f"{base_url}/{place}?format=j1")
        weather_data = res.json()
        data.append(
            {
                "location": place,
                "weather_data": weather_data["current_condition"][0]['temp_C']
            }
        )
    return data