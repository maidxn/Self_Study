size = int(input())

indent = (size - 1) * 2
lines = 2 * (size - 1) + 1
pos = 96 + size
left = [chr(pos)]
right = []
for line in range(lines):
    print("-" * abs(indent), end="")
    print(*left, sep="-", end="")
    if right:
        print("-", end="")
    print(*right, sep="-", end="")
    print("-" * abs(indent))
    if line < size - 1:
        right.insert(0, chr(pos))
        pos -= 1
        left.append(chr(pos))
    else:
        if right:
            right.pop(0)
        left.pop(-1)
    indent = 0 if 0 < indent <= 2 else indent - 2
