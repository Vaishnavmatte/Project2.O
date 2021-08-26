#!/usr/bin/env python
# coding: utf-8

# In[9]:


a=6
if(a==6):
    print("correct")


# In[11]:


a=15
b=20
if (a>=25):
    print("a is greater")
else:
    print("a is lesser")


# In[28]:


player1 = str(input("Enter either stone,paper,scissor"))
player2 = str(input("Enter either stone,paper,scissor"))
if (player1=="stone" and player2=="stone"):
    print("match is drawn and try again")
elif(player1=="stone" and player2=="paper"):
    print("stone can smash paper so player1 wins,""\n congrajulations player1")
elif(player1=="stone" and player2=="scissor"):
    print("stone can smash scissor so player1 wins,""\n congrajulations player1")
elif(player1=="paper" and player2=="stone"):
    print("stone can smash paper so user2 wins,""\n congrajulations player2")
elif(player1=="paper" and player2=="paper"):
    print("match is draw,""\n try again" )
elif(player1=="paper" and player2=="scissior"):
    print("scissor can cut paper so points goes to user2,""\n congratulations player2")
elif(player1=="scissor" and player2=="stone"):
    print("stone can beat scissor so user2 wins,""\n congratulations player2")
elif(player1=="scissor" and player2=="paper"):
    print("scissor can cut paper so user1 wins""\n congratulations player1")
elif(player1=="scissor" and player2=="scissor"):
    print("match is draw""\n try again")
    


# In[ ]:





# In[ ]:




