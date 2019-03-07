from Tkinter import *
import re

def pretty(line):
    line = line.replace('[Zone] ZoneChangeList.ProcessChanges() - ','')
    match1 = re.search('(?<=entityName=).*(?= id=)',line)
    match2 = re.search('\\[.*\\]',line)
    line = line.replace(match2.group(0),match1.group(0))
    return line

root = Tk()
v = StringVar()
Label(root, textvariable=v).pack()

hand = []
played = []
play = []
graveyard = []

while True:
    try:
        old_log = open('output_log.txt').readlines()
        old_log = [x.strip() for x in old_log]
    except:
        pass
    else:
        break

while True:
    while True:
        try:
            log = open('output_log.txt').readlines()
            log = [x.strip() for x in log]
        except:
            pass
        else:
            break
    for iter,line in enumerate(log):
        if iter > len(old_log) and 'TRANSITIONING' in line and line[-2:] != 'to':
            line = pretty(line)
            print line
            #figure out game_state
            if 'FRIENDLY' in line:
                card = re.search('(?<=card ).*(?= to)',line).group(0)
                if re.search('PLAY',line) != None:
                    if card in hand:
                        hand.pop(hand.index(card))
                        played.append(card)
                    if 'Hero' not in line:
                        play.append(card)
                elif re.search('HAND',line) != None:
                    hand.append(card)
                elif re.search('GRAVEYARD',line) != None:
                    if card in play:
                        play.pop(play.index(card))
                    else:
                        played.append(card)
                    graveyard.append(card)
                elif re.search('DECK',line) != None:
                    if card in hand:
                        hand.pop(hand.index(card))
    old_log = list(log)
    v.set('Hand: '+str(hand)+'\nPlay: '+str(play)+'\nGraveyard: '+str(graveyard)+'\nPlayed: '+str(played))
    root.update_idletasks()
    root.update()
