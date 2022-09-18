import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Lucida 14')

    button_size = (3,1)

    layout = [ 
        [sg.Text('|', key='-OUTPUTTEXT-', expand_x=True, justification='right', pad=(0,15), right_click_menu=theme_menu)],
        [sg.Button('Enter', expand_x=True), sg.Button('Clear', expand_x=True)],
        [sg.Button('7', size=button_size), sg.Button('8', size=button_size), sg.Button('9', size=button_size), sg.Button('/', size=button_size)],
        [sg.Button('4', size=button_size), sg.Button('5', size=button_size), sg.Button('6', size=button_size), sg.Button('*', size=button_size)],
        [sg.Button('1', size=button_size), sg.Button('2', size=button_size), sg.Button('3', size=button_size), sg.Button('+', size=button_size)],
        [sg.Button('0', expand_x=True), sg.Button('.', size=button_size), sg.Button('-', size=button_size)]
    ]

    return sg.Window('Calculator', layout)

theme_menu = ['menu', ['BlueMono', 'DarkTeal7', 'DarkGrey2', 'raondom']]

window = create_window('LightBlue3')

calculations = ''

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in '1234567890.':
        calculations+=event
        window['-OUTPUTTEXT-'].update(calculations) 

    if event in '/*+-':
        calculations+=event
        window['-OUTPUTTEXT-'].update(calculations)

    if event == 'Enter':
        window['-OUTPUTTEXT-'].update(eval(calculations))
        calculations = ''

    if event == 'Clear':
        calculations = ''
        window['-OUTPUTTEXT-'].update('')

window.close() 
