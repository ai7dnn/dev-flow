print('20221234 홍길동')

comp = [i if i%3 == 0 else i/2 for i in range(1, 10, 3)]
maplst = list(map(lambda x: x, list(range(1, 10, 2))))

print(comp)
print(maplst)
