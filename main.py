import PySimpleGUI as sg

# sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

layout = [
    # [sg.Titlebar("Title")],
    # [sg.Sizer(400, 250)],
    [sg.Text("Click OK to continue")], 
    [sg.Button("OK")]
]

# Create the window
window = sg.Window("Test", layout, margins=(200, 250))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
