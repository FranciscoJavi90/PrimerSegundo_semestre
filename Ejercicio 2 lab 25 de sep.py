a = [[5,6,3],[4,2,0],[6,1,3]]
b = [[50,16,37],[45,12,8],[6,10,3]]
c = [[0,0,0],[0,0,0],[0,0,0]]

for x in range(0,3):

    for y  in range(0,3):

        c[x][y] = a[x][y] = b[x][y]

for x in range(0,3):

    for y in range(0,3):

        print(str(c[x][y]))

    print("\n")