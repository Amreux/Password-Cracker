import tkinter as tk
from tkinter import ttk ,messagebox

def default_word_list_checker():
    if(default_word_list_value.get()=="checked"):
        word_list_entry.configure(state=['disabled'])
    else:
        word_list_entry.configure(state=['active'])

def mod_of_op_checker():
    if(mod_of_op_value.get()=="checked"):
        Username_entry.configure(state=['disabled'])
        Username_wordlist_entry.configure(state=['active'])
        default_usernames_wordlist_checkbutton.configure(state=['active'])
    else:
        Username_entry.configure(state=['active'])
        Username_wordlist_entry.configure(state=['disabled'])
        default_usernames_wordlist_checkbutton.configure(state=['disabled'])
        default_username_word_list_value.set('unchecked')

def default_username_word_list_checker():
    if(default_username_word_list_value.get()=="checked" and mod_of_op_value.get()=="checked"):
        Username_wordlist_entry.configure(state=['disabled'])
    else:
        Username_wordlist_entry.configure(state=['active'])




window=tk.Tk()
window.title("Password Cracker")
window.geometry("550x300")

URL=tk.StringVar()
word_list_path=tk.StringVar()
default_word_list_value=tk.Variable()
mod_of_op_value=tk.Variable()
username_value=tk.StringVar()
default_username_word_list_value=tk.Variable()

URL_label=ttk.Label(window,text="URL")
URL_label.grid(row=0,column=0,columnspan=10,padx=10,pady=10)

URL_entry=ttk.Entry(window,width=35,textvariable=URL)
URL_entry.grid(row=0,column=10,columnspan=20,padx=10,pady=10,)

Username_label=ttk.Label(window,text="username")
Username_label.grid(row=1,column=0,columnspan=10,padx=10,pady=10)

Username_entry=ttk.Entry(window,width=35,textvariable=username_value)
Username_entry.grid(row=1,column=10,columnspan=20,padx=10,pady=10)

Username_wordlist_label=ttk.Label(window,text="Username Wordlist Path")
Username_wordlist_label.grid(row=2,column=0,columnspan=10,padx=10,pady=10)

Username_wordlist_entry=ttk.Entry(window,width=35)
Username_wordlist_entry.grid(row=2,column=10,columnspan=20,padx=10,pady=10)

default_usernames_wordlist_checkbutton=ttk.Checkbutton(window,text="Default",variable=default_username_word_list_value,onvalue="checked",offvalue="unchecked",command=lambda:default_username_word_list_checker())
default_usernames_wordlist_checkbutton.grid(row=2,column=30,columnspan=15,padx=10,pady=10)


Mod_of_op_checkbutton=ttk.Checkbutton(window,text="crack both username and password",variable=mod_of_op_value,onvalue="checked",offvalue="unchecked",command=lambda:mod_of_op_checker())
Mod_of_op_checkbutton.grid(row=3,column=0,columnspan=25,padx=10,pady=10)
mod_of_op_value.set('unchecked')
mod_of_op_checker()


word_list_label=ttk.Label(window,text="Wordlist Path")
word_list_label.grid(row=5,column=0,columnspan=10,padx=10,pady=10)

word_list_entry=ttk.Entry(window,width=35,textvariable=word_list_path)
word_list_entry.grid(row=5,column=10,columnspan=20,padx=10,pady=10)

default_word_list_checkbox=ttk.Checkbutton(window,text="Default",variable=default_word_list_value,onvalue="checked",offvalue="unchecked",command=lambda:default_word_list_checker())
default_word_list_checkbox.grid(row=5,column=30,columnspan=15,padx=10,pady=10)

button=ttk.Button(window,text="let's crack",command=lambda:messagebox.showinfo(title="success",message=" username : admin \n password : password "))
button.grid(row=7,column=0,columnspan=50,pady=20)

window.mainloop()