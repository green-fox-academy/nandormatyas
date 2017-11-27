# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was

number = int(input('enter number: '))
space = " "
percent = '%'
a = 0
print(percent * number + 2 * percent)

while a < number:
  print(percent + space * a + percent + (((number - a - 1) * space) + percent))

  a += 1

print(percent * number + 2 * percent)