import requests
import yaml

secrets_file_path = 'secrets.yaml'
with open(secrets_file_path, 'r') as file:
    secrets = yaml.safe_load(file)

BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json'
API_KEY = secrets['google_api_key']
START = secrets['start']
DESTINATION = secrets['destination']

mode = 'transit'

def get_route(url, params):
    response = requests.get(url, params=params)
    print(response.json())

params = {
    'origin': START,
    'destination': DESTINATION,
    'mode': mode,
    'key': API_KEY
}

get_route(BASE_URL, params)