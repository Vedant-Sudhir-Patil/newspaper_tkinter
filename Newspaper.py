import abc
from tkinter import *
from PIL import Image
import datetime as dt
import tkinter.messagebox as tmsg

def Newspaper():
    root=Tk()
    # Newspaper 

    root.title("ZA WARUDO - By Big News Morgans")
    root.geometry("900x750")
    root.resizable(False,False)

    # Functions
    def every_100(text):
        # Function which breaks the line at every 100 letters
        final_text=""
        j=0
        for i in range(0,len(text)):
            j+=1
            final_text+=text[i]
            if j%100==0 and j != 0:
                final_text+="\n"
            elif text[i]=="\n":
                j=0
        return final_text

    def func():
        print("This currently has no function")

    # Menus and Submenus
    mainmenu= Menu(root)
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label="New File",command=func)
    m1.add_command(label="Open File",command=func)
    m1.add_separator()
    m1.add_command(label="Save",command=func)
    m1.add_command(label="Save As",command=func)
    mainmenu.add_cascade(label="File",menu=m1)
    m2=Menu(mainmenu,tearoff=0)
    m2.add_command(label="Undo",command=func)
    m2.add_command(label="Redo",command=func)
    m2.add_separator()
    m2.add_command(label="Cut",command=func)
    m2.add_command(label="Copy",command=func)
    m2.add_command(label="Paste",command=func)
    m2.add_separator()
    m2.add_command(label="Find",command=func)
    m2.add_command(label="Replace",command=func)
    mainmenu.add_cascade(label="Edit",menu=m2)
    mainmenu.add_command(label="Selection",command=func)
    mainmenu.add_command(label="View",command=func)
    mainmenu.add_command(label="Go",command=func)
    mainmenu.add_command(label="Run",command=func)
    mainmenu.add_command(label="Terminal",command=func)
    mainmenu.add_command(label="Help",command=func)
    mainmenu.add_command(label="Exit",command=quit)
    root.config(menu=mainmenu)

    #if __name__=="__main__":
    #    rep=int(input("How many articles :"))
    rep=3 
    text=[]
    photos=[]
    for i in range (rep):
        with open(f"F:\py_txt\{i+1}.txt","r") as f:
            txt=f.read()
            text.append(every_100(txt))
        photo=PhotoImage(file=f"F:\py_txt\{i+1}.png")
        photos.append(photo)
        
    # Scroll Bar
    f=Frame(root)
    canvas=Canvas(f)
    scroll=Scrollbar(f,command=canvas.yview)
    canvas.configure(yscrollcommand=scroll.set)
    canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion = canvas.bbox('all')))
    canvas.pack(side=LEFT,fill=BOTH, expand="yes")
    scroll.pack(side=RIGHT,fill=Y)
    fc=Frame(canvas)
    canvas.create_window((0,0),window=fc)
    f.pack(fill=BOTH,expand="yes")

    # Code which displays heading , date and title
    f0=Frame(fc, width=800, height=70)
    Label(f0, text="Newspaper GUI", font="comicsansms 33 bold",padx=22).pack()
    dtm=dt.datetime.now()
    a=dtm.strftime("%A, %d %B %Y")
    Label(f0, text=f"{a}", font="comicsansms 13").pack()
    f1=Frame(fc, width=800, height=50)
    Label(f1, text=f"News of Top {rep} Animes of all time", font="comicsansms 23 underline",padx=22, pady=22).pack(side="left")
    f0.pack()
    f1.pack(anchor="w")

    # Code which displays main text and images
    for i in range (rep):
        if i%2==0:
            x="left"
            vr="w"
            br="e"
        else:
            x="right"
            vr="e"
            br="w"
        f3= LabelFrame(fc, width=900,height=200)
        Label(f3,text=text[i], padx=22, pady=22,anchor=vr).pack(side=x,fill=BOTH)
        Label(f3,image=photos[i], anchor=br).pack(fill=BOTH)
        f3.pack(fill=BOTH,padx=22)

    # Status Bar
    statusvar=StringVar()
    statusvar.set("Ready")
    sbar=Label(root,textvariable=statusvar,relief=SUNKEN,bg="purple",fg="white",anchor=W)
    sbar.pack(side=BOTTOM,fill=X)

    root.mainloop()

Newspaper()
