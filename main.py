import PySimpleGUI as sg
import random
from PySimpleGUI.PySimpleGUI import rgb
from pynput import keyboard
from pynput.keyboard import KeyCode

# sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
sg.popup('Welcome to Typer!', 'Click OK to start playing!!', 'YOU CANNOT EXIT USING THE X BUTTON!', 'YOU HAVE TO PRESS THE ESC KEY', font=("Helvetica", 20))

letters = ('A','B',"C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
index = random.randrange(2)
letter = letters[index]

layout = [ 
    # [sg.Titlebar("Title")],
    # [sg.Sizer(200, 150)],
    [sg.Text(letter, font=("Helvetica", 75), text_color="black",
             background_color=rgb(124, 94, 206), key="Letters")],
    [sg.Button("NEXT")],
    [sg.Button("OK")]   
]

# Create the window
window = sg.Window("Typer", layout, margins=(200, 170),
                   background_color=rgb(124, 94, 206))
window.finalize()
    
with keyboard.Events() as events:
    for event in events:
        if (event.key == keyboard.Key.esc):
            break
        elif event.key == KeyCode.from_char(letter.lower()):
            print("IT WORKS")
            index = random.randrange(25)
            letter = letters[index]
            window.Element("Letters").Update(letter)
            window.refresh()
        else:
            print('Received event {}'.format(event))

window.close()
quit()
