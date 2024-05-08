import base64

#  A new custom charset
#  Change this guy to desired string. Append the "=" char if you also want to possibly change its location.
cuscharset = "ABDCEHGFIJKLUNOPYRTSMVWXQZajcdefohibkmlngpqrstuv4xzy8123w56709+0"

#  The standard charset
#  If you added an "=" char, or some other char to cuscharst above, make sure to add it here as well.
b64charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

encodedset = str.maketrans(b64charset, cuscharset)
decodedset = str.maketrans(cuscharset, b64charset)


def dataencode(x):
    y = base64.b64encode(x)
    y = y.translate(encodedset)
    return y


def datadecode(x):
    y = x.translate(decodedset)
    y = base64.b64decode(y)
    return y


print(datadecode("c3Yo"))