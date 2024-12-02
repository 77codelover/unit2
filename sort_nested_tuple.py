tup = [(1,(2,5)),(1,(4,3)),(5,(2,5))]
sort_tup = sorted(tup, key=lambda t: [t[1][1],[0]])
print(sort_tup)