import pyttsx3
import PyPDF2
from tkinter import *   # Importing the GUI named tkinter
from tkinter.filedialog import *
from page_range import *
engine = pyttsx3.init()  # Object creation
audiotabclose = ''


def audio(pageRange, audiotab):
    # Create a window
    audiotabclose = audiotab

    # Set Title as Image Loader
    audiotab.title("Audio Player Presented By Divya Barathi!")

    # Set the resolution of window
    audiotab.geometry("550x300+300+150")

    # Allow Window to be resizable
    audiotab.resizable(width=True, height=True)
    frame = Frame(audiotab)
    frame.pack()
    
    redbutton = Button(frame, text="Stop Audio", fg="blue", font=('Comic Sans MS', 10), command=close_window_a)  # The window will get closed by the command
    redbutton.pack( side = LEFT)

    photo = PhotoImage(file="lisening.gif")  # Creating a photoimage object to use image . JPEG wouldn't work here
    background_label = Label(audiotab, image=photo, text='Stop Audio')
    background_label.place(x=0, y=35, relwidth=1, relheight=1)

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
    try:
        a , b = get_text(pageRange)
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
    finally:
        engine.save_to_file(text, 'Audiobook created by Dolly.mp3')   # Saving the voice to a file 
        engine.runAndWait()
        print("Your audiobook file has been generated as an mp3 file. Check the project file directory for getting the file.")
    audiotab.mainloop()

def close_window_a():
    engine.stop()
    audiotabclose.destroy()

    