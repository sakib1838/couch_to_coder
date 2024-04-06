rivers = [
 {"name": "Nile", "length": 4157},
 {"name": "Yangtze", "length": 3434},
 {"name": "Murray-Darling", "length": 2310},
 {"name": "Volga", "length": 2290},
 {"name": "Mississippi", "length": 2540},
 {"name": "Amazon", "length": 3915}
]

# printing all the river's name
print("All the river's name")
for river in rivers:
    print(river['name'])

# calculating and printing all the river's name
print("Calculating total length of the rivers...")
l=0
for river_length in rivers:
    l+= river_length['length']
print(f"Total Length of River's is: {l}")

# printing all the river's name begins with letter M
print("Name of the rivers begins with letter M")
for river in rivers:
    if(river['name'][0]=='M'):
        print(river['name'])

# printing all the river's lenght in kilometer
# 1 Mile = 1.6 Kilometer
print("All the river's name within its length in Kilometer")
for river in rivers:
    print(f"{river['name']}'s length is {river['length']*1.6:.2f} Kilometer")