import json

#hero powers and coin
exceptions = ['Shapeshift',
              'Steady Shot',
              'Fireblast',
              'Reinforce',
              'Lesser Heal',
              'Dagger Mastery',
              'Totemic Call',
              'Life Tap',
              'Armor Up!',
              'The Coin']

def query(freqs,name,played):
    global exceptions
    freqs = freqs[name]
    candidates = []
    #this is the stupidest way i could have done this
    for card in freqs.keys():
        if played.count(freqs[card]) < 2 and card not in exceptions:
            for x in range(freqs[card]):
                candidates.append(card)
    return candidates

def probabilites(candidates):
    set_cand = set(candidates)
    options = [[x,candidates.count(x)] for x in set_cand]
    probs = [x[1] for x in options]
    new_options = []
    for pos,x in enumerate(probs):
        if x/(sum(probs)/100) > 1:
            new_options.append(options[pos])
    options = new_options
    probs = [x[1] for x in options]
    for pos,x in enumerate(probs):
        options[pos][1] = round(x/(sum(probs)/100),2)
    options.sort(key=lambda x: x[1])
    return options[::-1]

freqs = open('freqs.json','r').read()
freqs = json.loads(freqs)

cards_played = ['Sludge Slurper', 'Sir Finley Mrrgglton', 'Toxfin', 'The Coin', 'Ice Fishing', 'Underbelly Angler', 'Murloc Tidecaller', 'Murloc Tinyfin', 'Murloc Tidehunter', 'Rockpool Hunter']
this_turn = []
#having two variables is sorta obsolete and should be removed at some point

while True:
    inpt = input("End, predict or new card? ")
    if inpt == 'e':
        pass
    elif inpt == 'n':
        this_turn.append(input('Card name: '))
        cards_played.append(this_turn[-1])
    else:
        candidates = []
        for pos,card in enumerate(this_turn):
            if len(this_turn)-pos < 3:
                candidates += query(freqs,card,this_turn)
        if candidates == []:
            candidates += query(freqs,cards_played[0],[cards_played])
        probs = probabilites(candidates)
        for x in probs:
            print(x)
