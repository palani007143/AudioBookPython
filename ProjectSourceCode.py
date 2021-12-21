# Python audiobook project

# This project is done by: Palani Kumar S
from audio import *
from tkinter import *   # Importing the GUI named tkinter
from tkinter.filedialog import *
root = Tk()

def close_window():
    root.destroy()  # Destroying the main window


# Creating the tkinter window 

def main():
    frame = Frame(root)
    frame.pack(fill=None, expand=False)
    bottomframe = Frame(root, width=1000, height=500, background="bisque")
    bottomframe.pack( side = BOTTOM )
    redbutton = Button(frame, text="Browse and select the PDF file you want to process.", fg="blue", command=close_window)  # The window will get closed by the command
    redbutton.pack( side = LEFT)


    # Adding widget to the root window

    Label(root, text='Audiobook', font=('Comic Sans MS', 15)).pack(side=TOP, pady=10)
    # other stylish fonts can be used here too

    # photo = PhotoImage(file="AudiobookGUICanvas.gif")  # Creating a photoimage object to use image . JPEG wouldn't work here
    # Button(root, image=photo).pack(side=TOP)  # Setting image in button
    var = StringVar()
    entry = Entry(root, textvariable = var)
    entry.pack()
    root.mainloop()
    print(var.get(),"tets")
    pageRange = var.get()
    audio(pageRange)
    
    


if __name__ == '__main__':
    main()
