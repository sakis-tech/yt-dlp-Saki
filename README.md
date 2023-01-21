# yt-dlp-Saki (Swiss army knife interactive)

## yt_playlist_dl.py

This script is using the python library "yt_dlp" to download a playlist of videos from YouTube in the best audio format available and then converting them to mp3 files. The script then uses regular expressions to extract the artist and title information from the file name and renames the files accordingly. The script also replaces Greek letters in filenames with their English equivalents. Finally, the files are moved to a destination folder.

#### auf deutsch

Dieses Skript verwendet die Python-Bibliothek "yt_dlp", um eine Playlist von Videos von YouTube im besten verfügbaren Audioformat herunterzuladen und diese dann in mp3-Dateien umzuwandeln. Das Skript verwendet anschließend reguläre Ausdrücke, um die Informationen zu Künstler und Titel aus dem Dateinamen zu extrahieren und die Dateien entsprechend umzubenennen. Das Skript ersetzt auch griechische Buchstaben in Dateinamen durch ihre englischen Entsprechungen. Schließlich werden die Dateien in einen Zielordner verschoben.

## metadata-writer.py

This script uses the os and subprocess modules to traverse a specified directory and its subdirectories, searching for all mp3 files. For each mp3 file found, it extracts the artist and title from the file name, and uses the subprocess module to run the id3v2 command, which writes the extracted artist and title as metadata to the mp3 file. The script then prints a message indicating that the metadata has been written to the file. The script will also print "Metadata written successfully!" when all files have been processed.

#### auf deutsch

Dieses Skript verwendet die os- und subprocess-Module, um ein bestimmtes Verzeichnis und seine Unterverzeichnisse zu durchlaufen und nach allen mp3-Dateien zu suchen. Für jede gefundene mp3-Datei extrahiert es den Künstler und den Titel aus dem Dateinamen und verwendet das subprocess-Modul, um den id3v2-Befehl auszuführen, der den extrahierten Künstler und Titel als Metadaten in die mp3-Datei schreibt. Das Skript gibt dann eine Meldung aus, dass die Metadaten in die Datei geschrieben wurden. Das Skript gibt auch "Metadaten erfolgreich geschrieben!" aus, wenn alle Dateien verarbeitet wurden.
