import tkinter as tk
from tkinter import *
from Event import event
from Tables import Table
import sqlite3
import datetime


def add_event():
    gui = tk.Toplevel(ui)
    gui.geometry("500x1000")
    gui.title("Ajout evenement")
    p = event()

    def getEntry():
        p.NomEvent = myEntry_Nom.get()
        date_entry = myEntry_Date.get()
        p.DateEvent = datetime.datetime.strptime(date_entry, '%Y-%m-%d-%H:%M')
        for i in liste_lieu.curselection():
            p.LieuEvent = liste_lieu.get(i)
            print(liste_lieu.get(i))
        p.sauvgarde_event()

    label_Nom = Label(gui, text="Entrer Nom de l'evenement : ")
    label_Nom.pack()
    myEntry_Nom = tk.Entry(gui, width=40)
    myEntry_Nom.pack(pady=20)
    label_Lieu = Label(gui, text="Entrer le lieu de l'evenement : ")
    label_Lieu.pack()
    liste_lieu = Listbox(gui, width=40, height=10, selectmode=SINGLE)
    liste_lieu.insert(1, "Ciné Cité les Halles")
    liste_lieu.insert(2, "Gaumont Opéra côté Premier")
    liste_lieu.insert(3, "Le Grand Rex")
    liste_lieu.insert(4, "MK2 Beaubourg ")
    liste_lieu.insert(5, "Luminor Hôtel de ville ")
    liste_lieu.pack()
    label_Date = Label(gui, text="Entrer la date de l'evenement : (YYYY-MM-DD-hh:mm) ")
    label_Date.pack()
    myEntry_Date = tk.Entry(gui, width=40)
    myEntry_Date.pack(pady=20)
    btn = tk.Button(gui, height=1, width=10, text="valider", fg="red", command=getEntry)
    btn.pack()
    bouton = tk.Button(gui, text="Quitter", bg="red", command=gui.destroy)
    bouton.pack()
    gui.mainloop()


def show_event():
    t = Table()
    t.show_table()


def modifier_event(lieu, date, nom):
    don = [lieu, date, nom]
    connexion = sqlite3.connect("events_final_db.db")
    curseur = connexion.cursor()
    sql = '''UPDATE events SET lieu = ? , date = ? WHERE nom = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("modification reussi")


def modifier_ui():
    gui = tk.Toplevel(ui)
    gui.geometry("500x1000")
    gui.title("modification")
    p = event()

    def modify1():
        p.NomEvent = myEntry_Nom.get()
        date_entry = myEntry_Date.get()
        p.DateEvent = datetime.datetime.strptime(date_entry, '%Y-%m-%d-%H:%M')
        for i in liste_lieu.curselection():
            p.LieuEvent = liste_lieu.get(i)
        modifier_event(p.LieuEvent, p.DateEvent, p.NomEvent)

    label_Nom = Label(gui, text="Entrer Nom de l'evenement a modifier : ")
    label_Nom.pack()
    myEntry_Nom = tk.Entry(gui, width=40)
    myEntry_Nom.pack(pady=20)
    label_Lieu = Label(gui, text="Entrer le nouveau lieu de l'evenement : ")
    label_Lieu.pack()
    liste_lieu = Listbox(gui, width=40, height=10, selectmode=SINGLE)
    liste_lieu.insert(1, "Ciné Cité les Halles")
    liste_lieu.insert(2, "Gaumont Opéra côté Premier")
    liste_lieu.insert(3, "Le Grand Rex")
    liste_lieu.insert(4, "MK2 Beaubourg ")
    liste_lieu.insert(5, "Luminor Hôtel de ville ")
    liste_lieu.pack()
    label_Date = Label(gui, text="Entrer la nouvelle date de l'evenement : (YYYY-MM-DD-hh:mm) ")
    label_Date.pack()
    myEntry_Date = tk.Entry(gui, width=40)
    myEntry_Date.pack(pady=20)
    btn = tk.Button(gui, height=1, width=10, text="valider", fg="red", command=modify1)
    btn.pack()
    bouton = tk.Button(gui, text="Quitter", bg="red", command=gui.destroy)
    bouton.pack()
    gui.mainloop()


def delete_event(nom):
    don = [nom]
    connexion = sqlite3.connect("events_final_db.db")
    curseur = connexion.cursor()
    sql = '''DELETE FROM events  WHERE nom = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("SUPPRESSION reussi")


def delete_ui():
    gui = tk.Toplevel(ui)
    gui.geometry("500x1000")
    gui.title("suppression")
    p = event()

    def supp():
        p.NomEvent = myEntry_Nom.get()
        delete_event(p.NomEvent)

    label_Nom = Label(gui, text="Entrer Nom de l'evenement a supprimer : ")
    label_Nom.pack()
    myEntry_Nom = tk.Entry(gui, width=40)
    myEntry_Nom.pack(pady=20)

    btn = tk.Button(gui, height=1, width=10, text="valider", fg="red", command=supp)
    btn.pack()
    bouton = tk.Button(gui, text="Quitter", bg="red", command=gui.destroy)
    bouton.pack()
    gui.mainloop()


ui = tk.Tk()

# Ici on vas définir le titre de notre fenêtre
ui.title("Cine Club")

# Ici on vas définir la grandeur de notre fenêtre afin de s'assurer quelle soit bien
# centré par rapport a l'écran
screen_x = int(ui.winfo_screenwidth())
screen_y = int(ui.winfo_screenheight())
window_x = 480
window_y = 240

posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
ui.geometry(geo)

# Ici on vas définir l'icon' de notre fenêtre
ui.iconbitmap('cine.ico')
d1 = datetime.datetime.now()
mainmenu: tk.Menu = tk.Menu(ui)
first_menu = tk.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="Consulter Planning", command=show_event)
first_menu.add_command(label="Ajouter Evenement", command=add_event)
first_menu.add_command(label="Modifier Evenement", command=modifier_ui)
first_menu.add_command(label="Supprimer Evenement", command=delete_ui)
first_menu.add_separator()
first_menu.add_command(label="Quitter", command=ui.quit)
mainmenu.add_cascade(label="Gestion Evenement", menu=first_menu)
ui.config(menu=mainmenu)
ui.mainloop()
