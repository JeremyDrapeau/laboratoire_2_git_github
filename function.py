# Demande un message a l'utilisateur
def askMsg() -> str : 
    temp = input("Quel est le message a afficher? : ")
    return temp

# Demande un chiffre a l'utilisateur
def askNum() -> int :
    temp : int = int(input("Combien de fois voullez-vous l\'afficher"))
    return temp