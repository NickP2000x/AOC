"""
p, o
rock = X, A
paper = Y, B
scissors = Z, C
win = 8 
tie = 6
loss = 1
"""
player_total = 0

with open('day2/input.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
    for i in lines:
        p = i[2]
        o = i[0]
"""
        if o == "A":
            if p == "X":
                player_total += 3
            elif p == "Y":
                player_total += 4
            elif p == "Z":
                player_total += 8
        if o == "B":
            if p == "X":
                player_total += 1
            elif p == "Y":
                player_total += 5
            elif p == "Z":
                player_total += 9
        if o == "C":
            if p == "X":
                player_total += 2
            elif p == "Y":
                player_total += 6
            elif p == "Z":
                player_total += 7
"""
"""
        if p == "X":
            player_total += 1
            if o == "C":
                player_total += 6
            elif o == "B":
                player_total += 0
            elif o == "A":
                player_total += 3
        elif p == "Y":
            player_total += 2
            if o == "C":
                player_total += 0
            elif o == "B":
                player_total += 3
            elif o == "A":
                player_total += 6
        elif p == "Z":
            player_total += 3
            if o == "C":
                player_total += 3
            elif o == "B":
                player_total += 6
            elif o == "A":
                player_total += 0
"""
print(player_total)