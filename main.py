import PySimpleGUI as sg

# sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
sg.popup('Welcome to Typer!', 'Click OK to start playing!!', font=("Helvetica", 25))

letters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
layout = [ 
    # [sg.Titlebar("Title")],
    [sg.Sizer(200, 150)],
    [sg.Text("Click OK to continue", size=(30, 1), font=("Helvetica", 55), text_color="black", background_color = 'SkyBlue1')],
    [sg.Button("OK")]
]

# Create the window
window = sg.Window("Test", layout, margins=(200, 250), background_color='SkyBlue1')

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
