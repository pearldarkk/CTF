# s = []
# for i in range(0, 240):
#     s.append(idc.get_wide_byte(0x00590036 + 2 * i + i))
s = "011001100011011010000110111001101101111000100110111101100111011000101110111110100110011011110110010011101110011010100110001011101111101000101110000101101010011011111010001011100100111010100110100001101100111010101110010011101010011010111110"
s = "".join(map(str, s))
print("".join(chr(int(s[i:i + 8][::-1], 2)) for i in range(0, len(s), 8)))
