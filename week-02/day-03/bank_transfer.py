accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

def balance():
    for i in accounts:
        x = i.get('client_name')
        y = i.get('balance')
        print(x, y)

balance()

def transfer():
    
    anr1 = int(accounts[0].get('account_number'))
    abl1 = int(accounts[0].get('balance'))
    anr2 = int(accounts[1].get('account_number'))
    abl2 = int(accounts[1].get('balance'))
    anr3 = int(accounts[2].get('account_number'))
    abl3 = int(accounts[2].get('balance'))

    
    givemenumber = int(input('which account do you want to transfer from?: '))
    for b in accounts:
        if givemenumber == b.get('account_number'):
            destination = input('where to would you like to transfer?: ')
            amount = int(input('Amount: '))
            execute = input('Wish to transfer?: y/n ')
            if execute == 'y':
                abl1 -= amount
                abl2 += amount
                print('Transaction complete')
                break
            else:
                print('Transfer cancelled')
                break
                
            print('Account1: ', abl1, 'Account2: ', abl2)

        elif givemenumber != b.get('account_number'):
            print('404 - account not found')
            break

    
transfer()
    
        