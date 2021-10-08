import hashlib

md5s = [
    # 174282896860968005525213562254350376167, # ALEXC
    #137092044126081477479435678296496849608,
    126300127609096051658061491018211963916,
    314989972419727999226545215739316729360,
    256525866025901597224592941642385934114,
    115141138810151571209618282728408211053,
    8705973470942652577929336993839061582,
    256697681645515528548061291580728800189,
    39818552652170274340851144295913091599,
    65313561977812018046200997898904313350,
    230909080238053318105407334248228870753,
    196125799557195268866757688147870815374,
    74874145132345503095307276614727915885
]

flag = [""] * 15
flag[0] = 'ALEXC'
flag[1] = 'TF{dv'
sample1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
sample = 'abcdefghijklmnopqrstuvwxyz0123456789_'

for i1 in sample:
    for i2 in sample:
        for i3 in sample:
            for i4 in sample:
                for i5 in sample:
                    s = i1 + i2 + i3 + i4 + i5
                    hash_num = int('0x' + hashlib.md5(s.encode()).hexdigest(),
                                   16)
                    for i in range(0, len(md5s)):
                        if hash_num == md5s[i]:
                            flag[i + 2] = s
                            print(s)
flag[12] = '6v3k}'

for i in range(0, len(flag)):
    print(flag,end='')

#flag
# ALEXCTF{dv5d4s2vj8nk43s8d8l6m1n5l67ds9v41n52nv37j481h3d28n4b6v3k}
# Output
# ds9v4:5
# n5l67:4
# vj8nk:1
# v37j4:7
# 1n52n:6
# 28n4b:9
# 43s8d:2
# 5d4s2:0
# 8l6m1:3
# 81h3d:8