import tkinter
from tkinter import PhotoImage
import pandas
import random

location_value=1
random_locations=[]
BACKGROUND='#B1DDC6'
window=tkinter.Tk()
window.title("Flashy")
window.configure(padx=50,pady=50,bg=BACKGROUND)

#The French word

data=pandas.read_csv("Day31/data/french_words.csv")
French_list=data["French"].tolist()
English_list=data['English'].tolist()


#The function of buttons

def button_clicked():
    random_location=random.randint(0,len(French_list)-1)
    end=False
    while not end:
        if random_location in random_locations:
            random_location=random.randint(0,len(French_list)-1)
        else:
            end=True
    random_word=French_list[random_location]
    canvas.itemconfig(tittle,text="French",fill='black')
    canvas.itemconfig(word,text=random_word,fill='black')
    canvas.itemconfig(front_image, image=picture1)
    canvas.after(3000, flip_card, random_location)
    global location_value
    location_value = random_location
def right_click():
    global location_value
    random_locations.append(location_value)
    button_clicked()

#Flip the Card

def flip_card(n):
    canvas.itemconfig(front_image, image=picture1_new)
    canvas.itemconfig(tittle,text='English',fill='white')
    canvas.itemconfig(word,text=English_list[n],fill='white')

#Generate all components

picture1=PhotoImage(file="Day31/images/card_front.png")
picture1_new = PhotoImage(file="Day31/images/card_back.png")
canvas=tkinter.Canvas(window,width=800,height=526,background=BACKGROUND,highlightthickness=0)
front_image=canvas.create_image(400,263,image=picture1)
tittle = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
word = canvas.create_text(400,260,text="",font=("Arial",60,"bold"))
picture2=PhotoImage(file="Day31/images/wrong.png")
button1=tkinter.Button(window,text="Click Me",image=picture2,width=100,height=99,bg=BACKGROUND,highlightthickness=0,command=button_clicked)
picture3=PhotoImage(file="Day31/images/right.png")
button2=tkinter.Button(window,text="Click Me",image=picture3,width=100,height=100,bg=BACKGROUND,highlightthickness=0,command=right_click)

#Place all the components on their places

canvas.grid(row=0,column=1,columnspan=2)
button1.grid(row=1,column=1)
button2.grid(row=1,column=2)


button_clicked()

window.mainloop()