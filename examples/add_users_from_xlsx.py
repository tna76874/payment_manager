#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
example: add users from excel file
"""

import pandas as pd
import requests
import json

# API-Schlüssel
apikey = "test"

# URL des API-Endpunkts
url = 'http://localhost:5000/api/addUsers'

# Daten aus der Excel-Datei laden
data = pd.read_excel('example_list.xlsx')

# Konvertiere die Daten in das erforderliche JSON-Format für die Anfrage
data_json = data.to_dict(orient='records')

# Header mit dem API-Schlüssel
headers = {
    'Authorization': apikey,
    'Content-Type': 'application/json'
}

# Senden der POST-Anfrage an den API-Endpunkt
response = requests.post(url, headers=headers, json=data_json)

# Ausgabe der Antwort
print(response.json())
