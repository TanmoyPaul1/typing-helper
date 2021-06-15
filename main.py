import PySimpleGUI as sg
import random
from PySimpleGUI.PySimpleGUI import rgb
from pynput import keyboard
from pynput.keyboard import Key, KeyCode, Listener
      
# sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
# sg.popup('Welcome to Typer!', 'Click OK to start playing!!', font=("Helvetica", 25))

letters = ('A','B',"C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
index = random.randrange(2)
letter = letters[index]

layout = [ 
    # [sg.Titlebar("Title")],
    # [sg.Sizer(200, 150)],
    [sg.Text(letter, font=("Helvetica", 75), text_color="black",
             background_color=rgb(124, 94, 206), key="Letters")],
    # [sg.Listbox(letters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"), key="Letters")]
    # [sg.Button("NEXT")],
    [sg.Button("OK")]   
]

# Create the window
window = sg.Window("Typer", layout, margins=(200, 170),
                   background_color=rgb(124, 94, 206))



# Create an event loop
while True:
    event = window.read()
    
    with keyboard.Events() as actions:
        # Block at most one second
        for action in actions:
            if event == "OK" or event == sg.WIN_CLOSED or action.key == Key.esc:
                event = "OK"
                break
            elif action.key == KeyCode.from_char(letter.lower()):
                print('{} was pressed correctly'.format(action))
                break
            else:
                print(action.key, letter, KeyCode.from_char(letter))
                print('Incorrect button: {}'.format(action))

    index = random.randrange(25)
    letter = letters[index]
    window.Element("Letters").Update(letter)

    if event == "NEXT":
        index = random.randrange(25)
        letter = letters[index]
        window.Element("Letters").Update(letter)
        continue

    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
