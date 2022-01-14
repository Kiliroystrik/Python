from random import random
from Enemy import Enemy

# Randomize enemy level
brigandLevel = round((random()*5),0) + 1
wolfLevel = round((random()*5),1) + 10
soldierLevel = round((random()*5),1) +20
demonLevel = round((random()*5),1) + 30

# Tuple of enemies
enemyList = (["brigand",brigandLevel],("wolf",wolfLevel),("soldier",soldierLevel),("demon",demonLevel))

print(enemyList[0])

# for i in enemyList:
#     print(enemyList(i))