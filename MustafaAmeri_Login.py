from tkinter import *
import tkinter.messagebox as messagebox
import customtkinter  
import pandas as pd
import re
from PIL import Image,ImageTk


customtkinter.set_appearance_mode("dark")


customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("500x500")
root.title("User Information Form")
root.resizable(False, False) 


file_path = r"D:/user_info.xlsx"




def btn_Save():
    first_name = input_FirstName.get()
    last_name = input_LastName.get()
    National_ID = input_National_ID.get()
    age = input_Age.get()
    city = input_City.get()
    phone = input_Phone.get()
    email = input_Email.get()

    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    regex_mobile = r'^09[0-9]{9}$'

    if len(first_name) < 1:
        messagebox.showerror("Error" , "please enter your First Name")
    elif len(last_name) < 1:
        messagebox.showerror("Error" , "please enter your Last Name")
    elif len(National_ID) < 1:
        messagebox.showerror("Error" , "please enter your National ID")
    elif len(age) < 1:
        messagebox.showerror("Error" , "please enter your Age")
    elif not(age.isdigit()):
        messagebox.showerror("Error" , "please enter a valid Age")
    elif len(city) < 1:
        messagebox.showerror("Error" , "please enter your City")
    elif len(phone) < 1:
        messagebox.showerror("Error" , "please enter your Phone")
    elif not re.match(regex_mobile, phone):
        messagebox.showerror("Error", "please enter a valid Phone number")
    elif len(email) < 1:
        messagebox.showerror("Error" , "please enter your Email")
    elif not( re.match(regex, email) ):
        messagebox.showerror("Error" , "please enter a valid Email")
    else:
        input_FirstName.delete(0, END)
        input_LastName.delete(0, END)
        input_National_ID.delete(0, END)
        input_Age.delete(0, END)
        input_City.delete(0, END)
        input_Phone.delete(0, END)
        input_Email.delete(0, END)


      
        df_new = pd.DataFrame({
            "First Name": (first_name,),
            "Last Name": (last_name,),
            "National_ID": (National_ID,),
            "Age": (age,),
            "City": (city,),
            "Phone Number": (phone,),
            "Email": (email,),
        })

       
        
        try:

            df_existing = pd.read_excel(file_path, dtype=str)
            
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
            
         
            df_combined.to_excel(file_path, index=False)
        except FileNotFoundError:
         
            df_new.to_excel(file_path, index=False)

    messagebox.showinfo("Save successful", "The information was successfully saved.")



def search_data():
    search_id = input_search_National_ID.get()

    try:
        df = pd.read_excel(file_path, dtype=str)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return

    if search_id.isdigit() and len(search_id) > 0:
        result = df[df['National_ID'] == search_id]
        if not result.empty:
            info = result.iloc[0]
            result_text = f"First Name: {info['First Name']}\nLast Name: {info['Last Name']}\nNational ID: {info['National_ID']}\nAge: {info['Age']}\nCity: {info['City']}\nPhone Number: {info['Phone Number']}\nEmail: {info['Email']}"
            label_result.configure(text=result_text)
        else:
            label_result.configure(text="No result found.")
    else:
        messagebox.showerror("Error", "Please enter a valid National ID.")







