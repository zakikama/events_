import sqlite3
import tkinter as tk
import tkinter.ttk as ttk


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)

    def show_table(self):
        data = ()
        with sqlite3.connect('events_final_db.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM events")
            data = (row for row in cursor.fetchall())

        root = tk.Tk()
        root.title("liste des evenements")
        table = Table(root, headings=('nom', 'lieu', 'date'), rows=data)
        table.pack(expand=tk.YES, fill=tk.BOTH)
        root.mainloop()