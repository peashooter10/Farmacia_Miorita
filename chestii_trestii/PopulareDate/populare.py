# populare baza de date:
# python modele.py
# python populare.py

import mysql.connector
import random

bazaDate = mysql.connector.connect(
    host="localhost",
    user="root",
    database="farmacia_miorita_test"
)
myCursor = bazaDate.cursor()

judete = [
    ("Alba",), ("Arad",), ("Argeș",), ("Bacău",), ("Bihor",),
    ("Bistrița-Năsăud",), ("Botoșani",), ("Brașov",), ("Brăila",), ("București",),
    ("Buzău",), ("Caraș-Severin",), ("Călărași",), ("Cluj",), ("Constanța",),
    ("Covasna",), ("Dâmbovița",), ("Dolj",), ("Galați",), ("Giurgiu",),
    ("Gorj",), ("Harghita",), ("Hunedoara",), ("Ialomița",), ("Iași",),
    ("Ilfov",), ("Maramureș",), ("Mehedinți",), ("Mureș",), ("Neamț",),
    ("Olt",), ("Prahova",), ("Satu Mare",), ("Sălaj",), ("Sibiu",),
    ("Suceava",), ("Teleorman",), ("Timiș",), ("Tulcea",), ("Vaslui",),
    ("Vâlcea",), ("Vrancea",)
]
localitati = [
    ("Alba Iulia", 1), ("Arad", 2), ("Pitești", 3), ("Bacău", 4), ("Oradea", 5),
    ("Bistrița", 6), ("Botoșani", 7), ("Brașov", 8), ("Brăila", 9), ("București", 10),
    ("Buzău", 11), ("Reșița", 12), ("Călărași", 13), ("Cluj-Napoca", 14), ("Constanța", 15),
    ("Sfântu Gheorghe", 16), ("Târgoviște", 17), ("Craiova", 18), ("Galați", 19),
    ("Giurgiu", 20), ("Târgu Jiu", 21), ("Miercurea Ciuc", 22), ("Deva", 23), ("Slobozia", 24),
    ("Iași", 25), ("București (Ilfov)", 26), ("Baia Mare", 27), ("Drobeta-Turnu Severin", 28),
    ("Târgu Mureș", 29), ("Piatra Neamț", 30), ("Slatina", 31), ("Ploiești", 32),
    ("Satu Mare", 33), ("Zalău", 34), ("Sibiu", 35), ("Suceava", 36),
    ("Alexandria", 37), ("Timișoara", 38), ("Tulcea", 39), ("Vaslui", 40),
    ("Râmnicu Vâlcea", 41), ("Focșani", 42)
]
strazi = [
    "Strada Libertății", "Strada Unirii", "Strada Mihai Eminescu", "Strada Nicolae Bălcescu",
    "Strada Tudor Vladimirescu", "Strada Avram Iancu", "Strada Horea", "Strada Cloșca",
    "Strada Crișan", "Strada Vasile Alecsandri", "Strada Ion Creangă", "Strada George Coșbuc",
    "Strada Octavian Goga", "Strada Lucian Blaga", "Strada Nicolae Iorga", "Strada Ștefan cel Mare",
    "Strada Alexandru Ioan Cuza", "Strada Regele Ferdinand", "Strada Regina Maria", "Strada Independenței",
    "Strada Victoriei", "Strada Păcii", "Strada Speranței", "Strada Primăverii",
    "Strada Eroilor", "Strada Martirilor", "Strada Republicii", "Strada 1 Decembrie",
    "Strada Gării", "Strada Școlii", "Strada Bisericii", "Strada Parcului"
]
medicamente = [
    ("Analgezice", ["Paracetamol", "Ibuprofen", "Aspirina", "Diclofenac", "Ketoprofen",
                    "Metamizol", "Naproxen", "Codeina", "Tramadol", "Morfina"]),
    ("Antibiotice", ["Amoxicilina", "Ampicilina", "Cefalexina", "Cefuroxima", "Ceftriaxona",
                     "Azitromicina", "Claritromicina", "Doxiciclina", "Ciprofloxacina", "Metronidazol"]),
    ("Antiinflamatoare", ["Indometacin", "Meloxicam", "Piroxicam", "Celecoxib", "Etoricoxib",
                          "Sulindac", "Nabumetona", "Tenoxicam", "Lornoxicam", "Flurbiprofen"]),
    ("Antialergice", ["Loratadina", "Desloratadina", "Cetirizina", "Levocetirizina",
                      "Fexofenadina", "Difenhidramina", "Clorfeniramina", "Ketotifen"]),
    ("Cardiovasculare", ["Atenolol", "Metoprolol", "Bisoprolol", "Carvedilol",
                         "Enalapril", "Lisinopril", "Losartan", "Valsartan", "Amlodipina"]),
    ("Anticoagulante", ["Heparina", "Enoxaparina", "Warfarina", "Rivaroxaban", "Apixaban"]),
    ("Antidiabetice", ["Metformin", "Glibenclamid", "Gliclazid", "Sitagliptin", "Insulina"]),
    ("Digestive", ["Omeprazol", "Esomeprazol", "Pantoprazol", "Metoclopramid", "Loperamid"]),
    ("Antidepresive", ["Sertralina", "Fluoxetina", "Paroxetina", "Citalopram", "Duloxetina"]),
    ("Anxiolitice", ["Diazepam", "Alprazolam", "Lorazepam", "Clonazepam", "Bromazepam"]),
    ("Respiratorii", ["Salbutamol", "Formoterol", "Budesonid", "Fluticazona", "Montelukast"]),
    ("Antivirale", ["Aciclovir", "Valaciclovir", "Oseltamivir", "Remdesivir"]),
    ("Antifungice", ["Fluconazol", "Itraconazol", "Ketoconazol", "Nistatina"]),
    ("Vitamine", ["Vitamina C", "Vitamina D", "Vitamina B12", "Calciu", "Magneziu", "Zinc"]),
    ("Dermatologice", ["Acid salicilic", "Clotrimazol", "Miconazol", "Hidrocortizon crema"]),
]
nume_familie = [
    "Popescu", "Ionescu", "Dumitrescu", "Constantinescu", "Gheorghiu", "Stan", "Radu",
    "Munteanu", "Stefan", "Dobre", "Marin", "Tudor", "Florea", "Radulescu", "Filip",
    "Ilie", "Sandu", "Barbu", "Chiriac", "Voicu", "Badea", "Petrescu", "Neagu", "Balan",
    "Mihai", "Serban", "Enache", "Cristea", "Dragan", "Stoica"
]
nume_baieti = [
    "Andrei", "Alexandru", "Mihai", "Stefan", "Gabriel", "Florin", "Cristian", "Ion",
    "Daniel", "Radu", "Vlad", "Victor", "George", "Razvan", "Ionut", "Darius", "Paul",
    "Tudor", "Bogdan", "Cosmin", "Marian", "Dragos", "Eduard", "Lucian", "Sorin"
]
nume_fete = [
    "Maria", "Andreea", "Elena", "Ioana", "Gabriela", "Ana", "Alexandra", "Cristina",
    "Larisa", "Diana", "Roxana", "Ramona", "Daniela", "Loredana", "Monica", "Simona",
    "Alina", "Adriana", "Nicoleta", "Mirela", "Georgiana", "Irina", "Bianca", "Lavinia"
]
domenii_email = ["gmail", "yahoo", "outlook"]

