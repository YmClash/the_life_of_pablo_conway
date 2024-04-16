import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation
from matplotlib.widgets import Button
import customtkinter as custom
import sys



seed = 66

np.random.seed(seed=seed)

# def rerun(event) :
#     global grid
#     grid = np.random.choice([0, 1], size=(gril_X, gril_Y), p=[cell_A, cell_B])
#     ax.clear()
#     nombre_cycle = 0
#     anim.frame_seq = anim.new_frame_seq()
#     #anim.event_source.start()
#     anim.event_source.interval = 200
#     ax.set_title(f"")

custom.set_appearance_mode("dark")
custom.set_default_color_theme("dark-blue")

app = custom.CTk()
app.geometry("500x500")

frame = custom.CTkFrame(master=app)
frame.pack(padx=60,pady=20,fill="both", expand=True)

label =  custom.CTkLabel(master=frame,text="The life of Pablo Conway",font=("Roboto",24))
label.pack(padx=10,pady=12)

entre_grill_x = custom.CTkEntry(master=frame,placeholder_text="Gril_X")
entre_grill_x.pack(padx=10,pady=12)
entre_grill_y =custom.CTkEntry(master=frame,placeholder_text="Gril_Y")
entre_grill_y.pack(padx=10,pady=12)

def grid_size():
    gril_X= entre_grill_x.get()
    gril_Y = entre_grill_y.get()
    print(f'Grille X : {gril_X} '
          f'Grille Y : {gril_Y}')



# les  constante
gril_X = 30
gril_Y = 30




set_button= custom.CTkButton(master=frame,text="Set",command=grid_size)
set_button.pack(padx=10,pady=12)




# Probabilite cellule morte et celulle vivante
cell_A = 0.6
cell_B = 0.4

# les regle

regle_1_a = 2
regle_1_b = 3

regle_2_a = 3
regle_2_b = 0

# compteur
nombre_cycle = 0
cycle_detect = False
etat = []

def print_variable_value():
    print(f"gril x :{gril_X}\n"
          f"gril y : {gril_Y}\n"
          f"cell a : {cell_A}\n"
          f"cell b : {cell_B}\n")
    print("Seed:",seed)


print_button= custom.CTkButton(master=frame,text="Print Type",command=print_variable_value)
print_button.pack(padx=10,pady=12)
# grid = np.zeros((X, Y))
grid = np.random.choice([0, 1], size=(gril_X, gril_Y), p=[cell_A, cell_B])
# grid = np.random.choice([0, 1], size=(entre_grill_x,entre_grill_y), p=[cell_A, cell_B])

fig, ax = plot.subplots()


def exit():
    print("Exit")
    print(nombre_cycle)
    sys.exit()


def update(frame) :
    global grid, nombre_cycle, cycle_detect, etat

    new_grid = np.copy(grid)
    for i in range(gril_X) :
        for o in range(gril_Y) :
            # on compte les voisin vivant
            vivant = np.sum(grid[max(0, i - 1) :min(gril_X, i + 2), max(0, o - 1) :min(gril_Y, o + 2)]) - grid[i, o]
            if grid[i, o] == 1 :
                # regle pour une cellule vivante
                if vivant < regle_1_a or vivant > regle_1_b :
                    new_grid[i, o] = 0
            else :
                # Regle pour une cellule morte
                if vivant == regle_2_a :
                    new_grid[i, o] = 1

    if not cycle_detect :
        etat_current = new_grid.tobytes()
        if etat_current in etat :
            cycle_detect = True
        else :
            etat.append(etat_current)
            nombre_cycle += 1

    grid = new_grid
    ax.imshow(grid, cmap='binary')
    ax.set_title(f'Nombre de Cycle: {nombre_cycle}')
    return ax

###########################################################

# def update(frame) :
#     global grid, nombre_cycle, cycle_detect, etat
#
#     new_grid = np.copy(grid)
#     for i in range(entre_grill_x) :
#         for o in range(entre_grill_y) :
#             # on compte les voisin vivant
#             vivant = np.sum(grid[max(0, i - 1) :min(entre_grill_x, i + 2), max(0, o - 1) :min(entre_grill_y, o + 2)]) - grid[i, o]
#             if grid[i, o] == 1 :
#                 # regle pour une cellule vivante
#                 if vivant < regle_1_a or vivant > regle_1_b :
#                     new_grid[i, o] = 0
#             else :
#                 # Regle pour une cellule morte
#                 if vivant == regle_2_a :
#                     new_grid[i, o] = 1
#
#     if not cycle_detect :
#         etat_current = new_grid.tobytes()
#         if etat_current in etat :
#             cycle_detect = True
#         else :
#             etat.append(etat_current)
#             nombre_cycle += 1
#
#     grid = new_grid
#     ax.imshow(grid, cmap='binary')
#     ax.set_title(f'Nombre de Cycle: {nombre_cycle}')
#     return ax
#



# def rerun(event) :
#     global grid
#     grid = np.random.choice([0, 1], size=(gril_X, gril_Y), p=[cell_A, cell_B])
#     ax.clear()
#     nombre_cycle = 0
#     anim.frame_seq = anim.new_frame_seq()
#     #anim.event_source.start()
#     anim.event_source.interval = 200
#     ax.set_title(f"")


# plateau = plot.figure()
#
# img = plot.imshow(grid, interpolation='nearest', cmap='binary')

# restart_button_ax = plot.axes([0.8, 0.05, 0.1, 0.075])
# restart_button = Button(restart_button_ax, 'Encore')
# restart_button.on_clicked(rerun)


def run():
    anim = animation.FuncAnimation(fig, update, frames=100, interval=200)
    plot.show()

run_button = custom.CTkButton(master=frame,text="Run",command=run)
run_button.pack(padx=10,pady=12)
exit_button = custom.CTkButton(master=frame,text="Exit",command=exit)
exit_button.pack(padx=10,pady=12)






# anim = animation.FuncAnimation(fig, update, frames=100, interval=200)


app.mainloop()
