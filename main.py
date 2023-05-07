import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/willie/Public/main/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def wind1():
    subprocess.call(["python", "/home/willie/Public/main/wind1.py"])

def wind2():
    subprocess.call(["python", "/home/willie/Public/main/wind2.py"])

window = Tk()

window.geometry("314x54")
window.configure(bg = "#5E5E5E")


canvas = Canvas(
    window,
    bg = "#5E5E5E",
    height = 54,
    width = 314,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=wind1,
    relief="flat"
)
button_1.place(
    x=2.0,
    y=2.0,
    width=50.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=wind2,
    relief="flat"
)
button_2.place(
    x=54.0,
    y=2.0,
    width=50.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=106.0,
    y=2.0,
    width=50.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=158.0,
    y=2.0,
    width=50.0,
    height=50.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=210.0,
    y=2.0,
    width=50.0,
    height=50.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=quit,
    relief="flat"
)
button_6.place(
    x=262.0,
    y=2.0,
    width=50.0,
    height=50.0
)

window.mainloop()
    