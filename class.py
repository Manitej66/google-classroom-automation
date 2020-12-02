import sys
from time import sleep
from today_classes import *
import time
inp = sys.argv[1].upper()


if inp in classes:
    open_link(classes[inp])
elif inp == '-T':
    print()
    classes_today()
elif inp == '-A':
    subs = find_classes()
    print(subs)
    c = 0
    while True:
        if c == 1:
            break
        time = datetime.now().time()
        time = str(time).split(':')
        for i in subs:            
            if time[0] == i[0:2] and time[1] == i[3:5]:
                open_link(classes[i[20:]])
                print('Opened ' + i[20:] + ' link')
                if i == subs[-1]:
                    c = 1
                    break
                sleep(2700) # EACH CLASS IS 45MIN LONG
                break

else:
    print('\n' + '\t' + 'Invalid command')
    print('\n' + '\t' + 'Try class -h for help menu')
