Die Zugangsdaten sind in vier separate Variablen aufgteilt:
 consumer_key
 consumer_secret
 access_token
 access_token_secret


Sie können diese Informationen aus der Twitch-OAuth-Anmeldeseite erhalten, indem Sie die Anwendung registrieren und dann den generierten OAuth-Schlüssel verwenden. Die OAuth-Token bestehen normalerweise aus einer Zeichenfolge mit Zahlen und Buchstaben, nicht in der Form oauth:token.


Sie können Ihre Twitch-Anmeldeinformationen wie folgt aufteilen:



Gehen Sie zu https://dev.twitch.tv/console/apps und registrieren Sie eine neue Anwendung

Wählen Sie die Registerkarte "OAuth" und kopieren Sie den Client-ID-Wert (dies ist Ihr consumer_key)

Klicken Sie auf den Link "New Secret", um ein neues consumer_secret zu erstellen

Authentifizieren Sie sich bei Twitch, indem Sie die Anwendung verwenden und autorisieren

Nachdem Sie erfolgreich authentifiziert haben, erhalten Sie einen OAuth-Code (dies ist Ihr access_token)

Verwenden Sie den OAuth-Code und das client_id, um eine neue Anwendung zu erstellen und die access_token_secret abzurufen

Verwenden Sie diese vier Variablen im obigen Code, um sich bei Twitch Chat anzumelden


Sobald Sie Ihre Twitch-Anmeldeinformationen haben, können Sie den Bot mit dem obigen Code auf Ihrem Kanal ausführen und verschiedene Befehle hinzufügen, indem Sie die Funktion on_message() anpassen.
