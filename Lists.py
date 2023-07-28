friends = ["CB", "Rayne", "Oakley", "Joe", "Nico", "Tox", "Ori", "Nari"]
list = ["eee", "EEE", 3.14, 0, True, False]

print(friends)
print(list)

print(friends[1])
print(friends[-1])
print(friends[2:])
print(friends[3:6])

friends[0] = "Mystic"
print(friends[0])

friends.append("Seb")
print(friends)

friends.insert(4, "Winter")

print(friends.index("Nico"))

friends2 = friends.copy()
friends3 = friends

friends.sort()
print(friends)

friends.remove("Joe")
print(friends)

new_list = friends + list
print(new_list)

list1 = friends[1:] 
print(list1)

del friends[2]
print(friends)

# pop will automatically remove the last item if no index is specified
item2=friends.pop(2)
print(friends)
print(item2)

friends.sort(reverse=True)
print(friends)

# === second day ===
friends.extend(list)
print(friends)

friends.clear()
print(friends)

random_numbers = [2,5,6,5,3.4,6,7.2,8.9,6,3.4,5.2]
print(random_numbers.count(6))

random_numbers.reverse()
print(random_numbers)

random_numbers.sort()
print(random_numbers)

print(friends2)
print(friends)

print(len(random_numbers))