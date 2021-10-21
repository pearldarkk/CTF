import base64

def bitwise_xor_bytes(a, b):
    result_int = int.from_bytes(a, byteorder="big") ^ int.from_bytes(b, byteorder="big")
    return result_int.to_bytes(max(len(a), len(b)), byteorder="big")

AESblocksize = 16
authtoken = 'iHVcYuCO7VXUmvo+pb4XTs1NgMF6GhNkP+pCJ4aSYxU='
username = 'iamabear11111' # 13 ký tự cho tiện, gộp vào đủ 16 bytes
role = 1

usernamebytes = username.encode('utf-8')
plainbytes = len(usernamebytes).to_bytes(2, "little") + usernamebytes + role.to_bytes(1, "little")  # 16 bytes

encrypted_iv = base64.b64decode(authtoken)[:16]
cipher = base64.b64decode(authtoken)[16:]

key_and_iv = bitwise_xor_bytes(cipher, plainbytes)

new_role = 0
new_plainbytes = len(usernamebytes).to_bytes(2, "little") + usernamebytes + new_role.to_bytes(1, "little")

new_cipher = bitwise_xor_bytes(key_and_iv, new_plainbytes)
new_authtoken = base64.b64encode(encrypted_iv + new_cipher)

print(new_authtoken)