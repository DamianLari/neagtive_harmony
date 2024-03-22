import pygame
import time

def play_midi(file_path):
    # Initialisation de pygame
    pygame.init()
    
    # Initialisation du mixer
    pygame.mixer.init()
    
    # Chargement du fichier MIDI
    pygame.mixer.music.load(file_path)
    
    # Jouer le fichier MIDI
    pygame.mixer.music.play()

    # Attendre la fin de la musique
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Chemin vers votre fichier MIDI
file_path = 'inverted_song.mid'

# Jouer le fichier MIDI
play_midi(file_path)
