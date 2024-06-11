# Installation

## Docker

Die serverseitige Installation setzt Docker (oder podman) voraus. Empfohlen wird `docker-compose`:

``` 
--8<-- "docker-compose.yml"
```

Falls ein eigener Build bevorzugt wird, dann muss zuerst das Repo geclont werden.

```
git clone https://github.com/{{ extra.github_user }}/{{ extra.github_repo }}
cd {{ extra.github_repo }}
docker-compose build
```

## Konfiguration

Folgende Dateien müssen für den Start des Servers vorhanden sein:

```
├── data
│   ├── config.yml
│   └── license.dat
└── docker-compose.yml

```

### Lizenz

Zum Starten benötigt der Server eine gültige Lizenz aus der Datei `data/license.dat`. Dabei wird eine Anfrage an [https://worldtimeapi.org/api/ip](https://worldtimeapi.org/api/ip) gestellt um das aktuelle Datum abzufragen.

### Konfiguration von Events und Zahlungsinformationen

Um die Events zu konfigurieren, muss die Datei `data/config.yml` angelegt werden.
```
SEPA:
  default:
    Kontoinhaber: "Max Mustermann"
    IBAN: "DEXXXXXXXXXXXXXXXXX"
    BIC: "YYYYYYYY"

  peter:
    Kontoinhaber: "Peter Pan"
    IBAN: "DEZZZZZZZZZZZZZZZZZ"
    BIC: "KKKKKKKKKKKKK"

LINKS:
  05a: default
  07c: peter

EVENTS:
  - name: 'Event1'
    betrag: 12

  - name: 'Event2'
    link: peter

  - name: 'Event3'
    link: peter
    code: mycode

  - name: 'Event4'
    link: peter
    code: mycode
    whitelist:
      - 05a
```
In diesem Beispiel, bekommen bei Event1 die Klassen 05a und 05b die Zahlungsinformationen von `default` angezeigt, die Klasse 07c die von `peter`. In jedem Fall ist der Überweisungsbetrag auf 12€ fixiert. Event2 bekommt für jede Klasse die Zahlungsinformationen von `peter` angezeigt. Event3 wird nur angezeigt, wenn der URL Parameter `code=mycode` mit im Link enthalten ist. Event4 ist so definiert wie Event3, nur dass Ergebnisse nur für die Klasse 05a angezeigt werden. 


## Hinzufügen von Usern und Klassen

Siehe [API-Dokumentation](api.md).