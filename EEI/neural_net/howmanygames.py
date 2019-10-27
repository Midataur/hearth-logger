from random import randint
import json
import re

def op_filter(card_hist):
    op_cards = []
    for card in card_hist:
        if card["player"] == "opponent":
            op_cards.append(card)
    return op_cards


#read data
gamesets = [x.strip() for x in open("filenamelist.txt",'r').readlines()]

#prepare list of unique card ids

un = {}

print('Starting unique ids')

games = 0

for filename in gamesets:
    data = open(filename,'r').read()
    data = json.loads(data)

    #analyze freqs
    for game in data["games"]:
        games += 1

print('Analysed',games,'games')
