import tkinter as tk
from randomTables import magicItems, valuables
from fractions import Fraction
from random import randint

root = tk.Tk()
root.title("Treasure Hoard")

# Widget to accept user entry for CR.
label = tk.Label(root, text= "Enter monster CR:")
label.pack()

entry = tk.Entry(root, width= 20)
entry.focus_set()
entry.pack()

# Function to generate items.
def itemGen():
    for child in itemFrame.winfo_children():
        child.destroy()
    for child in valFrame.winfo_children():
        child.destroy()
    challengeRating = float(Fraction(entry.get()))
    itemFrameHead = tk.Label(itemFrame, text="Magic Items", font="bold")
    itemFrameHead.pack()
    valFrameHead = tk.Label(valFrame, text="Valuables", font="bold")
    valFrameHead.pack()
    for row in magicItems(challengeRating):
        if row[0] == 'Ammunition':
            row[0] = f'{randint(1,20) + 10}x {row[0]}'
        if row[0] == 'Potion of Healing':
            row[0] = f'{randint(1,4)}x {row[0]}'
        if row[1].strip() in ('+1', '+2', '+3'):
            row[0] = ''.join(row[0:2])
        name = tk.Label(itemFrame, text= row[0])
        name.pack(padx=0, pady=1)
    for row in valuables(challengeRating):
        for coin in row[0]:
            name = tk.Label(valFrame, text= coin)
            name.pack(padx=0, pady=1)
        for obj in row[1:]:
            name = tk.Label(valFrame, text= obj)
            name.pack(padx=0, pady=1)
        

# Button that runs the itemGen function.
itemGenButton = tk.Button(root, text= "Generate Treasure Hoard", command= itemGen)
itemGenButton.pack(padx= 0, pady= 10)

itemFrame = tk.Frame()
itemFrame.pack(side=tk.LEFT, padx=30)
valFrame = tk.Frame()
valFrame.pack(side=tk.RIGHT, padx=30)

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