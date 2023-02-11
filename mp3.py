import PySimpleGUI as sg
import os
from play import get_diretorios, play_sound, pause_sound, unpause, stop_sound, is_sound_playing

sg.theme('DarkPurple5')
nome_da_musica = [[sg.Text(text='press play..', justification = 'center', background_color = 'blue',
             text_color= 'black', size = (200.0), font = 'tahoma', key = 'song_name')]] 

Player_info = [
    [sg.Text('MP3 player by Tiago Dmasceno', background_color='black', text_color='white', font=('tahoma', 7) )]
]

currently_playing = [
    [sg.Text(background_color='black', text_color='white', size='200')]
]
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

    
