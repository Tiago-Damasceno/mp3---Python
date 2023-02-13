import os
from pygame import mixer
mixer.init()

# 1 criar um player de musica
    #1.1 criar uma playlist
    #1.2 fazer a play list tocar
    #1.3 transportar a playlist para a aba interativa

def get_files_inside_directory_not_recursive(songs):
    directories = []
    for (root, directories, files) in os.walk(songs):
        for file in files:
            directories.append(root + os.sep + file)

    return directories



def play_sound(sound_path):
    mixer.music.load(sound_path)
    mixer.music.play()

def stop_sounds():
    mixer.music.stop

def pause_sounds():
    mixer.music.pause()

def unpause ():
    mixer.music.unpause()

def is_sound_playing():
    if mixer.music.get_busy() == True:
        return True
    return False