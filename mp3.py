import PySimpleGUI as sg
import os
from play import get_diretorios, play_sound, pause_sound, unpause, stop_sound, is_sound_playing

sg.theme('DarkPurple5')
nome_da_musica = [[sg.Text(text='press play..', justification = 'center', background_color = 'blue',
             text_color= 'black', size = (200.0), font = 'tahoma', key = 'song_name')]] 



# 1 criar um player de musica
    #1.1 criar uma playlist
    #1.2 fazer a play list tocar
    #1.3 transportar a playlist para a aba interativa

# 2 criar uma aba para aparecer o player
    #2.1 criar uma aba grande
    #2.2 colocar uma iamgem da banda no meio
    #2.3 criar botões play e pause

# 3 fazer a aba dar play e pause na musica 
    # Fazer o botão dar play
    #fazer o botão dar pause

    
