# flag = b"NhaTrang{hello_from_h3ll}"
with open('flag.txt', 'rb') as f:
    flag = f.read().strip()

key = "Fsoft"
enc = b""
for i in range(len(flag)):
    enc += bytes([flag[i] ^ ord(key[i % len(key)])])

with open('enc.txt', 'w') as f:
    for c in enc:
        f.write('%02x' % c)

# import py2exe
# py2exe.freeze(console=["re1-chall.py"],windows=[],data_files=None,zipfile=None,options={"bundle_files":0},version_info={})