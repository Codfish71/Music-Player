import os 
from tkinter import *
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog
import sys

root = Tk()

#for file directory
def browse_file():
	global filename
	filename = filedialog.askopenfilename()

menubar= Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=subMenu) 
subMenu.add_command(label='Open a folder',command=browse_file)
subMenu.add_command(label='Exit',command=root.destroy)

def about_us():
	tkinter.messagebox.showinfo('Pentatonic','for further queries - Email : 2017.prathamesh.pendal@ves.ac.in') 

subMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=subMenu) 
subMenu.add_command(label='About Us',command = about_us)	


mixer.init()
root.geometry('1100x600')
root.title("Pentatonic")
root.configure(bg='#263238')
root.iconbitmap(r'icon1_qqB_icon.ico')



label = Label(root,text="Pentatonic")
labelfont = ('times', 20, 'bold')
label.pack()
label.config(bg='#263238',fg='#ffffff',font=labelfont)

def ply_btn():
	global paused
	if paused:
		mixer.music.unpause()		
		status['text'] = 'Music resumed'
		paused=FALSE
	else :
		try:
			mixer.music.load(filename)
			mixer.music.play()
			status['text'] = 'playing music'+'-'+os.path.basename(filename) 
			paused = TRUE 
		except:
			tkinter.messagebox.showerror('File not found','Please load at least one file')


def stp_btn():
		
			mixer.music.stop()
			status['text'] = 'Music stopped'
		
paused = FALSE
def pause_music():
	global paused
	paused = TRUE
	mixer.music.pause()
	status['text'] = 'Music paused'

def set_vol(val):
	volume = int(val)/100
	mixer.music.set_volume(volume)

# for mute btn 
muted = FALSE
def mute_btn():
	global muted
	if muted:
		mixer.music.set_volume(0.7)
		scale.set(70)
		mute_btn.configure(image=vol_phto)
		muted=FALSE
	else :
		mixer.music.set_volume(0)
		scale.set(0)
		mute_btn.configure(image=mute_phto)
		muted =TRUE


ply_photo = PhotoImage(file='play-button.png')
ply_btn = Button(root,image=ply_photo,command=ply_btn)
ply_btn.place(x=100,y=450)
ply_btn.config(width=50, height=50)

stp_phto = PhotoImage(file="iconfinder_24_Stop_106221.png")
stp_btn = Button(root,image=stp_phto,command=stp_btn)
stp_btn.place(x=200,y=450)
stp_btn.config(width=50, height=50)

pause_photo = PhotoImage(file='button_black_pause.png')
pause_btn = Button(root,image=pause_photo,command=pause_music) 
pause_btn.place(x=300,y=450)
pause_btn.config(width=50, height=50)

vol_phto = PhotoImage(file="volume-off.png")
mute_phto = PhotoImage(file="volume-off-indicator.png")
mute_btn = Button(root,image=vol_phto,command=mute_btn)
mute_btn.place(x=400,y=450)
mute_btn.config(width=50, height=50)

scale = Scale(root,from_=0,to=100,orient=HORIZONTAL,command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.place(x=580,y=470)

status = Label(root,text='Welcome to Pentatonic World')
status.pack(side=BOTTOM,fill=X)

# bakground image
bkg_img = PhotoImage(file='0157d81d5691553.png')
bkg = Label(root,image=bkg_img)
bkg.config(width=700,height=350)
bkg.place(x=50,y=50)


root.mainloop()

