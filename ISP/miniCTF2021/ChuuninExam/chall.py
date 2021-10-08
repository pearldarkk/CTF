from Crypto.Util.number import getRandomInteger
from string import *
import time


def stage1():  #caesar box
    print('\n\n\n***\nFirst Stage: Written test')
    intro = '\nGiven a ciphertext encrypted using the Roman method of cryptography...\n\n\n'
    print(intro)
    time.sleep(3)

    # challenge
    print('My ciphertext:\n')
    m = 'Developed around 100 BC, not until 9th-century, Caesar cipher was cracked with the discovery of frequency analysis.'
    key = getRandomInteger(2) % 13 + 7  # range 7 - 26
    # encrypt
    upper = ascii_uppercase
    lower = ascii_lowercase
    c = ''
    for ch in m:
        if ch in upper:
            c += upper[(upper.index(ch) + key) % 26]
        elif ch in lower:
            c += lower[(lower.index(ch) + key) % 26]
        else:
            c += ch
    print(c)
    buf = input('\n\n\nWhat is the messages?\n\n')
    time.sleep(1)
    # if pass
    if buf == m:
        print(
            '\n\n\nYou are qualified to the Second Stage!'
        )
    else:
        print('\n\n\nFailed! You are disqualified!')
        exit(-1)


def stage2():
    print('\n\n\n***\nSecond Stage: Forest of Death')
    intro = '\nYou have to bring your team\'s Scroll to the Building whose position is encrypted by an ancient Greek technique...\n\n\n'
    print(intro)
    time.sleep(3)

    # challenge
    print('My ciphertext:\n')
    m = 'Located_at_port_2026_encrypted_by_Scytale'
    # encrypt
    chrs = getRandomInteger(1) + 3  #max chars per lap in range 3 - 7
    c = ''
    rounds = (len(m) + chrs - 1) // chrs
    pad = rounds * chrs - len(m)  #padding
    for ch in range(pad):
        m += ' '
    for lap in range(rounds):
        for ch in range(chrs):
            c += m[ch * rounds + lap]
    print(c)
    buf = input('\n\n\nWhat is the messages?\n\n')
    time.sleep(1)

    # if pass
    m = m.replace(' ', '')
    if buf == m:
        print(
            '\n\n\nYou are qualified to the Final Stage!'
        )
    else:
        print('\n\n\nFailed! You are disqualified!')
        exit(-1)


def stage3():
    print('\n\n\n***\nFinal Stage: Team Fight')
    intro = '\nThe key of teamwork in a fight is to communicate secretly.\nThis was created at the end of the First World War in German.\n\n\n'
    print(intro)
    time.sleep(3)

    # challenge
    m = 'enigmaisformilitarycommunication'
    # encrypt
    print('Your team using this machine:\n')
    print('_________________________________________________________________\n')
    print('Machine: Enigma M3, reflector UKW B')
    print('Rotor - Position - Ring: III - 9 - 3, II - 19 - 20, VI - 16 - 6 ')
    print('Plugboard: dq cr bi ej kw mt os px uz gh')
    print('_________________________________________________________________')
    print('\n\n\nMy ciphertext:')
    c = 'renoy begxr bczov ukkrg uasgc pkyjw sb'
    print(c)
    buf = input('\n\n\nWhat is the messages? (remove spaces)\n\n')
    time.sleep(1)

    # if pass
    if buf == m:
        print('\n\n\nPTITkagure proud of you as a new Chuunin!')
    else:
        print(
            '\n\n\nYou are not gonna pass the Chuunin exam like this. Give up!'
        )
        exit(-1)


def main():
    intro = 'Cryptography is the science of secrets.\nA proper Chuunin knows how important crypto is!'
    print(intro)
    time.sleep(2)

    stage1()
    time.sleep(3)
    stage2()
    time.sleep(3)
    stage3()
    time.sleep(0.5)
    print(
        'New S-rank Hiden Jutsu to you from ISP Ichizoku: ISPCLUB{s3cr3t_pr0t3ct0r}'
    )


if __name__ == '__main__':
    main()