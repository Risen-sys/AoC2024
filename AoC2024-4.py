InputList = []
with open(r"C:\Users\MatthewSilbernagel\Desktop\input.txt", "r") as data:
    for t in data:
        InputList.append(t.strip())

XSet = set()
MSet = set()
ASet = set()
SSet = set()
for y, f in enumerate(InputList):
    for x, c in enumerate(f):
        Coord = (x, y)
        if c == "X":
            XSet.add(Coord)
        elif c == "M":
            MSet.add(Coord)
        elif c == "A":
            ASet.add(Coord)
        elif c == "S":
            SSet.add(Coord)

Directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
Part1Answer = 0
for Ex in XSet:
    X, Y = Ex
    for DX, DY in Directions:
        Em = (X+DX,Y+DY)
        Ay = (X+2*DX, Y+2*DY)
        Es = (X+3*DX, Y+3*DY)
        if Em in MSet and Ay in ASet and Es in SSet:
            Part1Answer += 1

Part2Answer = 0
for Ay in ASet:
    X, Y = Ay
    TopL, TopR, BotL, BotR = (X-1,Y-1),(X+1,Y-1),(X-1,Y+1),(X+1,Y+1)
    if TopL in MSet and TopR in MSet and BotL in SSet and BotR in SSet:
        Part2Answer += 1
        continue
    for q in range(3):
        TopL, TopR, BotR, BotL = TopR, BotR, BotL, TopL
        if TopL in MSet and TopR in MSet and BotL in SSet and BotR in SSet:
            Part2Answer += 1
            break
    
print(f"{Part1Answer = }")
print(f"{Part2Answer = }")