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

    def insert(self,name,phone_num):
        name = input ("Enter the name : ")
        phone_num = input("Enter the Number : ")
        new_entry = Entry(name, phone_num)

        if self.head is None:
            self.head = new_entry
        else:
            current = self.head
            while current.next:
                current = current.next

    def display(self):
        current = self.head
        while current:
            print("Name:", current.name)
            print("Phone number:", current.phone_num)
            current = current.next

phonebook.display() 
phonebook = Phonebook()
phonebook.insert(name, phone_num)

#deklaroj phonebook me init qe te mbaje shenim koken e linked
#  list ose entryin e pare ne phonebook
#useri vendos te dhenat
#nese koka eshte boshe atehere new entry eshte koka ose nese ka nje koke current
# do jete entry tjeter

