# mp3-Dateien-umbennen-und-verschieben

Dieses Skript durchläuft alle MP3-Dateien in einem Ordner und benennt sie um, indem es Künstler- und Titelinformationen aus dem Dateinamen extrahiert und dann den Künstlernamen und den Titel in einem neuen Dateinamen kombiniert. Der neue Dateiname wird dann in einen Unterordner mit dem Namen des Künstlers verschoben.

Um das Skript anzupassen, könnten einige Dinge in Betracht gezogen werden:

    Wenn Sie die Quell- und Zielordner ändern möchten, in denen sich die MP3-Dateien befinden, können Sie diese in den Variablen path und destination_folder anpassen.

    Wenn Sie das Muster ändern möchten, das verwendet wird, um Künstler- und Titelinformationen aus dem Dateinamen zu extrahieren, können Sie dies in der regulären Ausdrucksvariable pattern tun.

    Wenn Sie andere Zeichen ersetzen möchten, die möglicherweise in den Dateinamen enthalten sind, können Sie dies in den Zeilen mit den Aufrufen von replace tun.

    Wenn Sie bestimmte Zeichen aus dem Künstler- und Titelnamen entfernen möchten, können Sie dies in den Zeilen mit den Aufrufen von join tun.
