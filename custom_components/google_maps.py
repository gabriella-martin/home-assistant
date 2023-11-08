import requests
import yaml

secrets_file_path = 'secrets.yaml'
with open(secrets_file_path, 'r') as file:
    secrets = yaml.safe_load(file)

BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json'
API_KEY = secrets['google_api_key']
START = secrets['start']
DESTINATION = secrets['destination']

