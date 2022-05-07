import tkinter as tk
from randomTables import magicItems
from fractions import Fraction

root = tk.Tk()

# Widget to accept user entry for CR.
label = tk.Label(root, text= "Enter monster CR:")
label.pack()

entry = tk.Entry(root, width= 20)
entry.focus_set()
entry.pack()

# Function to generate items.
def itemGen():
    for child in frame.winfo_children():
            child.destroy()
    challengeRating = float(Fraction(entry.get()))
    frameHead = tk.Label(frame, text="Magic Items", font="bold")
    frameHead.pack()
    for row in magicItems(challengeRating):
        if row[1].strip() in ('+1', '+2', '+3'):
            row[0] = ''.join(row[0:2])
        name = tk.Label(frame, text= row[0])
        name.pack(padx=0, pady=1)

# Button that runs the itemGen function.
itemGenButton = tk.Button(root, text= "Generate Item List", command= itemGen)
itemGenButton.pack(padx= 0, pady= 10)

frame = tk.Frame()
frame.pack(side=tk.LEFT)

root.mainloop()

# class HelloFriend(tk.Frame):
#     def __init__(self, parent):
#         super(HelloFriend, self).__init__(parent)

#         # Widget to accept user entry for CR.
#         self.label = tk.Label(self, text= "Enter monster CR:")
#         self.label.pack()

#         self.entry = tk.Entry(self, width= 20)
#         self.entry.focus_set()
#         self.entry.pack()

#         # Generate magic item rewards.
#         def magicItemButton():
#             challengeRating = float(Fraction(self.entry.get()))
#             for row in treasureHoard(challengeRating):
#                 self.name = tk.Label(self, text= row[0])
#                 self.name.pack(padx=0, pady=5)

#         self.itemGen = tk.Button(self, text= "Generate Item List", command= magicItemButton)
#         self.itemGen.pack(padx= 0, pady= 10)

# if __name__ == "__main__":
#     root = tk.Tk()

#     main = HelloFriend(root)
#     main.pack(fill="both", expand = True)

#     root.mainloop()