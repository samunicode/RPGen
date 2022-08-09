# Made with love by Sameer Chauhan (https://github.com/samunicode) 
# Please credit me in all your future updates, that's all - you're free to use this code commercially, too.
# (c) Sameer Chauhan, 2022-23 provided under The MIT License (https://opensource.org/licenses/MIT)


#-------------------------------IMPORTING MODULES---------------------------------#
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox as mbox #we import it seperately bcoz ?* imports classes and this is not a class
from random import randint,choice,shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    password_list = []
    for char in range(randint(8, 10)):
      password_list.append(choice(letters))

    for char in range(randint(2, 4)):
      password_list += choice(symbols)

    for char in range(randint(2, 4)):
      password_list += choice(numbers)

    shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    
    entry2.delete(0, END)
    entry2.insert(0,password)
    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    name_website = entry0.get()
    name_email = entry1.get()
    name_password = entry2.get()

    with open('media/Password.csv','a') as data:
        if len(name_website)==0 or len(name_email)<=3 or len(name_password)==0:
            option = messagebox.showinfo(title="Uhh-ohh", message="Please enter a valid data!")
        else:
            option = messagebox.askokcancel(title="Confirm",
                                            message=f"Website: {name_website}\nEmail: {name_email}\nPassword: {name_password}\nWould you like to SAVE your login credentials?")
            if option:
                data.write(f"Website: {name_website} || Email: {name_email} || Password: {name_password}\n")
                option = messagebox.showinfo(title="Success", message="Successfully Saved")
                option = messagebox.showinfo(title="Instructions to access Login Credentials", message="Your Login Credentials have successfully been saved\n and can be viewed by clicking on 'VIEW DATA' button.\n\nTo modify or delete any entry, open 'Password.csv' file to make desired changes.")
                entry2.delete(0, END)
                entry1.delete(0, END)
                entry0.delete(0, END)
                data.close()


#--------------------------------------About--------------------------------------------#
def about_dev():
    mbox.showinfo('About Me','*RPGen is beginner friendly python project developed by Sameer Chauhan.\nContact\n1)Website: https:.//www.sameerchauhan.in\n2)GitHub: https://github.com/samunicode\n3)LinkedIn: https://www.linkedin.com/in/cbsameer/ \n\n\n***************************Features**************************\n\n\n*RPGen is a full fledged random password generator which generates passwords which are diffcult to crack.\n*Interactive GUI created to help user to interact with the application in more a fun and & interactive manner.\n*Credentials are stored in a CSV file from where user can access or remove the entries as per requirement.\n\n\n*************************MIT LICENSE*************************\n\n\n-----------Copyright (c) 2022-2023 Sameer Chauhan------------\n\n\n**Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sellcopies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n**The above copyright notice and this permission notice shall be included in all copies substantial portions of the Software.\n**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE')

#-------------------------------------VIEW ENTRIES-------------------------------------------#
def view_entries():
    #f = open("media/passec.txt", "r")#
    #print(f.read())#
    #mbox.showinfo()#
    entry_box = Tk()
    entry_box.title("Saved Credentials")
    entry_box.iconbitmap('media/favicon_rpgen.ico')
    with open("media/Password.csv", "r") as f:
         Label(entry_box, text=f.read()).pack()
    entry_box.mainloop()
    
    
#-----------------------------------------UI Setup------------------------------------------#

def btn_clicked():
    print("Button Clicked")


window = Tk()
window.title("RPGen Password Manager (@samunicode)")
window.iconbitmap('media/favicon_rpgen.ico')

window.geometry("864x486")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 486,
    width = 864,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"media/background.png")
background = canvas.create_image(
    432.0, 239.0,
    image=background_img)

entry0_img = PhotoImage(file = f"media/img_textBox0.png")
entry0_bg = canvas.create_image(
    697.5, 133.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)
entry0.insert(0,"Ex. www.sameerchauhan.in") #to keep frequently used data pre inserted

entry0.place(
    x = 555.0, y = 120,
    width = 285.0,
    height = 24)

entry1_img = PhotoImage(file = f"media/img_textBox1.png")
entry1_bg = canvas.create_image(
    697.5, 196.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)
entry1.insert(0,"Ex. sameerchauhan@mail.com") #to keep frequently used data pre inserted

entry1.place(
    x = 555.0, y = 183,
    width = 285.0,
    height = 24)

entry2_img = PhotoImage(file = f"media/img_textBox2.png")
entry2_bg = canvas.create_image(
    697.5, 252.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry2.place(
    x = 555.0, y = 239,
    width = 285.0,
    height = 24)

img0 = PhotoImage(file = f"media/img0.png")
b0 = Button(command=password_generator,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b0.place(
    x = 657, y = 274,
    width = 189,
    height = 27)

img1 = PhotoImage(file = f"media/img1.png")
b1 = Button(command=save_data,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b1.place(
    x = 553, y = 358,
    width = 72,
    height = 30)

img4 = PhotoImage(file = f"media/img4.png")
b2 = Button(command=about_dev,
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b2.place(
    x = 773, y = 358,
    width = 72,
    height = 30)

img5 = PhotoImage(file = f"media/img5.png")
b3 = Button(command=view_entries,
       image = img5,
       borderwidth = 0,
       highlightthickness = 0,
       relief = "flat")

b3.place(
       x = 335, y = 358, width = 72, height = 30)


window.resizable(False, False)
window.mainloop()
