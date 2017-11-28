# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

n = 4
a = [[0] * n]
for i in range(n):
  for j in range(n):
    if i != j:
      a[i][j] = 0
      print(a)
    else:
      a[i][j] = 1
      print(a)


    

