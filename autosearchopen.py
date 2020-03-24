# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:14:09 2020

@author: cs
"""
import pyautogui,time
namefield=(390,310)
submitbutton=(700,133)
openlink=(130,250)
pyautogui.click(namefield[0],namefield[1])
time.sleep(2)
pyautogui.typewrite('master_yi')
time.sleep(2)
pyautogui.click(submitbutton[0],submitbutton[1])
time.sleep(2)
pyautogui.click(openlink[0],openlink[1])