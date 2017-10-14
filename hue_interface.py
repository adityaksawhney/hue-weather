import beautifulhue
import config_parser
import requests
import json

config = config_parser.parsed()

def get_bridge_ip():
  url = config['hue']['bridge']['ip_url']
  r = requests.get(url)
  bridges = json.loads(r.text)
  bridge = bridges[0] if bridges else None
  if len(bridges) == 0:
    print("No Hue Bridges found. Please make sure you are on the same network as your Bridge.")
    exit()
  elif len(bridges) > 1:
    bridge = handle_multiple_bridges(bridges)
  return bridge['internalipaddress']

def handle_multiple_bridges(bridges):
  while True:
      print("Multiple Hue Bridges found. Please select the one you would like to connect to:")
      for i, b in enumerate(bridges):
        print("[" + str(i) + "]: Bridge ID: " + b['id'] + "  Internal IP: " + b['internalipaddress'])
      choice = int(raw_input())
      if choice >= 0 and choice < len(bridges):
        return bridges[choice]
      else:
        print("Please enter a number between 0 and " + str(len(bridges) - 1))

def main():
  get_bridge_ip
  
if __name__ == "__main__":
  main()
