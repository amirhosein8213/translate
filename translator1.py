from tkinter import *
from tkinter import ttk , messagebox , font , simpledialog , filedialog , colorchooser
from  deep_translator import GoogleTranslator
from PIL import Image, ImageTk


win = Tk()
win.geometry("800x600")
win.title("Translator App")


first_text = Text(win , font=("Tahoma" , 12) , height=12 , borderwidth=10)
first_text.pack(fill="x" , pady=10)



def tarjome():
    natije=GoogleTranslator(target=var.get()).translate(first_text.get('1.0',END))
    result_text.delete('1.0',END)
    result_text.insert(END,natije)
    result_text.after(100, tarjome) 
    




lanuage= LabelFrame(win , text="انتخاب زبان", font=("Tahoma" , 9) , labelanchor="ne")

image_ir=PhotoImage(file="iran.png")
var = StringVar(value="fa")
r1 = Radiobutton(lanuage ,  font=("Tahoma" , 9) ,image=image_ir, value="fa" ,variable=var , command=tarjome)
r1.pack(side="right")


image_en=PhotoImage(file="english.png")
r2= Radiobutton(lanuage ,image=image_en,value="en" ,variable=var, command=tarjome)
r2.pack(side="right")


image_fr=PhotoImage(file="france.png")
r3 = Radiobutton(lanuage , image=image_fr, value="fr" ,variable=var, command=tarjome)
r3.pack(side="right")



image_ge=PhotoImage(file="germany.png")
r4 = Radiobutton(lanuage ,image=image_ge, value="de" ,variable=var, command=tarjome)
r4.pack(side="right")



image_tr=PhotoImage(file="turkey.png")
r5 = Radiobutton(lanuage , image=image_tr , value="tr" ,variable=var, command=tarjome)
r5.pack(side="right")



image_ch=PhotoImage(file="china.png")
r6= Radiobutton(lanuage , image=image_ch, value="ch" ,variable=var, command=tarjome)
r6.pack(side="right")

lanuage.pack()



result_text = Text(win , font=("Tahoma" , 12) , height=12, borderwidth=10)
result_text.pack(fill="x" , pady=10)




mainloop()



