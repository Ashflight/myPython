SKZ_copypasta = open("SKZ-copypasta", "r")
# There are different modes when it comes to opening files, "r" is read, where you cannot edit the file.
# "w" is write, where you can write in the file, but not read it.
# "a" is append, where you can append information onto the end of it but you cannot edit what's already there.
# You can combine modes, for example "r+w" for read and write.

print(SKZ_copypasta.readable())
# print(SKZ_copypasta.read())

print("---")

# print(SKZ_copypasta.readline())
# print(SKZ_copypasta.readline())

# print(SKZ_copypasta.readlines()[5])

# for member in SKZ_copypasta.readlines():
    # print(member)

# lineText=""
# while True :
#     lineText = SKZ_copypasta.readline()
#     if not lineText:
#         break
#     print(lineText)


SKZ_copypasta.close