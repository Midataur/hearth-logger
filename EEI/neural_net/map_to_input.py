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

un = []

print('Starting unique ids')

for filename in gamesets:
    data = open(filename,'r').read()
    data = json.loads(data)

    #analyze freqs
    for game in data["games"]:
        card_hist = op_filter(game["card_history"])
        try:
            turn = card_hist[0]["turn"]
        except IndexError:
            continue
        for pos,card in enumerate(card_hist[:-1]):
            card_id = card["card"]["id"]
            if card_id not in un:
                un.append(card_id)

un = sorted(un)

print('Worked out unique ids')

#controls the order of opponent input data
op_list = ["Paladin",
           "Hunter",
           "Warrior",
           "Rogue",
           "Shaman",
           "Druid",
           "Priest",
           "Mage",
           "Warlock"]

##prepare the training data
num_games = 0

#exclude some game ids
exclusions = [int(x.strip()) for x in open('exclusions.txt','r').readlines()]

#wipe the training data list
open("training.csv","w").write('')
open("tr_answers.csv","w").write('')

open("testing.csv","w").write('')
open("te_answers.csv","w").write('')

for filename in gamesets:
    data = open(filename,'r').read()
    data = json.loads(data)
    #extract data from game
    for game in data["games"]:
        if randint(0,3) < 3:
            fn = ['training','tr_answers']
        else:
            fn = ['testing','te_answers']
        num_games += 1
        if num_games % 10 == 0:
            print('Working on game',num_games)
        card_hist = op_filter(game["card_history"])
        try:
            turn = card_hist[0]["turn"]
        except IndexError:
            continue
        #get turn order
        coin = [1] if game["coin"] else [0]
        #get opponent
        opponent = [0 for x in range(9)]
        opponent[op_list.index(game["opponent"])] = 1
        #get list of cards played this game
        played = [0 for x in range(len(un))]
        this_turn = [0 for x in range(len(un))]
        id_this_turn = []
        #look through the card list
        for pos,card in enumerate(card_hist[:-1]):
            #get card_id
            card_id = card["card"]["id"]
            turn = [int(card["turn"])]
            #save training data
            training_data = coin+turn+opponent+played+this_turn
            answers = [0 for x in range(len(un))]
            answers[un.index(card_id)]
            open(fn[0]+'.csv',"a").write(str(training_data)[1:-1]+'\n')
            open(fn[1]+'.csv',"a").write(str(answers)[1:-1]+'\n')
            #add the card id to played
            played[un.index(card_id)] += 1
            if len(id_this_turn) > 3:
                id_this_turn.pop(0)
                id_this_turn.append(card_id)
            #add this turn
            this_turn = [0 for x in range(len(un))]
            for x in id_this_turn:
                this_turn[un.index(x)] += 1

print('Saving data')
print('Done')
