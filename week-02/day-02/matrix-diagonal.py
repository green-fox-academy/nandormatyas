# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output



''' for r in range(4):
     for c in range(4):
          print(int(c==r), end=" ")
     print()
 '''

a = [[0 for x in range(4)] for y in range(4)]
for x in range(4):
    for y in range(4):
        if x==y:
            a[x][y]=1
    print(a[x])

#print(a)


