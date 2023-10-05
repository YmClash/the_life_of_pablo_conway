import customtkinter as custom
import sys


def hallo():
    print("Hallo Ymc ")

def exit():
    print("exit")
    sys.exit()

custom.set_appearance_mode("dark")

app =  custom.CTk()
app.title("The life  of Pablo")
app.geometry("400x400")

# textbox = custom.CTkTextbox(app,width=100,height=150,fg_color="black")
# textbox.configure()
# textbox.grid(row=0,column=1)

entre = custom.CTkEntry(app,width=50,height=20,placeholder_text="Entre")


#
# button_run = custom.CTkButton(app, text="run",bg_color="black",command= hallo)
# button_run.grid(row=0,column=0,padx=20,pady=20)
#
# button_exit =  custom.CTkButton(app,text="Exit",bg_color="black",command=exit)
# button_exit.grid(row=0,column=1,padx=20,pady=20,sticky="ew")






app.mainloop()