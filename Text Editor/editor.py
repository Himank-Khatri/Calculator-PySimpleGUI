import PySimpleGUI as sg
from pathlib import Path

sg.theme('default1')

smilies = [
    'Happy', [':)', ':D', 'xD', '<3'],
    'Sad', [':(', 't_t'],
    'Other', [':3']
]

smilies_events = smilies[1] + smilies[3] + smilies[5]

toolbar = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count']],
    ['Add', smilies]

]

layout = [
    [sg.Menu(toolbar)],
    [sg.Multiline(key='-INPUT-', expand_x=True, expand_y=True, font=('Dubai, 14'))],
]

window = sg.Window('Untitled', layout, size=(900,600))

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Open':
        path = sg.popup_get_file('Open', no_window=True, title='Open')
        file = Path(path)
        window['-INPUT-'].update(file.read_text())
        window.TKroot.title(f"{path.split('/')[-1]}")

    if event == 'Save':
        path = sg.popup_get_file('Save', no_window=True, save_as=True, title='Save As')
        file = Path(path)
        file.write_text(values['-INPUT-'])
        window.TKroot.title(f"{path.split('/')[-1]}.txt")


    if event == 'Word Count':
        sg.popup(f"Characters: {len(''.join(values['-INPUT-'].split()))}\nWords: {len(values['-INPUT-'].split())}")

    if event in smilies_events:
        window['-INPUT-'].update(values['-INPUT-']+event)

window.close()

