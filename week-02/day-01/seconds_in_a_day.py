current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables

hour = 3600
minute = 60
second = 1
day = 86400

current_hours = hour * current_hours
current_minutes = minute * current_minutes
current_seconds = second * current_seconds

a = current_hours + current_minutes + current_seconds
print(day - a)