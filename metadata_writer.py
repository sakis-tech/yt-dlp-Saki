import os
import subprocess

# specify the path to the top-level directory containing your mp3 files
top_directory = '/mnt/sakis/test/audio'

# traverse the directory tree to search for all mp3 files
for dirpath, dirnames, filenames in os.walk(top_directory):
    for filename in filenames:
        if filename.endswith(".mp3"):
            filepath = os.path.join(dirpath, filename)
            # extract the artist and title from the file name
            artist, title = filename.split(" - ")[0], filename.split(" - ")[1].replace('.mp3','')
            # use subprocess to run the id3v2 command
            subprocess.run(["id3v2", "-a", artist.strip(), "-t", title.strip(), filepath])
            print("Metadata written to file: ", filename)
print("Metadata written successfully!")
