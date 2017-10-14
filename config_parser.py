import json

def parsed():
  with open('config.json', 'r') as config_file:
    return json.load(config_file)