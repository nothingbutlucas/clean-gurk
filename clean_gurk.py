#!/usr/bin/env python3

import os
import sys
import json

# Capture user home variable
home = os.path.expanduser("~")
gurk_dir = home + "/.local/share/gurk"

# Open the json gurk file and replace all the messages with an empty list

with open(gurk_dir + '/gurk.data.json', 'r') as json_file:
    data = json.load(json_file)
    items = data['channels']['items']
    for message in items:
        message['messages'] = []

with open(gurk_dir + '/gurk.test.json', 'w') as file:
    json.dump(data, file)

# Erase the signal-{ACTUAL_YEAR}* files on the gurk directory

capture_actual_year = str(os.popen("date +%Y").read())

for file in os.listdir(gurk_dir):
    if file.startswith("signal-" + capture_actual_year) or file.startswith("signal-" + str(int(capture_actual_year) - 1)):
        os.remove(gurk_dir + "/" + file)

sys.exit(0)
