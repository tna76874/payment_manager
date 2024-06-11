#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
example: add user from list
"""

import requests
import json

# API-Schlüssel
apikey = "test"

# URL des API-Endpunkts
url = 'http://localhost:5000/api/addUsers'

# Beispiel JSON-Daten für die Anfrage
data =  [
        {"klasse": "10a", "sid": "doej1", "nachname": "Doe", "vorname": "John"},
        {"klasse": "10b", "sid": "smithj3", "nachname": "Smith", "vorname": "Jane"},
        ]

# Header mit dem API-Schlüssel
headers = {
    'Authorization': apikey,
    'Content-Type': 'application/json'
}

# Senden der POST-Anfrage an den API-Endpunkt
response = requests.post(url, headers=headers, json=data)

# Ausgabe der Antwort
print(response.json())
