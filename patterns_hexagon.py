size = int(input())

# Upper part of the hexagon
for i in range(size):
    print(" " * (size - i - 1) + "*" * (size + 2 * i))

# Lower part of the hexagon
for i in range(size - 1, -1, -1):
    print(" " * (size - i - 1) + "*" * (size + 2 * i))
