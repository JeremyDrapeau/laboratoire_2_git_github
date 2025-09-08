# Demande un message a l'utilisateur
def askMsg() -> str : 
    temp = input("Quel est le message a afficher? (q pour quitter) : ")
    return temp

# Demande un chiffre a l'utilisatseur oui oui
def askNum() -> int :
    temp = ""
    while not temp.isnumeric() :
        temp = input("Combien de fois voullez-vous l\'afficher")
    return int(temp)