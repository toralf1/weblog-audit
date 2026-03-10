# Web Log Audit

Ein kleines Python-Skript, das Webserver-Logs analysiert und grundlegende
Auffälligkeiten sichtbar macht (z. B. viele Requests von einer IP, viele 404-Fehler).

## Use-Case

Dieses Skript unterstützt bei der sicherheitsrelevanten Analyse von Webserver-Logdateien,
um typische Angriffs- und Scan-Muster zu erkennen. Dazu gehören z. B. ungewöhnlich viele
Anfragen von einzelnen IP-Adressen, gehäufte 4xx-/5xx-Statuscodes oder Zugriffe auf
potenziell sensible Pfade wie Login-Seiten oder Admin-Bereiche. Das Tool kann als Grundlage
für erste Auswertungen im Rahmen von Incident-Response, Schwachstellen-Scans oder
regelmäßigen Sicherheitsüberprüfungen genutzt werden.

## Hinweis zu den Beispieldaten

Die mitgelieferte Datei `example_access.log` enthält ausschließlich synthetische, zu
Demonstrationszwecken erzeugte Logeinträge. Es werden keine echten IP-Adressen, Hostnamen
oder sonstige personenbezogene bzw. kundenbezogene Daten verarbeitet oder veröffentlicht.

## Verwendung

1. Python 3 installieren.
2. Repository lokal klonen oder Dateien herunterladen.
3. Im Projektordner das Skript ausführen:

```bash
python log_audit.py
