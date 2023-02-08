import PySimpleGUI as sg
print(oi)
sg.theme('black')

layout = [[sg.Text('muito bom')],
[sg.Text('saber python'), sg.InputText()],
[sg.Button('ok'), sg.Button('cancel')]]

window = sg.Window('acertei', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'cancel':
        break
print('you entered', values=[0])

window.close()

    