# generare valori

def genereazaAdresa(persoana=False):
    nr = random.randint(1, 100)
    strada = random.choice(strazi)
    if persoana and random.randint(0, 1) == 1:
        scara = random.choice(["A", "B", "C"])
        return f"{strada} scara {scara} apartamentul {nr}"
    return f"{strada} numarul {nr}"

def genereazaNume():
    x = random.randint(0, 3)
    familie = random.choice(nume_familie)

    if x == 0:
        prenume = random.choice(nume_baieti)
        return familie, prenume
    elif x == 1:
        p1 = random.choice(nume_baieti)
        p2 = random.choice([n for n in nume_baieti if n != p1])
        return familie, f"{p1} {p2}"
    elif x == 2:
        prenume = random.choice(nume_fete)
        return familie, prenume
    else:
        p1 = random.choice(nume_fete)
        p2 = random.choice([n for n in nume_fete if n != p1])
        return familie, f"{p1} {p2}"

def genereazaLocalitateRandom():
    x = random.randint(0, 41)
    return localitati[x][0], localitati[x][1], x + 1

# populare tabele

def populeazaJudete():
    myCursor.executemany("INSERT INTO Judet(judet) VALUES (%s)", judete)
    print(f"Judete: {myCursor.rowcount} randuri inserate")

def populeazaLocalitate():
    myCursor.executemany(
        "INSERT INTO Localitate(localitate, id_judet) VALUES (%s, %s)", localitati
    )
    print(f"Localitate: {myCursor.rowcount} randuri inserate")

def populeazaRoluri():
    roluri = [("Admin",), ("Farmacist",), ("Utilizator",)]
    myCursor.executemany("INSERT INTO Roluri(rol) VALUES (%s)", roluri)
    print(f"Roluri: {myCursor.rowcount} randuri inserate")

def populeazaCategorii():
    categorii = [(cat,) for cat, _ in medicamente]
    myCursor.executemany("INSERT INTO Categorii(categorie) VALUES (%s)", categorii)
    print(f"Categorii: {myCursor.rowcount} randuri inserate")

