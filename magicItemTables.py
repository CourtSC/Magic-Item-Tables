#! python3
#! rollTables.py - a program to randomly roll on all of the items in MagicItems.csv.

from random import randint
from pathlib import Path
import csv

# Roll table for Treasure Hoard CR 0-4.
def magicTableCR4(d100):
    reward = []
    conTable = []
    itemTable = []
    rareTable = []
    # gems = sum([randint(1,6) for i in range(2)])
    # art = sum([randint(1,4) for i in range(2)])
    # cp = sum([randint(1,6) for i in range(6)])
    # sp = sum([randint(1,6) for i in range(3)])
    # gp = sum([randint(1,6) for i in range(2)])
    # reward.append((f'{cp * 100} CP', f'{sp * 100} SP', f'{gp * 10} GP'))
    # # Generate art or gem rewards 
    # if d100 in [i for i in range(7, 17)] + [i for i in range(37, 45)] + [i for i in range(61, 66)] + [i for i in range(76, 79)]:
    #     reward.append(f'{gems * 10} gp worth of gems.')
    # elif d100 in [i for i in range(17, 27)] + [i for i in range(45, 53)] + [i for i in range(66, 71)] + [i for i in range(79, 81)] + [i for i in range(86, 93)] + [i for i in range(98, 100)]:
    #     reward.append(f'{art * 25} gp worth of art objects.')
    # elif d100 in [i for i in range(27,37)] + [i for i in range(53,61)] + [i for i in range(71,76)] + [i for i in range(81,86)] + [i for i in range(93,98)] + [i for i in range(100, 101)]:
    #     reward.append(f'{gems * 50} gp worth of gems.')
    # Generate list of Consumables.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if 'consumable' in i.lower() and ('common' or 'uncommon' or 'varies') in i.lower():
                    i = i.split(',')
                    conTable.append([', '.join(i)])
    # Generate list from 50 magic items.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if ('common' or 'uncommon' or 'varies') in i.lower():
                    i = i.split(',')
                    itemTable.append([', '.join(i)])
    # Generate list of Rare Magic Items.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if 'rare' in i.lower():
                    i = i.split(',')
                    rareTable.append([', '.join(i)])
    if d100 in range(1, 61):
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
    elif d100 in range(61, 76):
        # Roll 1d4 times on table.
        for r in range(randint(1,4)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
    elif d100 in range(76, 86):
        # Roll 1d6 times on table.
        for r in range(randint(1,6)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
    elif d100 in range(86, 98):
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll 1d6 times on table.
        for r in range(randint(1,6)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
    elif d100 >= 98:
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll 1d6 times on table.
        for r in range(randint(1,6)):
            reward.append(itemTable[randint(0, len(itemTable) - 1 - 1)])
        # Pick a Rare magic item.
        reward.append(rareTable[randint(0, len(rareTable) - 1)])
    return reward

# Roll Table for Treasure Hoard CR 5-10.
def magicTableCR10(d100):
    reward = []
    conTable = []
    itemTable = []
    itemTableLow = []
    # gems = sum([randint(1,6) for i in range(3)])
    # art = sum([randint(1,4) for i in range(2)])
    # cp = sum([randint(1,6) for i in range(2)])
    # sp = sum([randint(1,6) for i in range(2)])
    # gp = sum([randint(1,6) for i in range(6)])
    # pp = sum([randint(1,6) for i in range(3)])
    # reward.append((f'{cp * 100} CP', f'{sp * 1000} SP', f'{gp * 10} GP', f'{pp * 10} PP'))
    # if d100 in [i for i in range(5,11)] + [i for i in range(29,33)] + [i for i in range(45,50)] + [i for i in range(64,66)] + [i for i in range(75,77)] + [i for i in range(81,85)]:
    #     reward.append(f'{art * 25} gp worth of art objects.')
    # elif d100 in [i for i in range(11,17)] + [i for i in range(33,37)] + [i for i in range(50,55)] + [i for i in range(67,70)] + [i for i in range(77,79)] + [i for i in range(85,89)]:
    #     reward.append(f'{gems * 50} gp worth of gems.')
    # elif d100 in [i for i in range(17,23)] + [i for i in range(37,41)] + [i for i in range(55,60)] + [i for i in range(70,73)] + [79] + [i for i in range(89,92)] + [i for i in range(95,97)] + [99]:
    #     reward.append(f'{gems * 100} worth of gems.')
    # elif d100 in [i for i in range(23,29)] + [i for i in range(41,45)] + [i for i in range(60,64)] + [i for i in range(73,75)] + [80] + [i for i in range(92,95)] + [i for i in range(97,99)] + [100]:
    #     reward.append(f'{art * 250} worth of art objects.')
    # Generate list of Consumables.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if 'consumable' in i.lower() and ('uncommon' or 'rare' or 'varies') in i.lower() and 'very rare' not in i.lower():
                    i = i.split(',')
                    conTable.append([', '.join(i)])
    # Generate list from 50 magic items.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if ('uncommon' or 'rare' or 'varies') in i.lower() and 'very rare' not in i.lower():
                    i = i.split(',')
                    itemTable.append([', '.join(i)])
    # Generate list of Common Magic Items.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if ('common' or 'varies') in i.lower():
                    i = i.split(',')
                    itemTableLow.append([', '.join(i)])
    # Generate list of Very Rare Magic Items
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        rareTable = []
        for row in reader:
            for i in row:
                if 'very rare' in i.lower():
                    i = i.split(',')
                    rareTable.append([', '.join(i)])
    if d100 in range(1, 61):
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll 1d4 Common items.
        for r in range(randint(1,4)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
    elif d100 in range(61, 76):
        # Roll 1d4 times on table.
        for r in range(randint(1,4)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d4 Common items.
        for r in range(randint(1,4)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
    elif d100 in range(76, 86):
        # Roll 1d6 times on table.
        for r in range(randint(1,6)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d6 Common items.
        for r in range(randint(1,6)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
    elif d100 in range(86, 98):
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll 1d6 times on table.
        for r in range(randint(1,6)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d6 Common items.
        for r in range(randint(1,6)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
    elif d100 >= 98:
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll 1d6 times on table.
        for r in range(randint(1,6)):
            reward.append(itemTable[randint(0, len(itemTable) - 1 - 1)])
        # Pick a Very Rare magic item.
        reward.append(rareTable[randint(0, len(rareTable) - 1)])
    return reward

# Roll Table for Treasure Hoard CR 11-16.
def magicTableCR16(d100):
    reward = []
    conTable = []
    itemTable = []
    itemTableLow = []
    # gems = sum([randint(1,6) for i in range(3)])
    # art = sum([randint(1,4) for i in range(2)])
    # gp = sum([randint(1,6) for i in range(4)])
    # pp =  sum([randint(1,6) for i in range(5)])
    # reward.append((f'{gp * 10} GP', f'{pp * 10} PP'))
    # if d100 in [i for i in range(4,7)] + [i for i in range(16,20)] + [i for i in range(30,36)] + [i for i in range(51,55)] + [i for i in range(67,69)] + [i for i in range(75,77)] + [i for i in range(83,85)] + [i for i in range(93,95)]:
    #     reward.append(f'{art * 250} gp worth of art objects.')
    # elif d100 in [i for i in range(7,10)] + [i for i in range(20,24)] + [i for i in range(36,41)] + [i for i in range(55,59)] + [i for i in range(69,71)] + [i for i in range(77,79)] + [i for i in range(86,89)] + [i for i in range(95,97)]:
    #     reward.append(f'{art * 750} gp worth of art objects.')
    # elif d100 in [i for i in range(10,13)] + [i for i in range(24,27)] + [i for i in range(41,46)] + [i for i in range(59,63)] + [i for i in range(71,73)] + [i for i in range(79,81)] + [i for i in range(97,99)]:
    #     reward.append(f'{gems * 500} gp worth of gems.')
    # elif d100 in [i for i in range(13,16)] + [i for i in range(27,30)] + [i for i in range(46,51)] + [i for i in range(63,67)] + [i for i in range(73,75)] + [i for i in range(81,83)] + [i for i in range(91,93)] + [i for i in range(99,101)]:
    #     reward.append(f'{gems * 1000} gp worth of gems.')
    # Generate list of Consumables.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if 'consumable' in i.lower() and ('rare' or 'very rare' or 'varies') in i.lower():
                    i = i.split(',')
                    conTable.append([', '.join(i)])
    # Generate list from 50 magic items.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if ('rare' or 'very rare' or 'varies') in i.lower():
                    i = i.split(',')
                    itemTable.append([', '.join(i)])
    # Generate list of Common & Uncommon Magic Items.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if ('common' or 'uncommon' or 'varies') in i.lower():
                    i = i.split(',')
                    itemTableLow.append([', '.join(i)])
    # Generate list of Very Rare Magic Items
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        rareTable = []
        for row in reader:
            for i in row:
                if 'very rare' in i.lower():
                    i = i.split(',')
                    rareTable.append([', '.join(i)])
    # Generate list of Legendary Magic Items
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        legTable = []
        for row in reader:
            for i in row:
                if 'legendary' in i.lower():
                    i = i.split(',')
                    legTable.append([', '.join(i)])
    if d100 in range(1,30):
        # Roll 1d4 + 1d6 times on the Low Magic Table.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Choose one Magic item
        reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
    elif d100 in range(30,51):
        # Roll 1d4 Magic Items.
        for r in range(randint(1,4)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d6 Low Magic Items.
        for r in range(randint(1,6)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
    elif d100 in range(51,67):
        # Roll 1d6 Magic Items.
        for r in range(randint(1,6)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d6 Low Magic Items.
        for r in range(randint(1,6)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
    elif d100 in range(67,75):
        # Roll 1d6 Magic Items.
        for r in range(randint(1,6)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d6 + 1d4 Low Magic Items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
    elif d100 in range(75,83):
        # Roll 1d6 + 1d4 Magic Items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d6 Low Magic Items.
        for r in range(randint(1,6)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
    elif d100 in range(83,93):
        # Roll 1d6 + 1d4 Magic Items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d6 Low Magic Items.
        for r in range(randint(1,6)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll for 1 Very Rare item.
        reward.append(rareTable[randint(0, len(rareTable) - 1)])
    elif d100 >= 93:
        # Roll 1d6 Magic Items.
        for r in range(randint(1,6)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d6 Low Magic Items.
        for r in range(randint(1,6)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d6 Consumables.
        for r in range(randint(1,6)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll 1d6 Very Rare items.
        for r in range(randint(1,6)):        
            reward.append(rareTable[randint(0, len(rareTable) - 1)])
        # Pick 1 Legendary Item
        reward.append(legTable[randint(0, len(legTable) - 1)])
    return reward

# Roll Table for Treasure Hoard CR 17+.
def magicTableCR17(d100):
    reward = []
    conTable = []
    itemTable = []
    itemTableLow = []
    # gems = sum([randint(1,6) for i in range(3)])
    # art = sum([randint(1,4) for i in range(2)])
    # gp = sum([randint(1,6) for i in range(12)])
    # pp =  + sum([randint(1,6) for i in range(8)])
    # reward.append((f'{gp * 10} GP', f'{pp * 10} PP'))
    # if d100 in [i for i in range(3,6)] + [i for i in range(15,23)] + [i for i in range(47,53)] + [69] + [i for i in range(73,75)] + [i for i in range(81,86)]:
    #     reward.append(f'{gems * 1000} gp worth of gems.')
    # elif d100 in [i for i in range(6,9)] + [i for i in range(23,31)] + [i for i in range(53,59)] + [70] + [i for i in range(75,77)] + [i for i in range(86,91)]:
    #     reward.append(f'{art * 2500} gp worth of art.')
    # elif d100 in [i for i in range(9,12)] + [i for i in range(31,39)] + [i for i in range(59,64)] + [71]  + [i for i in range(77,79)] + [i for i in range(91,96)]:
    #     reward.append(f'{art * 7500} gp worth of art.')
    # elif d100 in [i for i in range(12,15)] + [i for i in range(39,47)] + [i for i in range(64,69)] + [72] + [i for i in range(79,81)] + [i for i in range(96,101)]:
    #     reward.append(f'{gems * 5000} gp worth of gems.')
    # Generate list of Consumables.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if 'consumable' in i.lower() and ('rare' or 'very rare' or 'legendary' or 'varies') in i.lower():
                    i = i.split(',')
                    conTable.append([', '.join(i)])
    # Generate list from 50 magic items.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if ('rare' or 'very rare' or 'varies') in i.lower():
                    i = i.split(',')
                    itemTable.append([', '.join(i)])
    # Generate list of Common & Uncommon Magic Items.
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        for row in reader:
            for i in row:
                if ('common' or 'uncommon' or 'varies') in i.lower():
                    i = i.split(',')
                    itemTableLow.append([', '.join(i)])
    # Generate list of Very Rare Magic Items
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        rareTable = []
        for row in reader:
            for i in row:
                if 'very rare' in i.lower():
                    i = i.split(',')
                    rareTable.append([', '.join(i)])
    # Generate list of Legendary Magic Items
    with open(Path.cwd() / Path('MagicItems.csv'), 'r', encoding='Windows-1252') as dBase:
        reader = csv.reader(dBase, delimiter = '\n')
        legTable = []
        for row in reader:
            for i in row:
                if 'legendary' in i.lower():
                    i = i.split(',')
                    legTable.append([', '.join(i)])
    if d100 in range(1,30):
        # Roll 1d4 + 1d6 times on the Low Magic Table.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Choose 1d4 Magic item
        for r in range(randint(1,4)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d4 + 1d6 Consumables.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll for 1 Very Rare item.
        reward.append(rareTable[randint(0, len(rareTable) - 1)])
    elif d100 in range(30,51):
        # Roll 1d6 Magic Items.
        for r in range(randint(1,6)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d4 + 1d6 Low Magic Items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d4 + 1d6 Consumables.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll for 1 Very Rare item.
        reward.append(rareTable[randint(0, len(rareTable) - 1)])
    elif d100 in range(51,67):
        # Roll 1d4 + 1d6 Magic Items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d4 + 1d6 Low Magic Items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d4 + 1d6 Consumables.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll for 1d4 Very Rare item.
        for r in range (randint(1,4)):
            reward.append(rareTable[randint(0, len(rareTable) - 1)])
    elif d100 in range(67,75):
        # Roll 1d4 + 1d6 Magic Items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d6 + 1d4 + 3 Low Magic Items.
        for r in range(randint(1,6) + randint(1,4) + 3):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d4 + 1d6 Consumables.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll for 1d4 Very Rare item.
        for r in range (randint(1,4)):
            reward.append(rareTable[randint(0, len(rareTable) - 1)])
    elif d100 in range(75,83):
        # Roll 1d6 + 1d4 + 3 Magic Items.
        for r in range(randint(1,6) + randint(1,4) + 3):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d4 + 1d6 Low Magic Items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d4 + 1d6 Consumables.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll for 1d4 Very Rare item.
        for r in range (randint(1,4)):
            reward.append(rareTable[randint(0, len(rareTable) - 1)])
    elif d100 in range(83,93):
        # Roll 1d6 + 1d4 + 3 Magic Items.
        for r in range(randint(1,6) + randint(1,4) + 3):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d4 + 1d6 Low Magic Items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d4 + 1d6 Consumables.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll for 1d6 Very Rare item.
        for r in range (randint(1,6)):
            reward.append(rareTable[randint(0, len(rareTable) - 1)])
    elif d100 >= 93:
        # Roll 1d4 + 1d6 Magic Items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTable[randint(0, len(itemTable) - 1)])
        # Roll 1d4 + 1d6 Low Magic Items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(itemTableLow[randint(0, len(itemTableLow) - 1)])
        # Roll 1d4 + 1d6 Consumables.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(conTable[randint(0, len(conTable) - 1)])
        # Roll 1d4 + 1d6 Very Rare items.
        for r in range(randint(1,6) + randint(1,4)):
            reward.append(rareTable[randint(0, len(rareTable) - 1)])
        # Roll 1d4 Legendary Item
        for r in range(randint(1,4)):
            reward.append(legTable[randint(0, len(legTable) - 1)])
    return reward

# Accept CR as argument and choose correct table for hoard.
def treasureHoard(CR):
    d100 = randint(1,100)
    with open('magicRewards.csv', 'w', encoding='Windows-1252') as rew:
        writer = csv.writer(rew)
        writer.writerow(('Name', 'Rarity', 'Type', 'SubType', 'Attunement', 'Notes'))
        if CR <= 4:
            for i in magicTableCR4(d100):
                line = ''.join(i).split(', ')
                magicItem = line[:5]
                notes = ','.join(line[5:]).strip('\"')
                magicItem.append(notes)
                writer.writerow(magicItem)
                print(f'Added item {magicItem[0]} to reward list.')
        elif CR in range(5,11):
            for i in magicTableCR10(d100):
                line = ''.join(i).split(', ')
                magicItem = line[:5]
                notes = ','.join(line[5:]).strip('\"')
                magicItem.append(notes)
                writer.writerow(magicItem)
                print(f'Added item {magicItem[0]} to reward list.')
        elif CR in range(11,17):
            for i in magicTableCR16(d100):
                line = ''.join(i).split(', ')
                magicItem = line[:5]
                notes = ','.join(line[5:]).strip('\"')
                magicItem.append(notes)
                writer.writerow(magicItem)
                print(f'Added item {magicItem[0]} to reward list.')
        elif CR >= 17:
            for i in magicTableCR17(d100):
                line = ''.join(i).split(', ')
                magicItem = line[:5]
                notes = ','.join(line[5:]).strip('\"')
                magicItem.append(notes)
                writer.writerow(magicItem)
                print(f'Added item {magicItem[0]} to reward list.')

treasureHoard(4)
# End of file.