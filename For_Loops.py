for letter in "Giraffe Academy":
    print(letter)

friends = ["Mystic", "Seb", "Joe", "Tox", "Nico", "Ori", "Nari"]
for name in friends:
    print(name)

for index in range(10):
    print(index)
# range does not include the final number, for example range(5) would actually print 0, 1, 2, 3, 4 but not 5.

for index in range(3, 10):
    print(index)
# However, range does include the first number.

print(len(friends))

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First loop")
    else:
        print("Not first loop")