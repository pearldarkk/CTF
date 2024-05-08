import base64 as rtfd
import webbrowser
import time
def mikeSwift(cre):
    sto = []
    gre = ""
    for i in cre:
        sto.append(i+str(len(i)))
        sto.append("h4ck" + i)
    for i in sto:
        gre+=i
    return gre
def prompt():
    return bytes(input("Welcome to the loading dock. What is the password?\t"), 'utf-8')
def obfuscate(bys):
    fusc = rtfd.b64encode(bys)
    fusc += b"534345fdfgfgfdhty6y56yjl"
    fusc = str(fusc)
    fusc = fusc[2:len(fusc)-1]
    refus = []
    for i in fusc:
        refus.append((str(i)))
    fusc="florSFIUEfet4565477"
    for i in refus:
        fusc+=i
    return fusc
def crypt(sor):
    sro = []
    fusc = "893"
    for i in range(len(sor)):
        sro.append(sor[i]+str(i))
    sro.reverse()
    for i in sro:
        fusc+=i
    return fusc
def grant():
    print("Congratulation. Pleas Procid")
    webbrowser.open("") # Link challenge sau khi up
def punish():
    print("This is going to hurt.")
    while True:
        time.sleep(.1)
        webbrowser.open("https://www.youtube.com/watch?v=KuAgAEvlzBk")
def main():
    sik1 = prompt()
    sik = obfuscate(sik1)
    sik = crypt(sik)
    sik = mikeSwift(sik)
    if sik == "81h4ck891h4ck931h4ck3l1h4ckl71h4ck741h4ck4j1h4ckj71h4ck731h4ck3y1h4cky71h4ck721h4ck261h4ck671h4ck711h4ck151h4ck571h4ck701h4ck0y1h4cky61h4ck691h4ck961h4ck661h4ck681h4ck8y1h4cky61h4ck671h4ck7t1h4ckt61h4ck661h4ck6h1h4ckh61h4ck651h4ck5d1h4ckd61h4ck641h4ck4f1h4ckf61h4ck631h4ck3g1h4ckg61h4ck621h4ck2f1h4ckf61h4ck611h4ck1g1h4ckg61h4ck601h4ck0f1h4ckf51h4ck591h4ck9d1h4ckd51h4ck581h4ck8f1h4ckf51h4ck571h4ck751h4ck551h4ck561h4ck641h4ck451h4ck551h4ck531h4ck351h4ck541h4ck441h4ck451h4ck531h4ck331h4ck351h4ck521h4ck251h4ck551h4ck511h4ck1=1h4ck=51h4ck501h4ck001h4ck041h4ck491h4ck9n1h4ckn41h4ck481h4ck8c1h4ckc41h4ck471h4ck7w1h4ckw41h4ck461h4ck6Q1h4ckQ41h4ck451h4ck5H1h4ckH41h4ck441h4ck4N1h4ckN41h4ck431h4ck3j1h4ckj41h4ck421h4ck2V1h4ckV41h4ck411h4ck1T1h4ckT41h4ck401h4ck0d1h4ckd31h4ck391h4ck9m1h4ckm31h4ck381h4ck8J1h4ckJ31h4ck371h4ck7G1h4ckG31h4ck361h4ck6M1h4ckM31h4ck351h4ck5n1h4ckn31h4ck341h4ck4R1h4ckR31h4ck331h4ck3T1h4ckT31h4ck321h4ck2M1h4ckM31h4ck311h4ck1m1h4ckm31h4ck301h4ck0t1h4ckt21h4ck291h4ck9n1h4ckn21h4ck281h4ck8Y1h4ckY21h4ck271h4ck711h4ck121h4ck261h4ck6x1h4ckx21h4ck251h4ck521h4ck221h4ck241h4ck4Y1h4ckY21h4ck231h4ck3w1h4ckw21h4ck221h4ck2N1h4ckN21h4ck211h4ck1X1h4ckX21h4ck201h4ck0a1h4cka11h4ck191h4ck971h4ck711h4ck181h4ck871h4ck711h4ck171h4ck741h4ck411h4ck161h4ck651h4ck511h4ck151h4ck561h4ck611h4ck141h4ck451h4ck511h4ck131h4ck341h4ck411h4ck121h4ck2t1h4ckt11h4ck111h4ck1e1h4cke11h4ck101h4ck0f1h4ckf91h4ck9E1h4ckE81h4ck8U1h4ckU71h4ck7I1h4ckI61h4ck6F1h4ckF51h4ck5S1h4ckS41h4ck4r1h4ckr31h4ck3o1h4cko21h4ck2l1h4ckl11h4ck1f1h4ckf01h4ck0":
        grant()
    else:
        punish()
main()