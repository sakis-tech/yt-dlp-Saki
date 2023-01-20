import os
import re
import time

# Path to the folder with the MP3 files
path = "/mnt/sakis/download"

# Path to the destination folder
destination_folder = "/mnt/sakis/audio"

# Regular expression for matching the artist
artist_pattern = re.compile(r'^(.+?) - ')

# Regular expression for matching the title
title_pattern = re.compile(r'^.+? - (.*?)[^\w\s-]*\.mp3$')

# Iterate over all MP3 files in the folder
for file in os.listdir(path):
    if file.endswith('.mp3'):
        # Save current filename and convert to Unicode
        old_name = file.encode('utf-8').decode('utf-8')

        # Match the artist using the artist regular expression
        artist_match = artist_pattern.match(old_name)
        if artist_match:
            artist = artist_match.group(1).strip()
        else:
            artist = 'Unknown'

        # Match the title using the title regular expression
        title_match = title_pattern.match(old_name)
        if title_match:
            title = title_match.group(1).strip()
        else:
            title = old_name

        # Replace Greek letters in filenames
        artist = (
            artist.replace("Ά", "A")
            .replace("Έ", "E")
            .replace("Ή", "H")
            .replace("Ί", "I")
            .replace("Ό", "O")
            .replace("Ύ", "Y")
            .replace("Ώ", "W")
            .replace("ΐ", "I")
            .replace("Α", "A")
            .replace("Β", "B")
            .replace("Γ", "G")
            .replace("Δ", "D")
            .replace("Ε", "E")
            .replace("Ζ", "Z")
            .replace("Η", "H")
            .replace("Θ", "TH")
            .replace("Ι", "I")
            .replace("Κ", "K")
            .replace("Λ", "L")
            .replace("Μ", "M")
            .replace("Ν", "N")
            .replace("Ξ", "X")
            .replace("Ο", "O")
            .replace("Π", "P")
            .replace("Ρ", "R")
            .replace("Σ", "S")
            .replace("Τ", "T")
            .replace("Υ", "Y")
            .replace("Φ", "F")
            .replace("Χ", "X")
            .replace("Ψ", "PS")
            .replace("Ω", "O")
            .replace("ά", "a")
            .replace("έ", "e")
            .replace("ή", "i")
            .replace("ί", "i")
            .replace("ό", "o")
            .replace("ύ", "y")
            .replace("ώ", "w")
            .replace("ϊ", "i")
            .replace("ϋ", "u")
            .replace("ό", "o")
            .replace("α", "a")
            .replace("β", "b")
            .replace("γ", "g")
            .replace("δ", "d")
            .replace("ε", "e")
            .replace("ζ", "z")
            .replace("η", "i")
            .replace("θ", "th")
            .replace("ι", "i")
            .replace("κ", "k")
            .replace("λ", "l")
            .replace("μ", "m")
            .replace("ν", "n")
            .replace("ξ", "x")
            .replace("ο", "o")
            .replace("π", "p")
            .replace("ρ", "r")
            .replace("ς", "s")
            .replace("σ", "s")
            .replace("τ", "t")
            .replace("υ", "y")
            .replace("φ", "f")
            .replace("χ", "x")
            .replace("ψ", "ps")
            .replace("ω", "o")
        )
        title = (
            title.replace("Ά", "A")
            .replace("Έ", "E")
            .replace("Ή", "H")
            .replace("Ί", "I")
            .replace("Ό", "O")
            .replace("Ύ", "Y")
            .replace("Ώ", "W")
            .replace("ΐ", "I")
            .replace("Α", "A")
            .replace("Β", "B")
            .replace("Γ", "G")
            .replace("Δ", "D")
            .replace("Ε", "E")
            .replace("Ζ", "Z")
            .replace("Η", "H")
            .replace("Θ", "TH")
            .replace("Ι", "I")
            .replace("Κ", "K")
            .replace("Λ", "L")
            .replace("Μ", "M")
            .replace("Ν", "N")
            .replace("Ξ", "X")
            .replace("Ο", "O")
            .replace("Π", "P")
            .replace("Ρ", "R")
            .replace("Σ", "S")
            .replace("Τ", "T")
            .replace("Υ", "Y")
            .replace("Φ", "F")
            .replace("Χ", "X")
            .replace("Ψ", "PS")
            .replace("Ω", "O")
            .replace("ά", "a")
            .replace("έ", "e")
            .replace("ή", "i")
            .replace("ί", "i")
            .replace("ό", "o")
            .replace("ύ", "y")
            .replace("ώ", "w")
            .replace("ϊ", "i")
            .replace("ϋ", "u")
            .replace("ό", "o")
            .replace("α", "a")
            .replace("β", "b")
            .replace("γ", "g")
            .replace("δ", "d")
            .replace("ε", "e")
            .replace("ζ", "z")
            .replace("η", "i")
            .replace("θ", "th")
            .replace("ι", "i")
            .replace("κ", "k")
            .replace("λ", "l")
            .replace("μ", "m")
            .replace("ν", "n")
            .replace("ξ", "x")
            .replace("ο", "o")
            .replace("π", "p")
            .replace("ρ", "r")
            .replace("ς", "s")
            .replace("σ", "s")
            .replace("τ", "t")
            .replace("υ", "y")
            .replace("φ", "f")
            .replace("χ", "x")
            .replace("ψ", "ps")
            .replace("ω", "o")
        )

        # Construct the new file name
        new_name = f'{artist} - {title}.mp3'

        # Create the artist folder if it doesn't exist
        artist_folder = os.path.join(destination_folder, artist)
        if not os.path.exists(artist_folder):
            os.makedirs(artist_folder)

        # Rename the file and move it to the artist folder
        os.rename(os.path.join(path, old_name), os.path.join(artist_folder, new_name))

print('Done!')
