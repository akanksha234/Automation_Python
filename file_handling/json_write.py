import json
from pathlib import Path

#data to be written to the json file
turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}
file_to_write_to = Path('../Files/json_file_write.json')

with open(file_to_write_to, 'w') as json_file:
    json.dump(turn_to_json, json_file)



