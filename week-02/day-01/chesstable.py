# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#

a = '%'
b = " "
c = int(input('How long chess table?: '))
d = 0
while d < c:
  print((a + b) * 4)
  print((b + a) * 4)
  d += 1