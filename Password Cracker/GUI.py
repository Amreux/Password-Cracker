import customtkinter
from functions import main,username_and_password_main
import time
def default_passwords_list_checker():

    if(default_passwords_list_checkbox_value.get()=="checked"): 
        passwords_list_path_button.configure(state='disabled')
        passworsd_list_path_entry.configure(state='disabled')
    else:
        passwords_list_path_button.configure(state='active')
        passworsd_list_path_entry.configure(state='normal')

def default_usrnames_list_checker():

    if(default_usernames_list_checkbox_value.get()=="checked"): 

        usernames_list_path_button.configure(state='disabled')
        usernames_list_path_entry.configure(state='disabled')
    else:

        usernames_list_path_button.configure(state='active')
        usernames_list_path_entry.configure(state='normal')

def usernames_cracking_checker():
    if(mod_of_op.get()=="checked"):
        usernames_list_default_button.configure(state='normal')
        usernames_list_path_button.configure(state='active')
        usernames_list_path_entry.configure(state='normal')
        username_entry.configure(state='disabled')
    else:
        usernames_list_default_button.configure(state='disabled')
        usernames_list_path_button.configure(state='disabled')
        usernames_list_path_entry.configure(state='disabled')
        default_usernames_list_checkbox_value.set("unchecked")
        username_entry.configure(state='normal')


def status_code__button_checker():
    if(status_code_detetection_only_value.get()=="checked"):
        failure_message_entry.configure(state="disabled")
    else:
        failure_message_entry.configure(state="normal")

def password_conditions_checker():
    if(password_conditions_checkbox_value.get()=="checked"):
        password_length_button.configure(state="normal")
        substring_in_password_button.configure(state="normal")
        password_length_checkbox_value.set("unchecked")
        substring_in_password_checkbox_value.set("unchecked")
    else:
        password_length_button.configure(state="disabled")
        password_length_combo_box.configure(state="disabled")
        substring_in_password_button.configure(state="disabled")
        substring_in_password_entry.configure(state="disabled")

def time_limit_button_checker():
    if(time_limit_button_value.get()=="checked"):
        time_limit_combo_box.configure(state="normal")
    else:
        time_limit_combo_box.configure(state="disabled")


def password_length_button_checker():
    if(password_length_checkbox_value.get()=="checked"):
        password_length_combo_box.configure(state="normal")
    else:
        password_length_combo_box.configure(state="disabled")

def substring_in_password_button_checker():
    if(substring_in_password_checkbox_value.get()=="checked"):
        substring_in_password_entry.configure(state="normal")
    else:
        substring_in_password_entry.configure(state="disabled")
    
def main_function():

    passwords=open(passwords_list_path.get(),'r',encoding="latin-1").read().splitlines()
    if(password_length_combo_box.cget("state")=="normal" and password_length.get()!=""):
        passwords=list(filter(lambda x: str(len(x))==password_length.get(),passwords))
    
    if(substring_in_password_entry.cget("state")=="normal" and substring_in_password.get()!=None):
        passwords=list(filter(lambda x: substring_in_password.get() in x ,passwords))

    
    if(mod_of_op.get()=="unchecked"):
        password_found=main(passwords=passwords,URL=url.get(),username=username.get(),username_field_name=username_field_name.get(),num_of_threads=6,password_field_name=password_field_name.get(),failure_message=failure_message)
        print(password_found)
    else:
        login_data=username_and_password_main(URL=url.get(),usernames_list_path=usernames_list_path.get(),passwords=passwords,username_field_name=username_field_name.get(),password_field_name=password_field_name.get(),num_of_threads=6,failure_message=failure_message.get())
        print(login_data)


############################################################## configuration ########################################################################

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root_window=customtkinter.CTk()
root_window.geometry("1200x450")
root_window.title("password cracker")
root_window.resizable(width=False,height=False)

root_window.grid_rowconfigure(list(range(0,11)),weight=1)
root_window.grid_columnconfigure(list(range(0,10)),weight=1)

#############################################  variables #########################################################################################

#main frame variables
default_passwords_list_checkbox_value=customtkinter.Variable()
default_usernames_list_checkbox_value=customtkinter.Variable()
passwords_list_path=customtkinter.Variable()
usernames_list_path=customtkinter.Variable()
mod_of_op=customtkinter.Variable()
url=customtkinter.StringVar()
username=customtkinter.StringVar()
username_field_name=customtkinter.StringVar()
password_field_name=customtkinter.StringVar()

#password conditions variable
password_conditions_checkbox_value=customtkinter.Variable()
password_length=customtkinter.Variable()
password_length_checkbox_value=customtkinter.Variable()
substring_in_password=customtkinter.StringVar()
substring_in_password_checkbox_value=customtkinter.Variable()

