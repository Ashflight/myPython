# Data types in Python are called classes. The built-in ones Python has are strings, numbers and booleans.
# But you can create your own classes to represent various types of data.
# An item in a class is an "object".

from More_Copypasta import Member

JISOO_BLACKPINK = Member("JISOO", 28, "Visual and Vocalist", False)
Bang_Chan_SKZ = Member("Bang Chan", 25, "Leader and Vocalist", True)

print(JISOO_BLACKPINK.name)
print(JISOO_BLACKPINK.age)
print(JISOO_BLACKPINK.positions)

print(Bang_Chan_SKZ.name)
print(Bang_Chan_SKZ.age)
print(Bang_Chan_SKZ.positions)