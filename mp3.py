import PySimpleGUI as sg
import os
from play import get_files_inside_directory_not_recursive, play_sound, pause_sounds, unpause, stop_sounds, is_sound_playing


sg.theme('Reddit')
song_title_column = [sg.Text(text='press play..', justification = 'center', background_color = 'blue',
             text_color= 'black', size = (200.0), font = 'tahoma', key = 'song_name')] 

player_info = [
    [sg.Text('MP3 player by Tiago Dmasceno', background_color='black', text_color='white', font=('tahoma', 7) )]
]

currently_playing = [
    [sg.Text(background_color='black', text_color='white', size=(200,0), font= ('tahoma',10), key= 'currently_playing')]
]


ALBUM_COVER_IMAGE_PATH = 'images\\Capa.png'
PLAY_SONG_IMAGE_PATH = 'images\\play.png'
GO_BACK_IMAGE_PATH = 'images\\back.png'
PAUSE_SONG_IMAGE_PATH = 'images\\stop.png'
GO_FORWARD_IMAGE_PATH = 'images\\next.png'




main = [
    [sg.Canvas(background_color='black', size=(480, 20), pad=None)],
    [sg.Column(layout=player_info, justification='c',
               element_justification='c', background_color='black')],
    [
        sg.Canvas(background_color='black', size=(40, 350), pad=None),
        sg.Image(filename=ALBUM_COVER_IMAGE_PATH,
                 size=(350, 350), pad=None),
        sg.Canvas(background_color='black', size=(40, 350), pad=None)
    ],
    [sg.Canvas(background_color='black', size=(480, 10), pad=None)],
    [sg.Column(song_title_column, background_color='black',
               justification='c', element_justification='c')],
    [sg.Text('_'*80, background_color='black', text_color='white')],
    [
        sg.Canvas(background_color='black', size=(99, 200), pad=(0, 0)),
        sg.Image(pad=(10, 0), filename=GO_BACK_IMAGE_PATH, enable_events=True,
                 size=(35, 44), key='previous', background_color='black'),
        sg.Image(filename=PLAY_SONG_IMAGE_PATH,
                 size=(64, 64), pad=(10, 0), enable_events=True, key='play', background_color='black'),
        sg.Image(filename=PAUSE_SONG_IMAGE_PATH,
                 size=(58, 58), pad=(10, 0), enable_events=True, key='pause', background_color='black'),
        sg.Image(filename=GO_FORWARD_IMAGE_PATH, enable_events=True,
                 size=(35, 44), pad=(10, 0), key='next', background_color='black'),
    ],
    [sg.Column(layout=currently_playing, justification='c',
               element_justification='c', background_color='black', pad=None)]


]
window = sg.Window('spotfy', layout=main, size=(480, 730), background_color='black', finalize=True, grab_anywhere=True, resizable=False)

directory = sg.popup_get_folder('Select Music Directory')

songs_in_directory = get_files_inside_directory_not_recursive(directory)
song_count = len(songs_in_directory)
current_song_index = 0


def update_song_display():
    window['song_name'].update(os.path.basename(
        songs_in_directory[current_song_index]))
    window['currently_playing'].update(
        f'Playing: {os.path.basename(songs_in_directory[current_song_index])}')


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'play':
        if is_sound_playing():
            pass
        if is_sound_playing() == False:
            play_sound(songs_in_directory[current_song_index])
            update_song_display()

    elif event == 'pause':
        if is_sound_playing():
            pause_sounds()
        else:
            unpause()
        pass

    elif event == 'next':
        if current_song_index + 1 < song_count:
            stop_sounds()
            current_song_index += 1
            play_sound(songs_in_directory[current_song_index])
            update_song_display()

        else:
            print('Reached last song')
            pass

    elif event == 'previous':
        if current_song_index + 1 <= song_count and current_song_index > 0:
            stop_sounds()
            current_song_index -= 1
            play_sound(songs_in_directory[current_song_index])
            update_song_display()
        else:
            print('Reached first song')


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

    
