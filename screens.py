from funcs import printstats

def charinfo(chars):
    while True:
        print("\ncharacters: ")
        for i in chars.keys():
            print(f":: {i}")
        print("enter character name to select")
        print("enter <info 'character'> for stats")
        c = input("> ").split()
        if c[0] == "info":
            if c[1] not in chars.keys():
                print("character does not exist!")
            else:
                printstats(chars[c[1]])
                input("enter to continue")
        else:
            if c[0] not in chars.keys():
                print("character does not exist!")
            else:
                return c[0]

def round(enemy, player):
    # print basic stats
    print(f"enemy health: {enemy['health']}")
    print(f"enemy cooldown: {enemy['cooldown']}")
    print(f"your health: {player['health']}")
    print(f"your cooldown: {player['cooldown']}")
    
    # TODO: print actions (attack, def, skills in the future)

    input("enter action: ")

    # TODO: complete this


