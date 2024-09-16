

def karakter_for_prosent(prosentscore: int):
    if prosentscore >= 90:
        return"A"
    elif prosentscore >=80:
        return"B"
    elif prosentscore>=70:
        return "C"
    elif prosentscore >= 60:
        return "D"
    elif prosentscore >= 50:
        return "E"
    elif prosentscore >=40:
        return "F"


def skriv_ut_karakter(nummer):
    prosentscore = int (input("skriv inn en prosentscore :"))
    bokstavkarakter = karakter_for_prosent(prosentscore)
    print(f"karakteren for {nummer} ble {bokstavkarakter}")
    
skriv_ut_karakter(284034)


