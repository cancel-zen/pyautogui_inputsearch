
# coding: utf-8




import pyautogui


print('press ctrl-c to quit')


try:
    while True:
        x,y=pyautogui.position()
        positionstr='x:'+str(x).rjust(4)+' y:'+str(y).rjust(4)
        print(positionstr,end='')
        print('\b'*len(positionstr),end='',flush=True)
except KeyboardInterrupt:
    print('\done')


