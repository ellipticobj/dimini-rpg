from consts import chars, enemies
from screens import charinfo, round

playerstate = {}
enemystate = {}
currchar = "no"

print("dimini rpg")

charchoice = charinfo(chars)
print(f"you have chosen: {charchoice}")
playerstate = chars[charchoice]

print()
print("stage 1 start")
print("you are facing: hot diggity dog")
print("round 1")
enemystate = enemies["hot diggity dog"]

round(enemystate, playerstate)