#failure message frame
failure_message=customtkinter.StringVar()
status_code_detetection_only_value=customtkinter.Variable()


#time limit frame
time_limit_button_value=customtkinter.Variable()
time_limit=customtkinter.Variable()

################################################### main frame ###################################################################################
main_frame=customtkinter.CTkFrame(root_window)
main_frame.grid(row=0,column=0,rowspan=9,columnspan=6,padx=15,pady=15)


url_label=customtkinter.CTkLabel(main_frame,text="URL")
url_label.grid(row=0,column=0,pady=(20,0),padx=(20,0))


url_entry=customtkinter.CTkEntry(main_frame,placeholder_text="type the url here",width=300,textvariable=url)
url_entry.grid(row=0,column=1,pady=(20,0),columnspan=3,padx=(10,0))


username_label=customtkinter.CTkLabel(main_frame,text="Username")
username_label.grid(row=1,column=0,padx=(10,0),pady=(20,0))

username_entry=customtkinter.CTkEntry(main_frame,placeholder_text="type the username her",width=300,textvariable=username)
username_entry.grid(row=1,column=1,columnspan=3,padx=(10,0),pady=(20,0))

passwords_list_label=customtkinter.CTkLabel(main_frame,text="Passwords List")
passwords_list_label.grid(row=2,column=0,columnspan=1,padx=(10,0),pady=(20,0))

passworsd_list_path_entry=customtkinter.CTkEntry(main_frame,width=300,textvariable=passwords_list_path)
passworsd_list_path_entry.grid(row=2,column=1,columnspan=3,padx=(10,0),pady=(20,0))

passwords_list_path_button=customtkinter.CTkButton(main_frame,text="Browse",width=70,command=lambda:passwords_list_path.set(customtkinter.filedialog.askopenfilename()))
passwords_list_path_button.grid(row=2,column=4,padx=(10,0),pady=(20,0))

passwords_list_default_button=customtkinter.CTkCheckBox(main_frame,text="Default",variable=default_passwords_list_checkbox_value,command=lambda:default_passwords_list_checker(),onvalue="checked",offvalue="unchecked")
passwords_list_default_button.grid(row=2,column=5,columnspan=1,padx=(10,10),pady=(20,0))

mod_op_op_checkbox=customtkinter.CTkCheckBox(main_frame,text="Username Cracking",onvalue="checked",offvalue="unchecked",variable=mod_of_op,command=lambda:usernames_cracking_checker())
mod_op_op_checkbox.grid(row=3,column=0,columnspan=2,padx=(10,0),pady=(20,0))

usernames_list_label=customtkinter.CTkLabel(main_frame,text="Usernames List")
usernames_list_label.grid(row=4,column=0,columnspan=1,padx=(10,0),pady=(20,0))

usernames_list_path_entry=customtkinter.CTkEntry(main_frame,width=300,textvariable=usernames_list_path)
usernames_list_path_entry.grid(row=4,column=1,columnspan=3,padx=(10,0),pady=(20,0))

usernames_list_path_button=customtkinter.CTkButton(main_frame,text="Browse",width=70,command=lambda:usernames_list_path.set(customtkinter.filedialog.askopenfilename()))
usernames_list_path_button.grid(row=4,column=4,columnspan=1,padx=(10,0),pady=(20,0))

usernames_list_default_button=customtkinter.CTkCheckBox(main_frame,text="Default",variable=default_usernames_list_checkbox_value,onvalue="checked",offvalue="unchecked",command=lambda:default_usrnames_list_checker())
usernames_list_default_button.grid(row=4,column=5,columnspan=1,padx=(10,0),pady=(20,0))



username_field_name_label=customtkinter.CTkLabel(main_frame,text="Username Field Name")
username_field_name_label.grid(row=5,column=0,columnspan=1,padx=(10,0),pady=(20,0))

username_field_name_entry=customtkinter.CTkEntry(main_frame,placeholder_text="type here the username field name",width=300,textvariable=username_field_name)
username_field_name_entry.grid(row=5,column=1,columnspan=3,padx=(10,0),pady=(20,0))

password_field_name_label=customtkinter.CTkLabel(main_frame,text="Password Field Name")
password_field_name_label.grid(row=6,column=0,columnspan=1,padx=(10,0),pady=(20,0))

password_field_name_entry=customtkinter.CTkEntry(main_frame,placeholder_text="type here the password field name",width=300,textvariable=password_field_name)
password_field_name_entry.grid(row=6,column=1,columnspan=3,padx=(10,0),pady=(20,20))


