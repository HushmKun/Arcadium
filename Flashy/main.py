FONT = ('Arial',40,'italic')
BACKGROUND_COLOR = "#B1DDC6"
from tkinter import * 

#--------------------------------- Main Window -------------------------------------#
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR,padx=10,pady=10)
window.geometry("+10+10")
window.resizable(False , False)

#--------------------------------- Canvas for images -------------------------------#
canvas = Canvas(highlightthickness=0 , width=800,height=526,bg=BACKGROUND_COLOR )
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img  = PhotoImage(file="./images/card_back.png" )
canvas.create_image(400,263,image=card_front_img)
canvas.create_text(400 , 150,text="Title" , font=FONT)
canvas.create_text(400 , 263,text="Word" , font=('Arial',60,'bold'))
canvas.grid(row=0,column=0)
#---------------------------------- Buttons ----------------------------------------#
wrong = PhotoImage(file="./images/wrong.png")
right = PhotoImage(file="./images/right.png")

unknown_button = Button(image=wrong)
known_button   = Button(image=right)

unknown_button.grid(row=1,column=0)
known_button.grid(row=1,column=1)




window.mainloop()