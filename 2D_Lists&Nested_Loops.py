number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid)
print(number_grid[0])
print(number_grid[2][1])

for row in number_grid:
    print(row)

for row in number_grid:
    for column in row:
        print(column)


a = "abcdefg"
for x in a :
    print(x)