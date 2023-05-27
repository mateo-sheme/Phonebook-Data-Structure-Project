import csv

from tkinter import *
import tkinter as tk

from tkinter import messagebox


class Entry:
    def __init__(self,name,phone_num):
        self.name = name
        self.phone_num = phone_num
        self.next = None

#krijon klasen entry per te futur te dhenat e para
#deklaroj metoden init e cila ben inicializimin e 3 parametrave
#name, numri, ndersa self ben qe keto variabla te mbajne vlera 
# per cdo entry te vendosur
#ndersa none ben qe entry tjeter te vendoset si linked list, 
# momentalisht nuk ka entry tjeter keshtuqe vendoset si none


class Phonebook:
    def __init__(self):
        self.head = None

    def insert(self):
        name = input ("Enter the name : ")
        phone_num = input("Enter the Number : ")
        new_entry = Entry(name, phone_num)

        if self.head is None:
            self.head = new_entry
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_entry
    

    def update(self):
        if E_name.get() and E_number.get():
            phonebook[WhichSeleceted()] = E_name.get()+' '+E_number
            WriteInCSVFile(phonebook)
            messagebox.showinfo("Succesfully Updated")
            clear_text()


    def display(self):
        current = self.head
        while current:
            print("Name:", current.name)
            print("Phone number:", current.phone_num)
            current = current.next
    
    def binary_search(self, name):
        current = self.head
        while current:
            if current.name == name:
                return current.name & current.phone_num
            current = current.next
        return None

    def clear_text(self):
        E_name.set('')
        E_number.set('')

    def WriteInCSVFile(self,phonebook):
        with open('database.csv', 'w', newline='') as csv_file:
            writeobj = csv.writer(csv_file, delimiter=',')
            writeobj.writerow(['Name', 'Phone Number'])  # Write the header row

            current = phonebook.head
            while current:
                writeobj.writerow([current.name, current.phone_num])
                current = current.next

    def name_to_search(self,phonebook):
        input("Enter the name to search: ")
        name = phonebook.binary_search(name_to_search)
        if phone_num:
            print("Name:", name)
        else:
            print("Entry not found")



phonebook = Phonebook()


phonebook.WriteInCSVFile(phonebook)




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
E_name = tk.Entry(Inside_Frame1,width = 30, textvariable=E_name)
E_name.grid(row=0,column=1, padx=5, pady=5)

l_number = Label(Inside_Frame1, text="Number : ")
l_number.grid(row=1,column=0, padx=5, pady=5)

E_number = StringVar()
E_number = tk.Entry(Inside_Frame1,width = 30, textvariable=E_number)
E_number.grid(row=1,column=1, padx=5, pady=5)

if E_name.get() and E_number.get():
    # Retrieve values from Entry widgets
    name = E_name.get()
    phone_num = E_number.get()

Frame2 = Frame(window)
Frame2.grid(row=0,column=1,padx=15,pady=15)

Insert_button = tk.Button(Frame2, text="Insert contact",width=15,fg="black", command=phonebook.insert)
Insert_button.grid(row=0, column=0, padx=8, pady=8)

Update_button = Button(Frame2, text="Insert contact",width=15,fg="black", command=phonebook.update)
Update_button.grid(row=1, column=0, padx=8, pady=8)

clear_button = Button(Frame2, text="Insert contact",width=15,fg="black", command=phonebook.clear_text)
clear_button.grid(row=2, column=0, padx=8, pady=8)


display_data = Frame(window)
display_data.grid(row=1, column=0, padx=15, pady=15)
scroll = Scrollbar(display_data, orient=VERTICAL)
select = Listbox(display_data, yscrollcommand=scroll.set, width=40)
scroll.config(command=select.yview)
select.grid(row=0, column=0, sticky=W)
scroll.grid(row=0, column=1, sticky=N+S)




window.mainloop()

#deklaroj phonebook me init qe te mbaje shenim koken e linked
#  list ose entryin e pare ne phonebook
#useri vendos te dhenat
#nese koka eshte boshe atehere new entry eshte koka ose nese ka nje koke current
# do jete entry tjeter

