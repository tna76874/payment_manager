# Datenschutzerklärung

Der Schutz personenbezogener Daten ist ein wichtiges Anliegen im Design dieses Dienstes. In dieser Datenschutzerklärung wird über die Art, den Umfang und den Zweck der Erhebung, Verarbeitung und Speicherung von Daten im System informiert.

## 1. Arten der gespeicherten Daten

### 1.1 Lesbar gespeicherte Informationen aus config.yml
Bestimmte Konfigurationsinformationen werden in einer Datei `config.yml` und einer Datenbank `datab.db` gespeichert. Diese Informationen sind für den reibungslosen Betrieb des Systems erforderlich und enthalten keine personenbezogenen Daten.

### 1.2 Lesbar gespeicherte Daten in der Datenbank
Eine Auflistung der Klassen wird in der Datenbank gespeichert. Diese Informationen sind wichtig für die Verwaltung und Bereitstellung der Dienste.

### 1.3 Gehashte gespeicherte Daten
- **Kombination aus Anmeldename, Klasse und Name:** Diese Daten werden gehasht gespeichert, um die Privatsphäre zu schützen und sicherzustellen, dass personenbezogene Daten nicht im Klartext vorliegen.
- **IP-Adressen von Suchanfragen der letzten 7 Tage:** Auch diese Daten werden gehasht gespeichert, um die Anonymität zu gewährleisten und gleichzeitig die Nutzung der Dienste überwachen und analysieren zu können. Es wird die gehashte IP-Adresse der Anfrage gespeichert und der Rückgabestatus (1/0) der Suchanfrage.

## 2. Zugriffskontrollen

### 2.1 Ausbremsen von Brute-Force Anfragen
Mechanismen werden eingesetzt, um Brute-Force-Angriffe zu verhindern. Dies umfasst unter anderem die Begrenzung der Anzahl von Anfrageversuchen innerhalb von sieben Tagen.

### 2.2 Begrenzung der gültigen Suchanfragen pro Tag
Um Missbrauch zu verhindern und die Dienstqualität sicherzustellen, wird die Anzahl der Suchanfragen pro Tag pro Nutzer begrenzt. Diese Maßnahme hilft, die Systemleistung aufrechtzuerhalten und einen fairen Zugang zu den Diensten zu gewährleisten.

## 3. Verarbeitung von Nutzerinformationen

Die Informationen aus dem Formularfeld werden auf dem Server mit den entsprechenden Hash-Informationen in der Datenbank abgeglichen. Es erfolgt keine dauerhafte Speicherung auf dem Server, sondern lediglich eine Verarbeitung der Daten.

## 4. Ihre Rechte
Nutzer haben das Recht, jederzeit Auskunft über die gespeicherten personenbezogenen Daten zu erhalten sowie das Recht auf Berichtigung, Löschung und Einschränkung der Verarbeitung dieser Daten. Bei Fragen oder Anliegen bezüglich des Datenschutzes können sich Nutzer jederzeit an den Betreiber wenden.

## 5. Kontakt
Bei Fragen zur Erhebung, Verarbeitung oder Nutzung personenbezogener Daten, zur Auskunftserteilung, Berichtigung, Sperrung oder Löschung von Daten sowie zum Widerruf erteilter Einwilligungen wenden sich Nutzer bitte direkt an den jeweiligen Betreiber des Dienstes.

Für allgemeine Fragen und Informationen können Nutzer die Dateien im GitHub Repository einsehen:

[GitHub Repository](https://github.com/{{ extra.github_user }}/{{ extra.github_repo }})

Diese Datenschutzerklärung wird regelmäßig überprüft und bei Bedarf aktualisiert. Änderungen werden auf der Website des Betreibers veröffentlicht, um Nutzer stets über den Datenschutz zu informieren.

**Letzte Aktualisierung:**  {{ extra.build_doc_date }}

**Build ID:**  {{ extra.build_hash }}

**Build Datum:**  {{ extra.build_date }}
