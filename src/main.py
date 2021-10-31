from tkinter import *
from tkinter import messagebox
import pandas
import random
import pyperclip
# importing the json library
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    numbers = [1,2,3,4,5,6,7,8,9,10]
    symbols = ['@','!','$','^','&']

    password_list=[]

    r_letters = random.randint(0, len(letters))
    r_numbers = random.randint(0, len(numbers))
    r_symbols = random.randint(0, len(symbols))


    letter_choosed = [random.choice(letters) for _ in range(r_letters)]
    number_choosed = [random.choice(numbers) for _ in range(r_numbers)]
    symbol_choosed = [random.choice(symbols)for _ in range(r_symbols)]


    password_list = letter_choosed + number_choosed + symbol_choosed

    random.shuffle(password_list)
    password = " "
    password = [password + str(char) for char in password_list]

    real_pass = "".join(password)
    entry3.insert(index=0, string=real_pass)
    pyperclip.copy(real_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def is_empty(website,email,password):
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        return False
    else:
        return True


def save_password():
    website_link = entry1.get()
    email_username = entry2.get()
    password = entry3.get()
    isNotEmpty = is_empty(website=website_link, email=email_username, password=password)
    if isNotEmpty:
        # storage = f"{website_link} | {email_username} | {password}\n"
        new_data = {
            website_link:{
                "name":email_username,
                "password":password
            }
        }
        is_valid = messagebox.askokcancel(title="Password Manager",message=f"Your Infor:\n website:{website_link}\nEmail{email_username}\nPassword{password}")
        if is_valid:
            try:
                with open("data.json",mode="r") as file:
                    # json.dump(new_data,file,indent=4)
                    # loading the data
                    data = json.load(file)
                    # updating the data
                    data.update(new_data)
            except FileNotFoundError:
                file =  open("data.json",mode="w")
                json.dump(new_data,file,indent=4)
            else:
                with open('data.json',mode='w') as file:
                    # writing the data
                    json.dump(data,file,indent=4)
            finally:
                # print(data)
                file.close()
                entry1.delete(0,'end')
                entry3.delete(0,'end')
    else:
        messagebox.showerror(title="Error found ",message="You keep some field empty!!")
    
    
# ---------------------------- Search SETUP ------------------------------- #
def search():
    try:
        with open('data.json',mode="r") as file:
            data = json.load(file)
            try:
                # now i am going to get the searching data from the entry
                searching_data = entry1.get()
                print(data[searching_data])
            except KeyError:
                messagebox.showerror(title="The error message:",message=f"{searching_data}not inserted in the database")
            else:
                # now i am goning to show the message box 
                messagebox.askokcancel(title="Searching value:",message=f"Email:{data[searching_data]['name']}\nPassword:{data[searching_data]['password']}")
    except FileNotFoundError:
        messagebox.showerror(title="The Error:",message="the file dosen\'t exists")
    

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
# screen.minsize(width=600,height=600)
# lets padding it 20dp
# seting the title
screen.title("Passoword manager")
screen.config(padx=50,pady=50)




# now i am going to set up the image to the screen 
canva = Canvas(width=200,height=200)
img = PhotoImage(file='demoreader/logo.png')
canva.create_image(100,100,image=img)
# canva.grid(column=1,row=0)s
canva.grid(row=0,column=1)


label1 = Label(text="Website       :",fg="black")
label2 = Label(text="Email/Username:",fg="black")
label3 = Label(text="Password      :",fg="black")

label1.grid(row=1,column=0)
label2.grid(row=2,column=0)
label3.grid(row=3,column=0)

entry1 = Entry(width=54)
entry1.focus()
entry2 = Entry(width=54)
entry2.insert(END,"tanzin736@gmail.com")
entry3 = Entry(width=54)

entry1.grid(row=1,column=1,columnspan=2)
entry2.grid(row=2,column=1,columnspan=2)
entry3.grid(row=3,column=1,columnspan=2)

button1 = Button(text="Password Genarator",command=password_generator)
button2 = Button(text="Add",width=46,command=save_password)
button3 = Button(text="Search",width=15,command= search)

button1.grid(row=3,column=2)
button2.grid(row=4,column=1,columnspan=2)
button3.grid(row=1,column=2)







# to keep the screen up we are going to do this
screen.mainloop()
