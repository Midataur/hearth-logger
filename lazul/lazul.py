from Tkinter import *
import re
import time

root = Tk()
v = StringVar()
Label(root, textvariable=v).pack()

opponent = 'Unknown'
mytag = 'Midataur#1530'

while True:
    try:
        old_log = open('Power.log').readlines()
        old_log = [x.strip() for x in old_log]
    except:
        pass
    else:
        break

while True:
    time.sleep(0.01)
    while True:
        try:
            log = open('Power.log').readlines()
            log = [x.strip() for x in log]
        except:
            pass
        else:
            break
    #power log
    for iter,line in enumerate(log):
        if iter >= len(old_log):
            if 'CREATE_GAME' in line:
                opponent = 'Unknown'
    #zone_log
    for line in log[len(old_log)-1:]:
        tag = re.search('=\w+#\d\d\d\d',line)
        if tag != None:
            opponent = tag.group(0)[1:]
    old_log = list(log)
    v.set('Lazul predicts that your next opponent will be:\n'+str(opponent))
    root.update_idletasks()
    root.update()
