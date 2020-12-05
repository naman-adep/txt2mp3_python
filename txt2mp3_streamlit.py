from gtts import gTTS
from playsound import playsound
import streamlit as st 
import os

st.title("Convert Text to Audio")
txt = st.text_input("Enter Text Here")

if st.button("Convert"):
	os.system("del audio.mp3")
	speech = gTTS (text=txt, lang='en', slow=False)
	speech.save("audio.mp3")
	playsound("audio.mp3")
	st.write('Audio file is saved as audio.mp3')