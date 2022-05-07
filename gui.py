import tkinter as tk
from magicItemTables import treasureHoard

class HelloFriend(tk.Frame):
    def __init__(self, parent):
        super(HelloFriend, self).__init__(parent)

        for row in treasureHoard(4):
            self.name = tk.Label(self, text = row[0])
            self.name.pack(padx=0, pady=5)

if __name__ == "__main__":
    root = tk.Tk()

    main = HelloFriend(root)
    main.pack(fill="both", expand = True)

    root.mainloop()