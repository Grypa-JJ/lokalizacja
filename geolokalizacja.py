import pandas as pd
import googlemaps
from time import sleep

# Wczytanie danych z pliku CSV ('adresy.csv')
df = pd.read_csv('adresy.csv')

# Inicjalizacja klienta Google Maps API
gmaps = googlemaps.Client(key='AIzaSyDdHPYiN-gRAKUogs9RdzxQ-jY3CFl8vH8')

# Funkcja do wyciągania współrzędnych
def get_coordinates(address):
    try:
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            return None, None
    except Exception as e:
        print(f"Błąd: {e}")
        return None, None

# Dodanie nowych kolumn do DataFrame
df['latitude'], df['longitude'] = zip(*df['address'].apply(get_coordinates))

# Zapisanie wyników do nowego pliku CSV
df.to_csv('adresy_z_wspolrzednymi.csv', index=False)

print("Geolokalizacja zakończona. Wyniki zapisane w 'adresy_z_wspolrzednymi.csv'")
