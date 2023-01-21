# yt-dlp-Saki (Swiss army knife interactive)

## yt_playlist_dl.py

This script is using the python library `yt_dlp` to download a playlist of videos from YouTube in the best audio format available and then converting them to mp3 files. The script then uses regular expressions to extract the artist and title information from the file name and renames the files accordingly. The script also replaces Greek letters in filenames with their English equivalents. Finally, the files are moved to a destination folder.

<hr />

Dieses Skript verwendet die Python-Bibliothek `yt_dlp`, um eine Playlist von Videos von YouTube im besten verfügbaren Audioformat herunterzuladen und diese dann in mp3-Dateien umzuwandeln. Das Skript verwendet anschließend reguläre Ausdrücke, um die Informationen zu Künstler und Titel aus dem Dateinamen zu extrahieren und die Dateien entsprechend umzubenennen. Das Skript ersetzt auch griechische Buchstaben in Dateinamen durch ihre englischen Entsprechungen. Schließlich werden die Dateien in einen Zielordner verschoben.

## metadata-writer.py

This script uses the `os` and `subprocess` modules to traverse a specified directory and its subdirectories, searching for all mp3 files. For each mp3 file found, it extracts the artist and title from the file name, and uses the `subprocess module` to run the `id3v2` command, which writes the extracted artist and title as metadata to the mp3 file. The script then prints a message indicating that the metadata has been written to the file. The script will also print `Metadata written successfully!` when all files have been processed.

<hr />

Dieses Skript verwendet die `os-` und `subprocess-Module`, um ein bestimmtes Verzeichnis und seine Unterverzeichnisse zu durchlaufen und nach allen mp3-Dateien zu suchen. Für jede gefundene mp3-Datei extrahiert es den Künstler und den Titel aus dem Dateinamen und verwendet das `subprocess-Modul`, um den `id3v2-Befehl` auszuführen, der den extrahierten Künstler und Titel als Metadaten in die mp3-Datei schreibt. Das Skript gibt dann eine Meldung aus, dass die Metadaten in die Datei geschrieben wurden. Das Skript gibt auch `Metadaten erfolgreich geschrieben!` aus, wenn alle Dateien verarbeitet wurden.

## how to use `yt_playlist_dl.py`

To use this script, you need to have `Python` installed on your computer, as well as the `yt_dlp` library. You can install the library by running the command `pip install yt_dlp` in your command prompt or terminal.

Once you have Python and the library installed, you can run the script by executing the command `python3 yt_playlist_dl.py`.

When the script starts running, it will prompt you to enter the playlist URL. You can then enter the URL of the YouTube playlist that you want to download. The script will then download the videos from the playlist and convert them to MP3 files. The files will then be moved to the `destination folder` and be renamed according to the `artist` and `title` information extracted from the file name.

It's important to note that this script will download all videos in the playlist, so you should be careful with the playlist you're passing to the script if it has a lot of videos.
It's also advisable to check if the script has the permission to access the specified folders and files.

## how to use `metadata-writer.py`

To use this script, you will need to have `Python` and the `os` and `subprocess modules` installed on your system. You can check if you have Python installed by running the command `python --version` in the command line.

You will also need to have the `id3v2` command-line tool installed on your system. This tool is used to write metadata to mp3 files, and can be installed using the package manager of your operating system.

Once you have the necessary dependencies installed, you can run the script by navigating to the directory where the script is saved in the command line and running the command `python3 metadata-writer.py`.

You will also need to `specify` the path to the top-level directory containing your mp3 files in the script. Make sure the path is correct before running the script, to ensure that the script is able to locate and process the correct files.

It's also a good idea to make a backup of your files before running the script, in case something goes wrong or you need to revert to the original metadata.