def populeazaEmail(n):
    emailuri_set = set()
    while len(emailuri_set) < n:
        familie, prenume = genereazaNume()
        email = f"{familie.lower()}.{prenume.lower().split()[0]}{random.randint(1,999)}@{random.choice(domenii_email)}.com"
        emailuri_set.add((email,))
    myCursor.executemany("INSERT INTO Email(email) VALUES (%s)", list(emailuri_set))
    print(f"Email: {myCursor.rowcount} randuri inserate")

def populeazaProducatori(n=20):
    nume_producatori = [
        "Medicamente Bune SRL", "RoPharma SA", "Healthy&Co", "House & Wilson",
        "MedLife Pharma", "FarmaTrust SRL", "BioMed Romania", "AlphaMed SRL",
        "MedExpert SA", "PharmaPlus SRL", "NaturMed", "EuroPharma", "MedCor SRL",
        "VitaPharm", "ProSanatate SRL", "MedStar SA", "FarmaRo SRL",
        "BioFarm SA", "Gedeon Richter Romania", "Terapia SA"
    ]
    producatori = []
    for i in range(n):
        localitate, id_judet, id_localitate = genereazaLocalitateRandom()
        adresa = genereazaAdresa(persoana=False)
        producatori.append((
            nume_producatori[i % len(nume_producatori)],
            adresa,
            id_localitate,
            i + 1,
            "furnizor"
        ))
    myCursor.executemany(
        "INSERT INTO Partener(denumire, adresa, id_localitate, id_email, tipPartener) VALUES (%s,%s,%s,%s,%s)",
        producatori
    )
    print(f"Producatori: {myCursor.rowcount} randuri inserate")

def populeazaFarmacii(n=50):
    farmacii = []
    for i in range(n):
        localitate, id_judet, id_localitate = genereazaLocalitateRandom()
        adresa = genereazaAdresa(persoana=False)
        farmacii.append((
            f"Farmacia Miorita {i+1}",
            adresa,
            id_localitate,
            20 + i + 1
        ))
    myCursor.executemany(
        "INSERT INTO Farmacii(denumire, adresa, id_localitate, id_email) VALUES (%s,%s,%s,%s)",
        farmacii
    )
    print(f"Farmacii: {myCursor.rowcount} randuri inserate")

def populeazaMedicamente():
    lista = []
    for id_categorie, (categorie, lista_med) in enumerate(medicamente, start=1):
        for med in lista_med:
            id_furnizor = random.randint(1, 20)  # unul din cei 20 producatori
            lista.append((med, id_categorie, id_furnizor))
    myCursor.executemany(
        "INSERT INTO Medicamente(denumire, id_categorie, id_furnizor) VALUES (%s,%s,%s)",
        lista
    )
    print(f"Medicamente: {myCursor.rowcount} randuri inserate")

def populeazaAngajati(n=200):
    angajati = []
    for _ in range(n):
        familie, prenume = genereazaNume()
        id_farmacie = random.randint(1, 50)
        angajati.append((familie, prenume, id_farmacie))  
    myCursor.executemany(
        "INSERT INTO Angajati(id_nume, id_prenume, id_farmacie) VALUES (%s,%s,%s)",
        angajati
    )
    print(f"Angajati: {myCursor.rowcount} randuri inserate")

def populeazaUtilizatori(n=10000):
    utilizatori = []
    for i in range(n):
        familie, prenume = genereazaNume()
        adresa = genereazaAdresa(persoana=True)
        localitate, id_judet, id_localitate = genereazaLocalitateRandom()
        utilizatori.append((
            familie,
            prenume,
            adresa,
            70 + i + 1,          
            id_localitate,
            random.randint(1, 3)  
        ))
    myCursor.executemany(
        "INSERT INTO Utilizatori(nume, prenume, adresa, id_email, id_localitate, id_rol) VALUES (%s,%s,%s,%s,%s,%s)",
        utilizatori
    )
    print(f"Utilizatori: {myCursor.rowcount} randuri inserate")

# apeluri in ordine

def populareBazaDeDate():
    populeazaJudete()
    populeazaLocalitate()
    populeazaRoluri()
    populeazaCategorii()
    populeazaEmail(10070)      # toate emailurile dintr-o data
    populeazaProducatori(20)   # emailuri 1-20
    populeazaFarmacii(50)      # emailuri 21-70
    populeazaMedicamente()
    populeazaAngajati(200)
    populeazaUtilizatori(10000) # emailuri 71-10070

    bazaDate.commit()
    myCursor.close()
    bazaDate.close()
    print("\nPopulare finalizata!")

populareBazaDeDate()