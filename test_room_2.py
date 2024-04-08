import customtkinter
import sys


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


app = customtkinter.CTk()
app.geometry("350x350")


def login():
    log = entre_1.get()
    password  = entre_2.get()

    print(f"login test Bienvenue: {log}")
    print("Password: ",password)


def exit():
    print("Exit")
    sys.exit()

def slider(value):
    print(value)


frame = customtkinter.CTkFrame(master=app)
frame.pack(padx=60,pady=20,fill="both",expand=True)

label= customtkinter.CTkLabel(master=frame,text="Login System",font=("Roboto",24))
label.pack(padx=10,pady=12)


entre_1 = customtkinter.CTkEntry(master=frame,placeholder_text="Username")
entre_1.pack(padx=10,pady=12)
entre_2 = customtkinter.CTkEntry(master=frame,placeholder_text="Password",show="*")
entre_2.pack(padx=10,pady=12)


button_login = customtkinter.CTkButton(master=frame,text="Login",command=login)
button_login.pack(padx=10,pady=12)

button_exit = customtkinter.CTkButton(master=frame,text="Exit",command=exit)
button_exit.pack(padx=10,pady=12)

checkbox =  customtkinter.CTkCheckBox(master=frame,text="Remenber me ")
checkbox.pack(padx=10,pady=12)

slider = customtkinter.CTkSlider(master=frame,from_=0, to=100, command= slider )
slider.pack(padx=10,pady=12)


app.mainloop()