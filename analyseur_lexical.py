
#  PARTIE 3 : automates
 
def reconnaitre_identificateur(mot):
    etat = 0
    for caractere in mot:
        if etat == 0:
            if caractere.isalpha():
                etat = 1
            else:
                return False
        elif etat == 1:
            if caractere.isalnum():
                etat = 1
            else:
                return False
    return etat == 1
 
 
def reconnaitre_nombre(nb):
    etat = 0
    for caractere in nb:
        if etat == 0:
            if caractere.isdigit():
                etat = 1
            else:
                return False
        elif etat == 1:
            if caractere.isdigit():
                etat = 1
            else:
                return False
    return etat == 1
 
 
def reconnaitre_operateur(op):
    etat = 0
    for caractere in op:
        if etat == 0:
            if caractere in {"+", "-", "*", "/"}:
                etat = 1
            else:
                return False
        else:
            return False
    return etat == 1
 
 
def reconnaitre_affectation(aff):
    etat = 0
    for caractere in aff:
        if etat == 0:
            if caractere == "=":
                etat = 1
            else:
                return False
        else:
            return False
    return etat == 1
 
 
def reconnaitre_separateur(sep):
    etat = 0
    for caractere in sep:
        if etat == 0:
            if caractere in {"(", ")", ";"}:
                etat = 1
            else:
                return False
        else:
            return False
    return etat == 1
 
 
#  PARTIE 4 : analyseur lexical
 
# chaque automate est associe au nom de son token
CATEGORIES = [
    (reconnaitre_identificateur, "IDENTIFICATEUR"),
    (reconnaitre_nombre, "NOMBRE"),
    (reconnaitre_operateur, "OPERATEUR"),
    (reconnaitre_affectation, "AFFECTATION"),
    (reconnaitre_separateur, "SEPARATEUR"),
]
 
 
def categorie(lexeme):
    """Teste les automates un par un, retourne le nom du token."""
    for automate, nom in CATEGORIES:
        if automate(lexeme):
            return nom
    return "ERREUR LEXICALE"
 
 
def analyse(chaine):
    tokens = []          # liste de couples (token, lexeme)
    i = 0
    n = len(chaine)
    while i < n:
        c = chaine[i]
 
        # espaces, tabulations (et retours a la ligne) ignores
        if c in " \t\n":
            i += 1
 
        # bloc de lettres/chiffres colles = un seul lexeme
        elif c.isalnum():
            debut = i
            while i < n and chaine[i].isalnum():
                i += 1
            lexeme = chaine[debut:i]
            tokens.append((categorie(lexeme), lexeme))
 
        # tout autre caractere = un lexeme a lui seul
        else:
            tokens.append((categorie(c), c))
            i += 1
 
    return tokens
 
 
def afficher(tokens):
    print("Lexeme\tToken")
    for token, lexeme in tokens:
        print(lexeme, "\t", token)
#test 
print()
print("Tests identificateurs ")
for t in ["x", "nom", "var1", "somme25", "25var", "1abc", "_nom", "a b", "ab-c", "x1y2"]:
    print(f'"{t}"', reconnaitre_identificateur(t))
print()
print("Tests nombres")
for t in ["0", "12", "3456", "12a", "abc", "", "1 2", "-5", "3.5"]:
    print(f'"{t}"', reconnaitre_nombre(t))
print()
print("Operateur")
for t in [ "+","/","*-","25","sl25"]:
    print(f'"{t}"' ,reconnaitre_operateur(t))
print()
print("Affectation")
for t in ["=","oui","==","!"]:
    print(f'"{t}"' , reconnaitre_affectation(t))
print()
print("Separateur")
for t in [ ";","(",")",";;","x"]:
    print(f'"{t}"' , reconnaitre_separateur(t))
print()
print(" Analyse : exemple 1 ")
afficher(analyse("x = 25 + somme2;"))
print() 
print("Analyse : exemple 2 (erreur) ")
afficher(analyse("x = 25 + @;"))
print() 
print("Analyse : 25var ")
afficher(analyse("25var = 3;"))
print()
print("Analyse : entree libre ")
afficher(analyse("(a1 + 3) * b / 12 - c#;"))
