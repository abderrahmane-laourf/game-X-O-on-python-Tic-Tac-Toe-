from tkinter import *
# Initialisation des variables
player = "X"
winner = None


# Fonction pour changer de joueur
def next_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

# Fonction pour colorer les cases gagnantes
def color_winner(buttons):
    for button in buttons:
        button.config(bg="green")

# Fonction pour vérifier le gagnant
def check_winner():
    global winner
    winning_combinations = [
        (b1, b2, b3),
        (b4, b5, b6),
        (b7, b8, b9),
        (b1, b4, b7),
        (b2, b5, b8),
        (b3, b6, b9),
        (b1, b5, b9),
        (b3, b5, b7),
    ]
    for combination in winning_combinations:
        if combination[0]["text"] == combination[1]["text"] == combination[2]["text"] == player:
            winner = player
            color_winner(combination)
            label_status.config(text=f"Le joueur {player} a gagné !")
            return True
    return False

# Fonction pour gérer les clics sur les boutons
def on_click(button):
    if button["text"] == "" and not winner:
        button.config(text=player)
        if not check_winner():
            next_player()
            label_status.config(text=f"Tour du joueur {player}")

# Création de la fenêtre principale
root = Tk()
root.title("Morpion")

# Label pour le statut
label_status = Label(root, text="Tour du joueur X", font=("Arial", 16))
label_status.grid(row=0, column=0, columnspan=3)

# Création des boutons
b1 = Button(root, text="", font=("Arial", 24), height=2, width=5, command=lambda: on_click(b1))
b2 = Button(root, text="", font=("Arial", 24), height=2, width=5, command=lambda: on_click(b2))
b3 = Button(root, text="", font=("Arial", 24), height=2, width=5, command=lambda: on_click(b3))
b4 = Button(root, text="", font=("Arial", 24), height=2, width=5, command=lambda: on_click(b4))
b5 = Button(root, text="", font=("Arial", 24), height=2, width=5, command=lambda: on_click(b5))
b6 = Button(root, text="", font=("Arial", 24), height=2, width=5, command=lambda: on_click(b6))
b7 = Button(root, text="", font=("Arial", 24), height=2, width=5, command=lambda: on_click(b7))
b8 = Button(root, text="", font=("Arial", 24), height=2, width=5, command=lambda: on_click(b8))
b9 = Button(root, text="", font=("Arial", 24), height=2, width=5, command=lambda: on_click(b9))

# Placement des boutons dans la grille
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)

# Boucle principale
root.mainloop()
