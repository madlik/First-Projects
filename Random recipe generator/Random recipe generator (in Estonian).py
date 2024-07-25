from random import randint

#valida retseptide nimekirjast failis (sõnede list) suvaline retsept
def suvalise_retsepti_generaator():   
    try:
        f = open("Retseptid.txt", encoding="utf-8")
        retseptid_listiks = f.readlines()
        if not retseptid_listiks:
            print("Retseptide fail on tühi.")
            return
        maksimaalne_listi_pikkus = len(retseptid_listiks) - 1  #indekseerimine algab Ost, mitte 1st
        suvaline_indeks = randint(0, maksimaalne_listi_pikkus) 
        üks_retsept = retseptid_listiks[suvaline_indeks] 
        print(üks_retsept)
    except FileNotFoundError:
        print("Faili ei leitud.")

#kasutaja valib nimekirjast suvalise retsepti    
def retsepti_genereerimine():
    user_input = input("""Tere tulemast suvalise retsepti generaatorisse!
Retsepti genereerimiseks palun vajuta ENTER! """).strip()
    if user_input == "":
        print("\nSiin on üks suvaline retsept: \n")
        suvalise_retsepti_generaator()
    

def näita_kõiki_retsepte():
    try:
        f = open("Retseptid.txt", encoding="utf-8")
        retseptid = f.read()
        if not retseptid:
            print("Retseptide fail on tühi.")
        else:
            print(retseptid)
        f.close()
    except FileNotFoundError:
        print("Faili ei leitud.")

def menu():
    while True:
        print("""\nMenüü:
    1 - Veel üks retsept
    2 - Vaata kõiki retsepte
    3 - Välju
    """)
        valik = input("Mida soovid teha? Sisesta number: ").strip()
        match valik:
            case "1":
                print("\nSiin on üks suvaline retsept: \n")
                suvalise_retsepti_generaator()
            case "2":
                print("\nSiin on kõik retseptid: \n")
                näita_kõiki_retsepte()
            case "3": 
                print("Tänan kasutamast. Nägemist!")
                break
            case _:
                print("\n\033[91mVäär sisend\033[0m\n")
                
        

def main():
    retsepti_genereerimine()
    menu()
    
if __name__ == "__main__":
    main()