################################################################## passwords condition frame ####################################################################
passwords_conditions_frame=customtkinter.CTkFrame(root_window)
passwords_conditions_frame.grid(row=0,column=6,columnspan=4,padx=(0,20),pady=(15,5),rowspan=4)

conditions_on_password_button=customtkinter.CTkSwitch(passwords_conditions_frame,text="Password Condidtion",variable=password_conditions_checkbox_value,onvalue="checked",offvalue="unchecked",command=lambda:password_conditions_checker())
conditions_on_password_button.grid(row=0,column=6,columnspan=4,pady=(15,10),padx=(10,0))

password_length_label=customtkinter.CTkLabel(master=passwords_conditions_frame,text="Password Length")
password_length_label.grid(row=1,column=6,columnspan=1,padx=(20,0),pady=(10,0))

password_length_combo_box=customtkinter.CTkComboBox(passwords_conditions_frame,values=list(map(str,range(8,20))),variable=password_length)
password_length_combo_box.grid(row=1,column=7,columnspan=2,padx=(20,0),pady=(10,0))

password_length_button=customtkinter.CTkSwitch(passwords_conditions_frame,text="",onvalue="checked",offvalue="unchecked",variable=password_length_checkbox_value,command=lambda:password_length_button_checker())
password_length_button.grid(row=1,column=9,columnspan=1,padx=(20,0),pady=(10,0))


substring_in_password_label=customtkinter.CTkLabel(passwords_conditions_frame,text="A sub string in the password")
substring_in_password_label.grid(row=2,column=6,columnspan=1,padx=(20,0),pady=10)

substring_in_password_entry=customtkinter.CTkEntry(passwords_conditions_frame,textvariable=substring_in_password)
substring_in_password_entry.grid(row=2,column=7,columnspan=2,padx=(20,0))

substring_in_password_button=customtkinter.CTkSwitch(passwords_conditions_frame,text="",onvalue="checked",offvalue="unchecked",variable=substring_in_password_checkbox_value,command=lambda:substring_in_password_button_checker())
substring_in_password_button.grid(row=2,column=9,columnspan=1,padx=(20,0),pady=10)


##############################################################  failure detection ########################################################################

failure_detection_frame=customtkinter.CTkFrame(root_window)
failure_detection_frame.grid(row=4,column=6,columnspan=4,rowspan=3,padx=(0,20),pady=(0,5),sticky="n")

failure_message_label=customtkinter.CTkLabel(failure_detection_frame,text="Failure Message")
failure_message_label.grid(row=0,column=0,columnspan=1,padx=(20,0),pady=20)

failure_message_entry=customtkinter.CTkEntry(failure_detection_frame,placeholder_text="type here the failure message",width=300,textvariable=failure_message)
failure_message_entry.grid(row=0,column=1,columnspan=3,padx=(20,20),pady=20)

status_code_label=customtkinter.CTkLabel(failure_detection_frame,text="Detect failure from the status code only")
status_code_label.grid(row=1,column=0,columnspan=2,padx=20,pady=(0,20),sticky="w")

status_code_detection_button=customtkinter.CTkSwitch(failure_detection_frame,text="",variable=status_code_detetection_only_value,onvalue="checked",offvalue="unchecked",command=lambda:status_code__button_checker())
status_code_detection_button.grid(row=1,column=2,columnspan=2,padx=(20,0),pady=(0,20),sticky="e")
######################################################################################################################################

time_limit_frame=customtkinter.CTkFrame(root_window)
time_limit_frame.grid(row=7,column=6,columnspan=4,rowspan=1,padx=(0,20),pady=(0,5))


time_limit_label=customtkinter.CTkLabel(time_limit_frame,text="Time Limit",width=100)
time_limit_label.grid(row=0,column=0,columnspan=1,padx=(0,0),pady=(20,20))

time_limit_combo_box=customtkinter.CTkComboBox(time_limit_frame,values=list(map(str,range(1,60))),width=200,variable=time_limit)
time_limit_combo_box.grid(row=0,column=1,columnspan=1,padx=(20,10),pady=(20,20),sticky="nsew")

time_limit_button=customtkinter.CTkSwitch(time_limit_frame,text="",onvalue="checked",offvalue="checked",variable=time_limit_button_value,command=lambda:time_limit_button_checker())
time_limit_button.grid(row=0,column=2,columnspan=2,padx=(20,0),pady=20,sticky="e")

######################################################################################################################################
submit_button=customtkinter.CTkButton(root_window,text="Start",command=lambda:main_function())
submit_button.grid(row=10,column=0,columnspan=11,pady=(10,15),rowspan=1,)



####################### intialization of checkboxes and switches###################################
usernames_cracking_checker()
password_conditions_checker()
password_length_button_checker()
time_limit_button_checker()
######################################################################################################################################


root_window.mainloop()
