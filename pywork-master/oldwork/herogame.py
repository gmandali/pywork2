print("""Your hero is in danger.
he is surounded by evil trolls.
this is his last battle.""")
hero = 108
troll = 0
damage = 3
while hero != 0:
    print("your hero swung and defeated one troll but took 3 damage points.")
    troll += 1
    hero -= 3
print("your hero fought valiantly and defeated",troll,"trolls but is no more.")