from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/willie/Public/main/assets/testwindow/")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("257x267")
window.configure(bg = "#FFFFFF")





button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
     
    relief="flat"
)
button_1.place(
    x=13.0,
    y=237.0,
    width=38.0,
    height=20.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= quit,
    relief="flat"
)
button_2.place(
    x=206.0,
    y=237.0,
    width=38.0,
    height=20.0
)
window.resizable(False, False)
window.mainloop()
