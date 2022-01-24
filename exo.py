
def entryTime(s,keypad):
    if len(s)>10**5:
        print("Le string s est trop long. Veuillez réesayer avec une autre valeur. ")
        return
    if len(keypad)!=9:
        print("Le string keypad n'a pas la bonne longueur. Veuillez réesayer avec un nombre de longueur 9. ")
        return
    somme=0
    for i in range(9):        
        chiffre=int(keypad[i])
        somme+=chiffre
    if somme!=45: #45 est la somme des chiffres de 1 à 9 
        print("Le string keypad est invalide, tous les chiffres de 1 à 9 ne sont pas représentés ") 
        return
    totaltime=0 #initialisation
    for i in range (len(s)-1):
        key=s[i]
        nextkey=s[i+1]
        positioninitiale=keypad.index(key) #retourne l'index donc la position du chiffre désiré
        positionarrivee=keypad.index(nextkey)
        time=calculateFromPosition(positioninitiale,positionarrivee)
        totaltime+=calculateFromPosition(positioninitiale,positionarrivee)
    print("Le temps total minimum pour écrire ce string est de " + str(totaltime))

def max_diff(int_array):
    return
        
        

def calculateFromPosition(positioninitiale,positionarrivee): #fonction pour calculer le temps d'une case a une autre
    time=0
    match positioninitiale:
        case 0: #haut gauche
            listtime= [0,1,2,1,1,2,2,2,2]
            time=listtime[positionarrivee]
            return time
        case 1:#haut milieu
            listtime= [1,0,1,1,1,1,2,2,2]
            time=listtime[positionarrivee]  
            return time
        case 2: #haut droite
            listtime= [2,1,0,2,1,1,2,2,2] 
            time=listtime[positionarrivee]
            return time
        case 3:#milieu gauche
            listtime= [1,1,2,0,1,2,1,1,2]
            time=listtime[positionarrivee]
            return time
        case 4: #case centrale
            listtime= [1,1,1,1,0,1,1,1,1]
            time=listtime[positionarrivee]
            return time
        case 5: #milieu droite
            listtime= [2,1,1,2,1,0,2,1,1]
            time=listtime[positionarrivee]
            return time
        case 6: #bas gauche
            listtime= [2,2,2,1,1,2,0,1,2]
            time=listtime[positionarrivee]
            return time
        case 7: #bas milieu
            listtime= [2,2,2,1,1,1,1,0,1]
            time=listtime[positionarrivee]
            return time
        case 8: #bas droite
            listtime= [2,2,2,2,1,1,2,1,0]
            time=listtime[positionarrivee]
            return time

        case _: return #default case

if __name__ == '__main__':
    s=input("Quelle valeur pour s ? Des chiffres de 1 à 9 seulement \n")
    keypad=input("Quelle valeur pour keypad ? (longueur 9, chiffres de 1 à 9 avec une seule occurence) \n")
    entryTime(s,keypad)

