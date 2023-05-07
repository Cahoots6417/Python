from tkinter import *
from tkinter import Tk, Entry, Text, Button, PhotoImage 
from pathlib import Path
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/willie/Public/main/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

root = Tk()
 
root.configure(background='#5e5e5e')
root.geometry('314x54')
 
def option_1():
    subprocess.call(["python3", "/home/willie/Public/main/option_1.py"]) 

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))


button_1 = Button(root,  
borderwidth=0,
image=button_image_1, 
command=option_1,
relief="flat"
)

button_1.place(
    x=2.0,
    y=2.0,
    width=50.0,
    height=50.0
)

root.mainloop()