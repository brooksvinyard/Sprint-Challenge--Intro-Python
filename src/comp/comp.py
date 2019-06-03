# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []

for d in range(len(humans)):
    if humans[d].name[0] == "D":
        a.append(humans[d].name)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []

for e in range(len(humans)):
    if humans[e].name[-1] == "e":
        b.append(humans[e].name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []

for cg in range(len(humans)):
    if humans[cg].name[0].lower() in ["c", "d", "e", "f", "g"]:
        c.append(humans[cg].name)
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []

for ageTen in range(len(humans)):
    d.append(humans[ageTen].age+10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []

for hyphen in range(len(humans)):
    e.append(f"{humans[hyphen].name}-{humans[hyphen].age}")
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []

for tuples in range(len(humans)):
    if humans[tuples].age > 26 and humans[tuples].age < 33:
        insideTuple = (humans[tuples].name, humans[tuples].age)
        f.append(insideTuple)
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []

for newHuman in range(len(humans)):
    insideHuman = Human(humans[newHuman].name.upper(), humans[newHuman].age+5)
    g.append(insideHuman)
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []

for newMath in range(len(humans)):
    h.append(math.sqrt(humans[newMath].age))
print(h)
