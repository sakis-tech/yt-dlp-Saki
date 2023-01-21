# yt-dlp-Saki (Swiss army knife interactive)

Dieses Skript durchläuft alle MP3-Dateien in einem Ordner und benennt sie um, indem es Künstler- und Titelinformationen aus dem Dateinamen extrahiert und dann den Künstlernamen und den Titel in einem neuen Dateinamen kombiniert. Der neue Dateiname wird dann in einen Unterordner mit dem Namen des Künstlers verschoben.

Um das Skript anzupassen, könnten einige Dinge in Betracht gezogen werden:

Wenn Sie die Quell- und Zielordner ändern möchten, in denen sich die MP3-Dateien befinden, können Sie diese in den Variablen `path` und `destination_folder` anpassen.

Wenn Sie das Muster ändern möchten, das verwendet wird, um Künstler- und Titelinformationen aus dem Dateinamen zu extrahieren, können Sie dies in der regulären Ausdrucksvariable `pattern` tun.

Wenn Sie andere Zeichen ersetzen möchten, die möglicherweise in den Dateinamen enthalten sind, können Sie dies in den Zeilen mit den Aufrufen von `replace` tun.

Wenn Sie bestimmte Zeichen aus dem Künstler- und Titelnamen entfernen möchten, können Sie dies in den Zeilen mit den Aufrufen von `join` tun.

# metadata-writer.py

This script uses the os and subprocess modules to traverse a specified directory and its subdirectories, searching for all mp3 files. For each mp3 file found, it extracts the artist and title from the file name, and uses the subprocess module to run the id3v2 command, which writes the extracted artist and title as metadata to the mp3 file. The script then prints a message indicating that the metadata has been written to the file. The script will also print "Metadata written successfully!" when all files have been processed.

### auf deutsch ###

Dieses Skript verwendet die os- und subprocess-Module, um ein bestimmtes Verzeichnis und seine Unterverzeichnisse zu durchlaufen und nach allen mp3-Dateien zu suchen. Für jede gefundene mp3-Datei extrahiert es den Künstler und den Titel aus dem Dateinamen und verwendet das subprocess-Modul, um den id3v2-Befehl auszuführen, der den extrahierten Künstler und Titel als Metadaten in die mp3-Datei schreibt. Das Skript gibt dann eine Meldung aus, dass die Metadaten in die Datei geschrieben wurden. Das Skript gibt auch "Metadaten erfolgreich geschrieben!" aus, wenn alle Dateien verarbeitet wurden.
