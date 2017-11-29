# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Bözsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Béla", "Todd", "Neef", "Jeff"]
order = []
i = 0
for girl in girls:
    order.append(girl)
    for boy in range(1):
        order.append(boys[0 + i])
        
        i += 1
    
        


print(order)