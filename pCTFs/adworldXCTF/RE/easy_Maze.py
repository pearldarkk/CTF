# Debug to get the maze
# s = bytearray()
# Python>offset = 0x00007FFD6D899750
# Python>for i in range(49):
# Python> s.append(get_wide_dword(offset + 4*i))
# Python>print(s)
maze = bytearray(
    b'\x01\x00\x00\x01\x01\x01\x01\x01\x00\x01\x01\x00\x00\x01\x01\x01\x01\x00\x01\x01\x01\x00\x00\x00\x01\x01\x00\x00\x01\x01\x01\x01\x00\x00\x00\x01\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\x00\x01'
)
maze = [int(_) for _ in maze]
for i in range(len(maze)):
    if i % 7 == 0:
        print()
    print(maze[i], end='')