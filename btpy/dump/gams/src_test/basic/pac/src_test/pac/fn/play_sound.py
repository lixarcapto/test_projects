

import pygame
import time
from ..out_deps import Basic

LIMIT_AUDIO = 0.7

@Basic.new_thread
def play_sound(route:str)->None:
    __play_in_main(route)

def __play_in_main(mp3_path):
    volume = LIMIT_AUDIO
    repeats = 1
    # Initialize pygame
    pygame.init()
    # Set up the mixer
    mixer = pygame.mixer
    # Load the MP3 file
    try:
        mixer.music.load(mp3_path)
    except pygame.error as e:
        print(f"Error loading MP3 file: {e}")
        return
    # Set the volume
    mixer.music.set_volume(volume)  
    # Adjust volume as needed
    # Play the MP3 file in a loop
    mixer.music.play(repeats)  
    # -1 for infinite loop
    # Keep the main loop running until 
    # stopped
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mixer.music.stop()
                pygame.quit()
                return
        # Check if the music is stopped 
        # (e.g., due to an error)
        if not mixer.music.get_busy():
            # If stopped, break the loop 
            # and exit
            break
        # Otherwise, continue the loop
        time.sleep(0.1)  
        # Allow other events to be processed