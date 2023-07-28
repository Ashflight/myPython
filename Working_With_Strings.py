print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("Giraffe\\Academy")

phrase = "Giraffe Academy"
print(phrase + " is cool")

print(phrase.lower())
print(phrase.upper())
print(phrase.islower())
print(phrase.isupper())
print(phrase.upper().isupper())

i = "1"
print("i is upper")
print(i.isupper())
print("H0".isupper())

print(len(phrase))

print(phrase[0])
print(phrase[1])
print(phrase[2])
print(phrase[3])
print(phrase[4])
print(phrase[5])
print(phrase[6])
print(phrase[7])
print(phrase[8])
print(phrase[9])
print(phrase[10])
print(phrase[11])
print(phrase[12])
print(phrase[13])
print(phrase[14])

print("G index")
print(phrase.index("G"))
# print(phrase.index("g"))
print(phrase.index("i"))
print(phrase.index("r"))
print(phrase.index("a"))

print(phrase.index("Academy"))

if "Academy1" in phrase:
    print("yes, Academy is in phrase")
else:
    print("no, Academy1 is not in phrase")

print(phrase.replace("Giraffe", "Elephant"))