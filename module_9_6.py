def all_variants4(text):
    k, j = 0, 0
    for j in range(len(text)):
        for k in range(len(text)):
            if j+k+1 < len(text)+1:
                yield text[k:(j+k+1)]

a =all_variants4('abc')
for i in a:
    print(i)



