import os
import re

# Path to the folder with the MP3 files
path = '/home/sakis/youtube/download'

# Path to the destination folder
destination_folder = '/home/sakis/youtube/audio'

# Regular expression for matching the artist and title
pattern = re.compile(r'^(.+?)[^\w\s-]+(.+?)$')

# Iterate over all MP3 files in the folder
for file in os.listdir(path):
    if file.endswith('.mp3'):
        # Save current filename and convert to Unicode
        old_name = file.encode('utf-8').decode('utf-8')

        # Match the artist and title using the regular expression
        match = pattern.match(old_name)
        if match:
            artist = match.group(1).strip()
            title = match.group(2).strip()
        else:
            artist = 'Unknown'
            title = old_name

        # Replace Greek letters in filenames
        artist = artist.replace('Ά', 'A').replace('Έ', 'E')
        title = title.replace('Ά', 'A').replace('Έ', 'E')

        # Remove all other characters in the artist and title
        artist = ''.join(c for c in artist if c.isalnum() or c in [' ', '-', '_'])
        title = ''.join(c for c in title if c.isalnum() or c in [' ', '-', '_'])

        # Remove additional characters from the title
        title = title.split('.')[0]

        # Construct the new file name
        new_name = f'{artist} - {title}.mp3'

        # Create the artist folder if it doesn't exist
        artist_folder = os.path.join(destination_folder, artist)
        if not os.path.exists(artist_folder):
            os.makedirs(artist_folder)

        # Rename the file and move it to the artist folder
        os.rename(os.path.join(path, old_name), os.path.join(artist_folder, new_name))

print('Done!')
