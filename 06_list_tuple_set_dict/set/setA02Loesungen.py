geradeZahlen = {2, 4, 6, 8}
ungeradeZahlen = {1, 3, 5, 7}

alleZahlen = ungeradeZahlen.union(geradeZahlen)
gemeinsameZahlen = ungeradeZahlen.intersection(geradeZahlen)

print(alleZahlen, gemeinsameZahlen)