def open_search_window():

    root.withdraw()
    

    search_window = customtkinter.CTkToplevel(root)
    search_window.title("Search Window")
    search_window.geometry("500x500") 
    search_window.resizable(False, False)


    frame_search =customtkinter.CTkFrame(master=search_window , width=320, height=400, corner_radius=15)
    frame_search.place(x=100,y=40)

    title_search =customtkinter.CTkLabel(master=frame_search ,text="For the search, please enter the national ID number: ",font=("tahoma",13),text_color="cbb5f7")
    title_search.place(x=10,y=15)

    Label_search_National_ID = customtkinter.CTkLabel(master=frame_search,width=60,text='National ID',text_color="#8e57fa")
    Label_search_National_ID.place(x=10,y=55)
    global input_search_National_ID
    input_search_National_ID=customtkinter.CTkEntry(master=frame_search,width=220,placeholder_text="National ID",border_color='#5c1bd4')
    input_search_National_ID.place(x=90,y=55)



    global label_result
    label_result = customtkinter.CTkLabel(master=frame_search, text="", width=280, height=200, text_color="white", anchor="w", justify="left")
    label_result.place(x=10, y=135)


    button_frame_search=customtkinter.CTkButton(text='Search',master=frame_search,width=300,height=30,corner_radius=6,text_color='white',hover_color='#713cd2',fg_color='#6429d1',compound='left' ,command=search_data)
    button_frame_search.place(x=10,y=95)








    def on_closing():
        root.deiconify()  
        search_window.destroy()  

    search_window.protocol("WM_DELETE_WINDOW", on_closing)






frame=customtkinter.CTkFrame(master=root , width=320, height=400, corner_radius=15)
frame.place(x=100,y=40)
title=customtkinter.CTkLabel(master=frame,text="Enter Your Information",font=("tahoma",20),text_color="#cbb5f7")
title.place(x=70,y=15)

Label_FirstName = customtkinter.CTkLabel(master=frame,width=60,text='First Name',text_color="#8e57fa")
Label_FirstName.place(x=10,y=70)
input_FirstName=customtkinter.CTkEntry(master=frame,width=220,placeholder_text="First Name",border_color='#5c1bd4')
input_FirstName.place(x=90,y=70)


Label_LastName = customtkinter.CTkLabel(master=frame,width=60,text='Last Name',text_color="#8e57fa")
Label_LastName.place(x=10,y=110)
input_LastName=customtkinter.CTkEntry(master=frame,width=220,placeholder_text="Last Name",border_color='#5c1bd4')
input_LastName.place(x=90,y=110)


Label_National_ID = customtkinter.CTkLabel(master=frame,width=60,text='National ID',text_color="#8e57fa")
Label_National_ID.place(x=10,y=150)
input_National_ID=customtkinter.CTkEntry(master=frame,width=220,placeholder_text="National ID",border_color='#5c1bd4')
input_National_ID.place(x=90,y=150)

Label_Age = customtkinter.CTkLabel(master=frame,width=60,text='Age',text_color="#8e57fa")
Label_Age.place(x=10,y=190)
input_Age=customtkinter.CTkEntry(master=frame,width=220,placeholder_text="Age",border_color='#5c1bd4')
input_Age.place(x=90,y=190)

Label_City = customtkinter.CTkLabel(master=frame,width=60,text='City',text_color="#8e57fa")
Label_City.place(x=10,y=230)
input_City=customtkinter.CTkEntry(master=frame,width=220,placeholder_text="City",border_color='#5c1bd4')
input_City.place(x=90,y=230)



Label_Phone = customtkinter.CTkLabel(master=frame,width=60,text='Phone',text_color="#8e57fa")
Label_Phone.place(x=10,y=270)
input_Phone=customtkinter.CTkEntry(master=frame,width=220,placeholder_text="Phone",border_color='#5c1bd4')
input_Phone.place(x=90,y=270)


Label_Email = customtkinter.CTkLabel(master=frame,width=60,text='Email',text_color="#8e57fa")
Label_Email.place(x=10,y=310)
input_Email=customtkinter.CTkEntry(master=frame,width=220,placeholder_text="Email",border_color='#5c1bd4')
input_Email.place(x=90,y=310)


button_Save = customtkinter.CTkButton(text='Save',master=frame,width=100,height=30,corner_radius=6,text_color='white',hover_color='#713cd2',fg_color='#6429d1' ,command=btn_Save)
button_Save.place(x=50,y=350)


button_Search=customtkinter.CTkButton(text='Search',master=frame,width=100,height=30,corner_radius=6,text_color='#6429d1',hover_color='#bea2f5',fg_color='white',compound='left' ,command=open_search_window)
button_Search.place(x=160,y=350)



root.mainloop()
