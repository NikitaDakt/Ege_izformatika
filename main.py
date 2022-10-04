max_sum = 41
buffer = dict()
def F(k1,k2,v):
    if (k1,k2,v) in buffer.keys():
        return buffer[(k1,k2,v)]
    if k1 + k2 >= max_sum:
        buffer[(k1,k2,v)]
        return "win"
    moves = []
    print(k1,k2,v)
    if v != 1:moves.append(F(k1+4,k2,1))
    if v != 2:moves.append(F(k1,k2+4,2))
    if v != 3:moves.append(F(k1*4,k2,3))
    if v != 4:moves.append(F(k1,k2*4,4))

    if "win" in moves: 
        buffer[(k1,k2,v)]
        return "win1"
    if all(x == "win1" for x in moves):
        buffer[(k1,k2,v)]
        return "loose1"
    if "loose1" in moves:
        buffer[(k1,k2,v)] 
        return "Win2"
    if all(x == "Win2" for x in moves) == len(moves):
        buffer[(k1,k2,v)]
        return "loose2"
    if all(x == "Loose2" for x in moves)+ all(x == "Win2" for x in moves) == len(moves):
        buffer[(k1,k2,v)]
        return "loose21"

k1 = 7
for k2 in range(1,33+1):
    print(k2,F(k1,k2,0))
