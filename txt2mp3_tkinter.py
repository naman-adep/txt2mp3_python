from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

def convert_audio():
	text_info = text.get()
	os.system("del audio.mp3")
	myObj = gTTS (text=text_info, lang='en', slow=False)
	myObj.save("audio.mp3")
	playsound("audio.mp3")
	text_entry.delete(0,END)

app = Tk()
app.geometry('500x500')
app.title("Python Text to Audio App")
heading = Label (text="Python Text to Audio App", fg="black", font="10", height="3")
heading.pack()
text_field = Label(text="Text :")
text_field.place(x=15,y=70)
text = StringVar()
text_entry = Entry(textvariable=text, width="30")
text_entry.place(x=15,y=100)
button = Button(text="Convert to Audio", command=convert_audio, width="30", height="2", bg="grey")
button.place(x=15, y ="140")


mainloop()
