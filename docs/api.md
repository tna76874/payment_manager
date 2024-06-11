# API-Dokumentation

Dokumentationen für die API-Endpoints `AddUsers` und `DeleteUsers`.

#### AddUsers Endpoint

- **Beschreibung:** Fügt eine Liste von Benutzern zur Datenbank hinzu.
  
- **Authorization:** Der Anfrage muss ein 'Authorization' Header mit einem gültigen API-Schlüssel enthalten.

- **Anfrage JSON-Format:**

```
{
    "sid": [
        {
            "klasse": "<Klassenname>",
            "sid": "<Schüler-ID>",
            "nachname": "<Nachname>",
            "vorname": "<Vorname>"
        },
        ...
    ]
}
```

- **Antworten:**

    - 201: {"message": "Benutzer erfolgreich hinzugefügt"} - wenn die Benutzer erfolgreich hinzugefügt wurden.
    - 401: {"error": "Unberechtigt"} - wenn der bereitgestellte API-Schlüssel ungültig ist.
    - 500: {"error": "<Fehlermeldung>"} - bei einem internen Serverfehler.

- **Rückgabe:** Eine JSON-Antwort mit einer Nachricht, die das Ergebnis der Operation angibt, und einem entsprechenden HTTP-Statuscode.

- **Beispiele:**

```
curl -X POST -H "Authorization: <API-Schlüssel>" -H "Content-Type: application/json" -d '[
        {"klasse": "10a", "sid": "doej1", "nachname": "Doe", "vorname": "John"},
        {"klasse": "10b", "sid": "smithj3", "nachname": "Smith", "vorname": "Jane"}
    ]' http://<Server>/api/addUsers
```

``` 
--8<-- "examples/add_users.py"
```

``` 
--8<-- "examples/add_users_from_xlsx.py"
```

#### DeleteUsers Endpoint

- **Beschreibung:** Endpoint zum Löschen aller Benutzer und aller Klassen.

- **Authorization:** Der Anfrage muss ein 'Authorization' Header mit einem gültigen API-Schlüssel enthalten.

- **Antworten:**
    - 200: {"message": "Alle Benutzer und Klassen erfolgreich gelöscht"} - wenn die Löschung erfolgreich ist.
    - 401: {"error": "Unberechtigt"} - wenn der bereitgestellte API-Schlüssel ungültig ist.
    - 500: {"error": "<Fehlermeldung>"} - bei einem internen Serverfehler.

- **Hinweis:** Dieser Endpunkt löscht alle Benutzer und Klassen aus der Datenbank. Verwenden Sie ihn mit Vorsicht, da diese Aktion nicht rückgängig gemacht werden kann.

- **Beispiel:**

    ```
    curl -X DELETE -H "Authorization: <API-Schlüssel>" http://<Server>/api/deleteUsers
    ```

``` 
--8<-- "examples/delete_users.py"
```