import json

def op_filter(card_hist):
    op_cards = []
    for card in card_hist:
        if card["player"] == "opponent":
            op_cards.append(card)
    return op_cards

#read data
gamesets = [x.strip() for x in open("filenamelist.txt",'r').readlines()]

freqs = {}

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
        this_turn = []
        for pos,card in enumerate(card_hist[:-1]):
            pair = [card,card_hist[pos+1]]
            for x in range(2):
                #check if we need to make a new field
                name = pair[0]["card"]["name"]
                if name not in freqs:
                    freqs[name] = {}
                #add to the appropriate frequency
                next_card = pair[1]
                next_name = next_card["card"]["name"]
                #check again for field
                if next_name not in freqs[name]:
                    freqs[name][next_name] = 0
                freqs[name][next_name] += 1
                pair = pair[::-1]

open("freqs.json","w").write(json.dumps(freqs,indent=2))

