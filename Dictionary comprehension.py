#Dictionary comprehension

names = [
    "Ashok",
    "Raiyan",
    "Meghana"
]

#List compersion
lengths = [len(name) for name in names]
print(lengths)

#Dictiory compersion
lengths = {name: len(name) for name in names}
print(lengths)