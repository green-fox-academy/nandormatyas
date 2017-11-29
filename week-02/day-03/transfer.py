
#Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

def transfer():
    clients = {}
    for i in accounts:
        for u in i:
            client = {i.get('account_number'):i.get('balance')}
            clients.update(client)
            
    
    accnrfrom = int(input('From Account?: '))
    if accnrfrom in clients.keys():
        accnrto = int(input('To account?: '))
        amount = int(input('Amount?: '))
        balfrom = clients.get(accnrfrom) 
        balto = clients.get(accnrto)
        balfrom = float(balfrom)
        balto = float(balto)
        clients[accnrfrom] -= amount
        clients[accnrto] += amount

    else:
        print("404 - account not found")

    #print(clients)

transfer()