#DAY1
'''from tkinter import *
from PIL import Image,ImageTk

root=Tk()     #root is instance of tk class
#gui logic

#Width*Height
root.geometry("1000x400")

#(width,height)
root.maxsize(1000,1000)
root.minsize(800,600)

root.title("Course Hub App")

a = Label(root, text="course Hub app",font=("Arial",24))
a.pack()

photos=PhotoImage(file="1.png")
Himanshu=Label(image=photos)
Himanshu.pack()

#for jpg Image
image=Image.open("photo.jpg")
photo=ImageTk.PhotoImage(image)

Himanshu_label=Label(image=photo)
Himanshu_label.pack()

root.mainloop()'''




#DAY2

from tkinter import *

root = Tk()
root.geometry("300x233")
root.title("My GUI with Himanshu")

# Important Label Options
"""
text -> adds the text
bg -> background
fg -> foreground
font -> sets the font 
       1. ("comicsansms", 19, "bold")
       2. "comicsansms 19 bold"
padx -> x padding
pady -> Y padding
relief -> border styling - SUNKEN, RAISED, GROOVE, RIDGE
"""


title_Label = Label(
    text="""
Random text is placeholder content used in design, layout mockups, and \n software testing to fill space without drawing the reader's attention.
Common Types of Random Text

• Lorem Ipsum: Scrambled classical Latin text derived from Cicero's de \n Finibus Bonorum et Malorum. It is traditionally used because its normal letter distribution mimics natural English. You can create it using online tools like the Lipsum generator.
• Real English Random Text: Meaningful sentences or words drawn from ]n common vocabulary corpora, useful for prompts, testing names, or building user interfaces.
• Fake Data: Structured placeholder text containing realistic names,\n email addresses, phone numbers, and JSON responses.
""",
    bg="red",
    fg="white",
    padx=13,
    pady=14,
    font=("comicsansms",9, "bold"),
    borderwidth=3,
    relief=SUNKEN,
)
#Important Pack Option

'''
anchor=nw  (DEFAULT=TOP)
side=left,right,top,bottom 
fill
padx
paxy
'''

# title_Label.pack(side=BOTTOM,fill=X,padx=10,pady=10,anchor="sw")
title_Label.pack(side=LEFT,fill=Y,padx=10,pady=10)



root.mainloop()



#DAY3
from tkinter import *
root=Tk()
root.geometry("353x536")
f1=Frame(root,bg="grey")
f1.pack(side=LEFT,fill="y")

f2=Frame(root,borderwidth=8,bg='grey',relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="Project-Himanshu")
l.pack(pady=142)

l=Label(f2,text="Course Hub")
l.pack()
root.mainloop()


#Day4
from tkinter import *
root=Tk()
root.geometry("655x333")

frame=Frame(root,borderwidth=6,bg='grey',relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

b1=Button(frame,fg="red",text="Print now")
b1.pack()
root.mainloop()
 
