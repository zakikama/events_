import datetime
import sqlite3

class event:
    def __init__(self):
        self.DateEvent = datetime.datetime(2020, 5, 17)
        self.LieuEvent = "init"
        self.NomEvent = "init"

    def show_event(self):
        print("nom "+ self.NomEvent+" date " + self.DateEvent.strftime("%b %d %Y %H:%M:%S") + " lieu " + self.LieuEvent)


    def sauvgarde_event(self):
        donnees = [ self.NomEvent, self.LieuEvent, self.DateEvent]
        connexion = sqlite3.connect("events_final_db.db")
        curseur = connexion.cursor()

        curseur.execute('''CREATE TABLE IF NOT EXISTS events( nom TEXT, lieu TEXT, date DATETIME)''')
        curseur.execute('''
            INSERT INTO events(nom, lieu, date ) VALUES (?,?,?)
            ''', donnees)
        connexion.commit()
        print("sauvgarde reussi")







