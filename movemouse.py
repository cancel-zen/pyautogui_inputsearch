
# coding: utf-8

# In[4]:


import pyautogui


# In[6]:


pyautogui.size()


# In[7]:


width,height=pyautogui.size()


# In[12]:


for i in range(10):
    pyautogui.moveTo(100,100,duration=0.25)
    pyautogui.moveTo(200,100,duration=0.25)
    pyautogui.moveTo(200,200,duration=0.25)
    pyautogui.moveTo(100,200,duration=0.25)


# In[11]:


for i in range(10):
    pyautogui.moveTo(100,100)
    pyautogui.moveTo(200,100)
    pyautogui.moveTo(200,200)
    pyautogui.moveTo(100,200)


# In[15]:


for i in range(10):
    pyautogui.moveRel(100,0,duration=0.25)
    pyautogui.moveRel(0,100,duration=0.25)
    pyautogui.moveRel(-100,0,duration=0.25)
    pyautogui.moveRel(0,-100,duration=0.25)


# In[17]:


pyautogui.position()

