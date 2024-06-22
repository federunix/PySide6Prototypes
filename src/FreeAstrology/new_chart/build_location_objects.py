import csv
import json
from geopy.geocoders import Nominatim
import time

# Inizializza il geolocalizzatore Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

def get_location_info(city, country):
    try:
        # Utilizza il nome della città e il paese per ottenere informazioni dettagliate
        location = geolocator.geocode(f"{city}, {country}")
        if location:
            # Ottiene ulteriori dettagli come provincia, regione, e codice postale
            address = location.raw['address']
            province = address.get('state', '')
            region = address.get('region', '')
            postal_code = address.get('postcode', '')
            return province, region, postal_code
        else:
            return None, None, None
    except Exception as e:
        print(f"Errore: {e}")
        return None, None, None

# Leggi il file CSV e ottieni ulteriori informazioni
with open('worldcities.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    results = []
    for row in reader:
        city = row['city_ascii']
        country = row['country']
        province, region, postal_code = get_location_info(city, country)
        result = row.copy()  # Copia tutti i campi del CSV
        result.update({
            'provincia': province,
            'regione': region,
            'codice_postale': postal_code
        })
        results.append(result)
        # Aggiungi un ritardo per evitare di sovraccaricare il servizio di geocoding
        time.sleep(1)

    # Stampa i risultati (opzionale)
    for result in results:
        print(result)

# Salva i risultati in un file JSON
with open('extended_worldcities.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(results, jsonfile, ensure_ascii=False, indent=4)
