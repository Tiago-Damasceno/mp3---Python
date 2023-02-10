import os
from pygame import mixer
mixer.init

def get_diretorios(directory):
    directories = []
    for (root, dir, files) in os.walk(directory):
        for file in files:
            directories.append(root + os.sep + file)

    return directories



def play_sound(sound_path):
    mixer.music.load(sound_path)
    mixer.music.play()

def stop_sound():
    mixer.music.stop

def pause_sound():
    mixer.music.pause()

def unpause ():
    mixer.music.unpause()

def is_sound_playing():
    if mixer.music.get_busy() == True:
        return True
    return False