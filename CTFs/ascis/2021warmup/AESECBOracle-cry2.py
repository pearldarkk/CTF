import math
import requests


def req(inp):
    url = "http://125.235.240.166:20104/encrypt"
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://125.235.240.166:20104",
        "Connection": "close",
        "Referer": "http://125.235.240.166:20104/",
        "Upgrade-Insecure-Requests": "1"
    }
    data = {"input": inp.encode().hex()}
    res = requests.post(url, headers=headers, data=data)
    return res.text


def chunkstring(string, length):
    return (string[0 + i:length + i] for i in range(0, len(string), length))


def roundup(x, base=10):
    return int(math.ceil(x / (base + 0.0))) * base


try:
    found = False
    secret = ""

    secretLen = 0
    prependChars = ""

    message = "A"
    data = req(message)
    output = list(chunkstring(data, 32))
    initialLen = len(output)

    curLen = 0

    while (curLen <= initialLen):
        message += "A"
        data = req(message)
        output = list(chunkstring(data, 32))
        curLen = len(output)

    extra = len(message) - 1

    secretLen = ((curLen - 1) * 16) - extra - len(prependChars)

    print("SECRETLEN: " + str(secretLen))

    while not found:
        initialBlock = "A" * (16 - len(prependChars))
        fullLen = roundup(secretLen, 16)
        prepend = "B" * (fullLen - len(secret) - 1)
        message1 = initialBlock + prepend

        data = req(message1)
        initialReturn = list(chunkstring(data, 32))
        # print "INITIAL: " + str(initialReturn)

        for i in range(33, 127):
            message2 = message1 + secret + chr(i)
            data = req(message2)
            oracle = list(chunkstring(data, 32))
            # print "ORACLE: " + str(oracle)
            compareBlock = (len(prependChars + message2) // 16) - 1
            # print "COMPARE = " + str(compareBlock)
            if oracle[compareBlock] == initialReturn[compareBlock]:
                secret += chr(i)
                # print "LENGTH: " + str(len(secret))
                # print "SECRET: " + secret
                # print "INITIAL: " + str(initialReturn)
                # print "ORACLE: " + str(oracle)
                if len(secret) == secretLen:
                    found = True
                    print(secret)
                break

finally:
    pass
