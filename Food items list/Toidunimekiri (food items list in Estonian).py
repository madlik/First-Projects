# TOIDUNIMEKIRJA KOOSTAMINE JA MUUTMINE

# Funktsioonid

# MENÜÜ
def menu():
    while True:
        print("""\nTere tulemast koostama toidunimekirja!
Menüü:
1 - Kuva nimekiri
2 - Lisa toode
3 - Kustuta toode
4 - Kustuta terve nimekiri
5 - Välju
""")
        valik = input("Mida soovid teha? Sisesta number: ")
        match valik:
            case "1":
                show()
            case "2":
                add()
            case "3":
                delete()
            case "4":
                deleteall()
                show()  # Optionally show the updated list after deletion
            case "5":
                print("Nimekiri on koostatud! Nägemist!")
                break  # Exit the loop and the program
            case _:
                print("\n\033[91mVäär sisend\033[0m\n")

# LISA NIMEKIRJA TOODE
def add():
    while True:
        with open("toidunimekiri.txt", encoding="utf-8") as f:
            sisu = f.read().splitlines()  # Read lines into a list

        show()
        
        toode = input("Lisa toidunimekirja toode või vajuta 'ENTER' nimekirjast väljumiseks: ").lower()
        if toode == "":
            return
        
        if toode not in sisu:
            with open("toidunimekiri.txt", "a", encoding="utf-8") as f:
                f.write("\n" + toode)
            print("Toode on lisatud nimekirja")
        else:
            print((toode + " on juba nimekirjas.").capitalize())

# NÄITA TOIDUNIMEKIRJA
def show():
    with open("toidunimekiri.txt", encoding="utf-8") as f:
        nimekiri = f.read()
    print("\nNimekirjas on:\n" + nimekiri)

# KUSTUTA TOODE NIMEKIRJAST
def delete():
    while True:
        with open("toidunimekiri.txt", encoding="utf-8") as f:
            sõnelist = f.read().splitlines()

        show()
        
        eemaldatav_toode = input("Sisesta toode, mille soovid nimekirjast kustutada või vajuta 'ENTER' nimekirjast väljumiseks: ").lower()
        if eemaldatav_toode == "":
            return
        
        if eemaldatav_toode in sõnelist:
            sõnelist.remove(eemaldatav_toode)
            with open("toidunimekiri.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(sõnelist))
            print(eemaldatav_toode.capitalize() + " on nimekirjast eemaldatud.")
        else:
            print("\n" + eemaldatav_toode.capitalize() + " ei ole nimekirjas.")

# KUSTUTA TERVE NIMEKIRI
def deleteall():
    küsimus = input("Kas oled kindel, et soovid nimekirja kustutada? (jah/ei) ").lower()
    if küsimus == "jah":
        with open("toidunimekiri.txt", "w", encoding="utf-8") as f:
            f.write("")
        print("Nimekiri on kustutatud.")
    else:
        print("Nimekirja kustutamine katkestati.")

def main():
    menu()

if __name__ == "__main__":
    main()
