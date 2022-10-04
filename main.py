max_sum = 47
buffer = dict()
def F(k1,k2):
    if (k1,k2) in buffer.keys():
        return buffer[(k1,k2)]
    if k1 + k2 >= max_sum:
        return "win"
    moves = [F(k1+4,k2),F(k1,k2+4),F(k1*4,k2),F(k1,k2*4)]
    if "win" in moves: 
        buffer[(k1,k2)]
        return "win1"
    if all(x == "win1" for x in moves):
        buffer[(k1,k2)]
        return "loose1"
    if "loose1" in moves:
        buffer[(k1,k2)] 
        return "Win2"
    if all(x == "Win2" for x in moves) == len(moves):
        buffer[(k1,k2)]
        return "loose2"
    if all(x == "Loose2" for x in moves)+ all(x == "Win2" for x in moves) == len(moves):
        buffer[(k1,k2)]
        return "loose21"

for k2 in range(1,57+1):
    print(k2,F(1,))
