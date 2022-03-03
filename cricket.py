score1 = [1,2,3,4,2]
p1=[]
p2=[]
for i in score1:
    if i % 2 != 0:
        p1.append(i)
    else:
        p2.append(i)
print("P1 is:", sum(p1))
print("P2 is:", sum(p2))
