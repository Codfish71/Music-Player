from tkinter import *
from pygame import mixer

root = Tk()

mixer.init()
root.geometry('1100x600')
root.title("Pentatonic")
root.configure(bg='#263238')
root.iconbitmap(r'icon1_qqB_icon.ico')

menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
menu.add_cascade(label='File') 


label = Label(root,text="")
label.pack()

def ply_btn():
	print("Playing a song")
ply_photo = PhotoImage(file='play-button.png')
ply_btn = Button(root,image=ply_photo,command=ply_btn)
ply_btn.place(x=500,y=500)

root.mainloop()

