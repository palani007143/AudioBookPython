import pyttsx3
import PyPDF2
from tkinter import *   # Importing the GUI named tkinter
from tkinter.filedialog import *
from page_range import *

# Executing the command for text to speech
def audio(pageRange):
    # Label(root, text='Audiobook', font=('Comic Sans MS', 15)).pack(side=TOP, pady=10)
    # Label.pack()
    # root.mainloop()
    engine = pyttsx3.init()  # Object creation
    rate = engine.getProperty('rate')
    print (rate)  # Printing the current voice rate
    engine.setProperty('rate', 185)   # Setting up the new voice rate
    volume = engine.getProperty('volume')
    print (volume)  # Printing the current volume level
    engine.setProperty('volume',1.0)  # Setting up the volume level between 0 and 1
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    book=askopenfilename()
    pdfreader=PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages
    a , b = get_text(pageRange)
    try:
        for num in range(a, b):
            page=pdfreader.getPage(num)
            text=page.extractText()
            player=pyttsx3.init()
            player.say(text)
            player.runAndWait()
    except:
        for num in range(0,pages):
            page=pdfreader.getPage(num)
            text=page.extractText()
            player=pyttsx3.init()
            player.say(text)
            player.runAndWait()
    engine.save_to_file(text, 'Audiobook created by Dolly.mp3')   # Saving the voice to a file 
    engine.runAndWait()
    print("Your audiobook file has been generated as an mp3 file. Check the project file directory for getting the file.")
