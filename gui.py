from tkinter import *
import tkinter as tk



window = tk.Tk()

window.geometry("500x800")
window.title("Phonebook")


Frame1 = LabelFrame(window, text = "Enter the Contact")
Frame1.grid(padx = 25, pady = 15)

Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0,column=0,padx=15,pady=15)\

l_name = Label(Inside_Frame1, text="Name : ")
l_name.grid(row=0,column=0, padx=5, pady=5)

E_name = StringVar()
E_name = Entry(Inside_Frame1,width = 30, textvariable=E_name)
E_name.grid(row=0,column=1, padx=5, pady=5)

l_number = Label(Inside_Frame1, text="Number : ")
l_number.grid(row=1,column=0, padx=5, pady=5)

E_number = StringVar()
E_number = Entry(Inside_Frame1,width = 30, textvariable=E_number)
E_number.grid(row=1,column=1, padx=5, pady=5)


Frame2 = Frame(window)
Frame2.grid(row=0,column=1,padx=15,pady=15)

Insert_button = Button(Frame2, text="Insert contact",width=15,fg="black", command=)
Insert_button.grid(row=0, column=0, padx=8, pady=8)

Update_button = Button(Frame2, text="Insert contact",width=15,fg="black", command=)
Update_button.grid(row=1, column=0, padx=8, pady=8)

clear_button = Button(Frame2, text="Insert contact",width=15,fg="black", command=)
clear_button.grid(row=2, column=0, padx=8, pady=8)


display_data = Frame(window)
display_data.grid(row=1, column=0, padx=15, pady=15)
scroll = Scrollbar(display_data, orient=VERTICAL)
select = Listbox(display_data, yscrollcommand=scroll.set, width=40)
scroll.config(command=select.yview)
select.grid(row=0, column=0, sticky=W)
scroll.grid(row=0, column=1, sticky=N+S)




window.mainloop()