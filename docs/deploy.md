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

Zum Starten benötigt der Server eine gültige Lizenz aus der Datei `data/license.dat`. Dabei wird eine Anfrage an [https://worldtimeapi.org](https://worldtimeapi.org) oder [https://timeapi.io](https://timeapi.io) gestellt um das aktuelle Datum abzufragen.

### Konfiguration von Events und Zahlungsinformationen <a id="event-config"></a>

Um die Events zu konfigurieren, muss die Datei `data/config.yml` angelegt werden.
```
INFO:
    impressum: https://meinewebsite.de

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

Wenn die Datei `data/config.yml` geändert wird, dann muss der Server nicht neugestartet werden - die Konfiguration wird dynamisch eingelesen. 

### Erforderlichkeit eines gültigen SSL/TLS-Zertifikats

Für die sichere Nutzung unseres Dienstes ist die Beschaffung eines gültigen SSL/TLS-Zertifikats unerlässlich. Ohne eine HTTPS-Verbindung ist die Nutzung des Dienstes nicht möglich. Wir empfehlen dringend, sicherzustellen, dass das Zertifikat aktuell ist und den geltenden Sicherheitsstandards entspricht.

### Proxy-Konfiguration

Die Proxy-Header müssen richtig konfiguriert sein, damit der Dienst die Verbindung nicht als "unsicher" ablehnt und die Zugriffseinschränkung über die IP-Adressen funktioniert. Im Folgenden dazu Beispielkonfigurationen.

Nginx:
```
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
```

Traefik:
```
additionalMiddlewares:
  forwardheaders:
    headers:
      customRequestHeaders:
        X-Forwarded-Proto: "https"
        X-Real-IP: "{client_ip}"
        X-Forwarded-For: "{client_ip}"
```

### Cloudflare Turnstile

Optional kann ein Schutz mit Turnstile eingerichtet werden um automatisierten Anfragen auf das Formular vorzubeugen (empfohlen). Dazu wird ein Konto bei cloudflare benötigt und Turnstile muss dort für die entsprechende Domain konfiguriert sein. Danach in `docker-compose.yml` die folgenden Environment-Variablen hinzufügen:

```
SALDOMANAGER_TURNSTILE_SECRET=XXXXX
SALDOMANAGER_TURNSTILE_PUBLIC_KEY=YYYYY
```

### Start und Update

Der Container wird gestartet mit:

```
docker-compose up -d
```

Um den Dienst zu updaten muss das aktuelle `latest` Image gepulled werden. Danach wird der Container neugestartet.

```
docker-compose pull && docker-compose down && docker-compose up -d
```

Um die Logs des laufenden Containers anzuzeigen:

```
docker-compose logs -f
```

## Hinzufügen von Usern und Klassen

Siehe [API-Dokumentation](api.md).