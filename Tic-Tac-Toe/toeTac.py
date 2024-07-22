import customtkinter as tk
# import tkinter as tk


app = tk.CTk()
app.title("TicTacToe by YmC")
app.geometry("425x575")
app.configure(bg="black")


def press():
    for column in range(3):
        for row in range(3):
           print(f"Button {row} {column} pressed")


def draw_grid():
    for column in range(3):
        for row in range(3):
            button = tk.CTkButton(app,text="X",font=("Roboto",150),command=press)
            button.grid(row=row,column=column)



draw_grid()









app.mainloop()