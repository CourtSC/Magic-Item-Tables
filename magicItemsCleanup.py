import csv

with open('Magic Item Tables/MagicItems.csv', 'w', encoding='Windows-1252') as dBase:
    writer = csv.writer(dBase)
    for i in dBase:
        if ',' in i[0]:
            pass
