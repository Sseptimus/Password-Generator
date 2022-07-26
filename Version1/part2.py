from tkinter import *
import json
import math
from functools import partial
with open('Password-Generator\Version1\Password-Generator-Data.json', 'r') as f:
  data = json.load(f)
  
passwords = data[0]
accounts = data[1]
usernames = data[2]
password_labels = []
account_labels = []
username_labels = []
view_buttons = []
tabs = []
show_buttons = []
current_page = 1
total_pages = 0
class Page(Tk):
    def setup(self):
        global focus_check,tabBackground,pages
        pages = self
        self.title("Password Manager")
        self.configure(background="#0e0118")
        self.bind("<Escape>", lambda event: self.destroy())
        focus_check = BooleanVar()
        self.bind('<FocusIn>', lambda _: focus_check.set(True))
        self.bind('<FocusOut>', lambda _: focus_check.set(False))
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        geometry = "700x500+" + str(int(screen_width/2 - 350)) + "+" + str(int(screen_height/2 - 250))
        self.geometry(geometry)
        self.headerBackground = PhotoImage(file=r"Password-Generator\Assets\Element backgrounds\header_background.png")
        tabBackground = PhotoImage(file=r"Password-Generator\Assets\Element backgrounds\tab_background.png")
        self.set_tabs()
        self.header = Label(self,image=self.headerBackground, borderwidth=0)
        self.header.place(x=0,y=0)
        self.newBackground = PhotoImage(file=r"Password-Generator\Assets\Element backgrounds\new_password.png")
        self.add_password = Button(self,image=self.newBackground, width=50,height=50,borderwidth=0,command=self.new_password)
        self.add_password.place(y=37,x=530)
        self.next_button = Button(self,text="→",font=("Arial", 15), background="#0e0118", foreground="#ffffff",command=self.next_page)
        self.next_button.place(y=460,x=660)
        self.previous_button = Button(self,text="←",font=("Arial", 15), background="#0e0118", foreground="#ffffff",command=self.previous_page)
        self.previous_button.place(y=460,x=20)
        
            
    def new_password(self):
        global generate_button, manual_button, account_input, username_input, password_input, new_window
        new_window = Toplevel(self)
        new_window.grab_set()
        new_window.focus_set()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        geometry = "400x370+" + str(int(screen_width/2 - 200)) + "+" + str(int(screen_height/2 - 185))
        new_window.geometry(geometry)
        new_window.title("New Password")
        new_window.configure(background="#0e0118")
        account_name = Label(new_window, text="Account Name:", font=("Arial", 15), background="#0e0118", foreground="#ffffff")
        account_name.place(x=25,y=25)
        account_input = Entry(new_window, width=30, font=("Arial", 15), background="#0e0118", foreground="#ffffff")
        account_input.place(x=25,y=75)
        username_name = Label(new_window, text="Username:", font=("Arial", 15), background="#0e0118", foreground="#ffffff")
        username_name.place(x=25,y=125)
        username_input = Entry(new_window, width=30, font=("Arial", 15), background="#0e0118", foreground="#ffffff")
        username_input.place(x=25,y=175)
        password_name = Label(new_window, text="Password:", font=("Arial", 15), background="#0e0118", foreground="#ffffff")
        password_name.place(x=25,y=225)
        password_input = Entry(new_window, width=30, font=("Arial", 15), background="#0e0118", foreground="#ffffff")
        password_input.place(x=25,y=275)
        done_button = Button(new_window, text="Add password", font=("Arial", 15), background="#0e0118", foreground="#ffffff",command= lambda: Page.new_password_entry())
        done_button.place(x=25,y=325)

        
    def next_page(self):
        global current_page, total_pages
        if current_page == total_pages:
            return
        current_page += 1
        
        
        
        print(current_page)
        for i in password_labels:
            
            if password_labels.index(i) >= current_page*3-3 and password_labels.index(i) <= current_page*3-1:
                i.place(x=490,y=155+(password_labels.index(i)-((current_page-1)*3))*100)
            else:
                i.place(x=1000,y=1000)
        for i in account_labels:
            if account_labels.index(i) >= current_page*3-3 and account_labels.index(i) <= current_page*3-1:
                i.place(x=20,y=155+(account_labels.index(i)-((current_page-1)*3))*100)
            else:
                i.place(x=1000)
        for i in view_buttons:
            if  view_buttons.index(i) >= current_page*3-3 and view_buttons.index(i) <= current_page*3-1:
                i.place(x=540,y=155+(view_buttons.index(i)-((current_page-1)*3))*100)
            else:
                i.place(x=1000)
                               
                
    def previous_page(self):
        global current_page, total_pages
        if current_page == 1:
            return
        current_page -= 1
        for i in password_labels:
            if password_labels.index(i) >= current_page*3-3 and password_labels.index(i) <= current_page*3-1:
                i.place(x=500,y=155+(password_labels.index(i)-((current_page-1)*3))*100)
            else:
                i.place(x=1000)
        for i in account_labels:
            if account_labels.index(i) >= current_page*3-3 and account_labels.index(i) <= current_page*3-1:
                i.place(x=20,y=155+(account_labels.index(i)-((current_page-1)*3))*100)
            else:
                i.place(x=1000)
                
                
    def manuel_entry(self):
        global password_input,current_page
        generate_button.place_forget()
        manual_button.place_forget()
        password_input = Entry(new_window, width=30, font=("Arial", 15), background="#0e0118", foreground="#ffffff")
        password_input.place(x=25,y=275)
        done_button = Button(new_window, text="Add password", font=("Arial", 15), background="#0e0118", foreground="#ffffff",command= lambda: Page.new_password_entry())
        done_button.place(x=25,y=325)
        current_page = 1
        for i in password_labels:
            i.place_forget()
        for i in account_labels:
            i.place_forget()
        page.set_tabs()
        
    def set_tabs(self):
        global total_pages
        total_pages = math.ceil(len(passwords)/3)
        view_background = PhotoImage(file=r"Password-Generator\Assets\Element backgrounds\hidden_password.png")
        for i in passwords:
            
            if passwords.index(i) < 3:
                tabs.append(Label(pages, text="Text",width=700,height=100, image = tabBackground,borderwidth=0))
                tabs[passwords.index(i)].place(x=0,y=125+passwords.index(i)*100)
                account_labels.append(Label(pages, text=accounts[passwords.index(i)],font=("Arial", 20),fg="#ffffff", background="#0e0118"))
                account_labels[passwords.index(i)].place(x=20,y=155+passwords.index(i)*100)
                password_labels.append(Label(pages, text=len(i)*("*"),font=("Arial", 20),fg="#ffffff", background="#0e0118"))
                view_buttons.append(Button(pages, command= partial(page.popup,passwords.index(i)),text = "View Password", font=("Arial", 15),background="#0e0118", foreground="#ffffff"))
                view_buttons[passwords.index(i)].place(x=540,y=155+passwords.index(i)*100)
                if len(i) > 6:
                    password_labels[-1].config(text="******")
                    password_labels[-1].place(x=490-36,y=155+passwords.index(i)*100)
                else:
                    password_labels[-1].place(x=490-len(i)*5,y=155+passwords.index(i)*100)
            else: 
                tabs.append(Label(pages, text="Text",width=700,height=100, image = tabBackground,borderwidth=0))
                tabs[passwords.index(i)].place(x=700*(total_pages-1),y=125+(passwords.index(i)-(total_pages*3))*100)
                account_labels.append(Label(pages, text=accounts[passwords.index(i)],font=("Arial", 20),fg="#ffffff", background="#0e0118"))
                account_labels[passwords.index(i)].place(x=700*(total_pages-1)+20,y=155+(passwords.index(i)-(total_pages*3))*100)
                password_labels.append(Label(pages, text=len(i)*("*"),font=("Arial", 20),fg="#ffffff", background="#0e0118"))
                view_buttons.append(Button(pages,command= partial(page.popup,passwords.index(i)),text = "View Password", font=("Arial", 15),background="#0e0118", foreground="#ffffff"))
                view_buttons[passwords.index(i)].place(x=540,y=155+(passwords.index(i)-(total_pages*3))*100)
                if len(i) > 6:
                    password_labels[-1].config(text="******")
                    password_labels[-1].place(x=490-36+700*(total_pages-1),y=155+(passwords.index(i)-(total_pages*3))*100)
                else:
                    password_labels[-1].place(x=490-len(i)*5+700*(total_pages-1),y=155+(passwords.index(i)-(total_pages*3))*100)

        
    def new_password_entry():
        passwords.append(password_input.get())
        accounts.append(account_input.get())
        usernames.append(username_input.get())
        data[0] = passwords
        data[1] = accounts
        data[2] = usernames
        with open('Password-Generator\Version1\Password-Generator-Data.json', 'w') as outfile:
            json.dump(data, outfile)
        tabs.append(Label(pages,width=700,height=100, image = tabBackground,borderwidth=0))
        account_labels.append(Label(pages, text=account_input.get(),font=("Arial", 20),fg="#ffffff", background="#0e0118"))
        if len(password_input.get()) > 6:
            password_labels.append(Label(pages, text="******",font=("Arial", 20),fg="#ffffff", background="#0e0118"))
        else:
            password_labels.append(Label(pages, text=len(password_input.get())*("*"),font=("Arial", 20),fg="#ffffff", background="#0e0118"))
        new_window.destroy()

    def popup(self,location):
        
        info_window = Toplevel(self)
        info_window.grab_set()
        info_window.focus_set()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        info_window.configure(background="#0e0118")
        geometry = "400x370+" + str(int(screen_width/2 - 200)) + "+" + str(int(screen_height/2 - 185))
        info_window.geometry(geometry)
        info_window.title("View Information")
        account_title = Label(info_window, text="Account:",font=("Arial", 20),fg="#ffffff", background="#0e0118")
        account_title.place(x=25,y=25)
        account_info = Label(info_window, text=accounts[location],font=("Arial", 20),fg="#ffffff", background="#0e0118")
        account_info.place(x=25,y=55)
        username_title = Label(info_window, text="Username:",font=("Arial", 20),fg="#ffffff", background="#0e0118")
        username_title.place(x=25,y=85)
        username_info = Label(info_window, text=usernames[location],font=("Arial", 20),fg="#ffffff", background="#0e0118")
        username_info.place(x=25,y=115)
        password_title = Label(info_window, text="Password:",font=("Arial", 20),fg="#ffffff", background="#0e0118")
        password_title.place(x=25,y=145)
        password_info = Label(info_window, text=passwords[location],font=("Arial", 20),fg="#ffffff", background="#0e0118")
        password_info.place(x=25,y=175)
if __name__ == "__main__":
    page = Page()
    page.setup()
    page.mainloop()
    