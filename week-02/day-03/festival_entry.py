watchlist = []

security_alcohol_loot = 0

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

# Queue of festivalgoers at entry
# no. of alcohol units 
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival

# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

def security_check():
    watchlist = list()
    security_alcohol_loot = 0
    enter = 0
    for i in queue:
        guns = i.get('guns')
        alcohol = i.get('alcohol')
        name = i.get('name')
        #for i in queue:
        if guns == 0 and alcohol == 0:
            enter += 1
            
        elif guns > 0:
            watchlist.append(name)
            security_alcohol_loot += alcohol
            alcohol = 0
            guns = 0        
            enter +=1   
            


        #for i in queue:        
        elif alcohol > 0:
            security_alcohol_loot += alcohol
            alcohol = 0
            enter += 1
            
        
                

    return watchlist, security_alcohol_loot, enter, queue


print(security_check())







