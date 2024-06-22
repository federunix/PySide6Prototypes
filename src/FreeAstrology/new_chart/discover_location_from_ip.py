import requests

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        data = response.json()
        return data["ip"]
    except requests.exceptions.RequestException as e:
        return None

def get_ip_location(ip_address):
    api_url = f"http://ipapi.co/{ip_address}/json/"
    try:
        response = requests.get(api_url)
        data = response.json()
        if response.status_code == 200:
            return {
                "ip": data.get("ip"),
                "city": data.get("city"),
                "region": data.get("region"),
                "country": data.get("country_name"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "timezone": data.get("timezone")
            }
        else:
            return {"error": data.get("error", "Unable to fetch data")}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Ottenere l'indirizzo IP pubblico del computer
public_ip = get_public_ip()
if public_ip:
    # Ottenere la geolocalizzazione dell'indirizzo IP pubblico
    location = get_ip_location(public_ip)
    print(location)
else:
    print("Unable to retrieve public IP address")
