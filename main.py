import PySimpleGUI as sg
import random

# sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
# sg.popup('Welcome to Typer!', 'Click OK to start playing!!', font=("Helvetica", 25))

letters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
index = random.randrange(25)
letter = letters[index]

layout = [ 
    # [sg.Titlebar("Title")],
    # [sg.Sizer(200, 150)],
    [sg.Text(letter, font=("Helvetica", 75), text_color="black", background_color='LightSkyBlue1', key= "Letters")],
    # [sg.Listbox(letters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"), key="Letters")]
    [sg.Button("NEXT")],
    [sg.Button("OK")]   
]

# Create the window
window = sg.Window("Typer", layout, margins=(200, 170), background_color='LightSkyBlue1')

# Create an event loop
while True:
    event, values = window.read()

    if event == "NEXT":
        index = random.randrange(25)
        letter = letters[index]
        window.Element("Letters").Update(letter)

    
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

# Progress Bar
# for i in range(1,10000):
#     sg.one_line_progress_meter('My Meter', i+1, 10000, 'key','Optional message')
