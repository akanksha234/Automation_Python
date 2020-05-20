import json
from pathlib import Path

json_file_path = Path('../Files/purchase_14781239.json')

with open(json_file_path) as json_file:
    message_json  = json.load(json_file)

print(message_json)
