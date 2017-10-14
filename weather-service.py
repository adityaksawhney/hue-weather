# Service to handle getting the current location and weather.
# Author: Aditya Sawhney
import requests
import json
import config_parser

config = config_parser.parsed()

def get_location():
  url = config['location']['base_url']
  r = requests.get(url)
  j = json.loads(r.text)
  return j

def get_weather(location):
  url = config['weather']['base_url']
  query = {'lat': str(location['latitude']),
            'lon': str(location['longitude']),
            'APPID': config['weather']['apikey']}
  r = requests.get(url, params=query)
  return json.loads(r.text)

def main():
  location = get_location()
  print(get_weather(location))

if __name__ == "__main__":
  main()