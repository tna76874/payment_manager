#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
example: delete all userdata
"""

import requests

# API-Schlüssel
apikey = "test"

# URL des API-Endpunkts
url = 'http://localhost:5000/api/deleteUsers'

# Header mit dem API-Schlüssel
headers = {
    'Authorization': apikey
}

# Senden der DELETE-Anfrage an den API-Endpunkt
response = requests.delete(url, headers=headers)

# Überprüfen des Statuscodes der Antwort
if response.status_code == 200:
    print("Alle Benutzer erfolgreich gelöscht")
else:
    print("Fehler beim Löschen aller Benutzer. Statuscode:", response.status_code)