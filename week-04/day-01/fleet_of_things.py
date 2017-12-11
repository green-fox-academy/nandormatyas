from fleet import Fleet
from thing import Thing

fleet = Fleet()

todo = ["Get milk", "Remove the obstacles"]
completed=["Stand up", "Eat lunch"]

for i in todo:
    x = Thing(i)
    fleet.add(x)
for j in completed:
    y = Thing(j)
    y.complete()
    fleet.add(y)

#Thing(fleet)



# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

print(fleet)