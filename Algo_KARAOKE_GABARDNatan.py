from ast import Return

class Joueur:
    def __init__(self,Nom,Song0,Song1,Song2,Song3,Song4):
        self.__Name=Nom
        self.__Song0=Song0
        self.__Song1=Song1
        self.__Song2=Song2
        self.__Song3=Song3
        self.__Song4=Song4

    def getTotalScore(self):
        T = self.__Song0 + self.__Song1 + self.__Song2 + self.__Song3 + self.__Song4
        print(self.__Name,"possède",T,"points")
    
    def getBestScore(self):
        M = self.__Song0
        N = 0
        for i in range (4) :
            C = self.__Song+i
            if M < C :
                M = C
                N = i
        print ("ton meilleur score est sur la musique n°",N)

    def getLastScore(self):
        M = self.__Song0
        N = 0
        for i in range (4) :
            C = "self.__Song"+i
            if M > C :
                M = C
                N = i
        print ("ton pire score est sur la musique n°",N)
        
    def getAfficheScore(self):
        print("ton score sur la musique 1:", self.__Song0,"2:", self.__Song1,"3:", self.__Song2,"4:", self.__Song3,"5:", self.__Song4,)

    def getAjouteScore(self):
        M = int(input("quel musique as tu fait ?"))
        S = int(input("Quel nouveau score as tu fait ?"))
        if M == 1 :
            self.__Song0 = S
        elif M == 2 :
            self.__Song1 = S
        elif M == 3 :
            self.__Song2 = S
        elif M == 4 :
            self.__Song3 = S
        elif M == 5 :
            self.__Song4 = S
        
nom = input("quel est ton prénom ?")

Joueur1 = Joueur(nom,0,0,0,0,0)



fin = False

while fin != True :
    R = int(input("que voulez vous faire ?        Ajouter Score : 1       Afficher Score : 2       Afficher le total : 3  \n"))
    if R == 1 :
        Joueur1.getAjouteScore()
    elif R == 2 :
        Joueur1.getAfficheScore()
    elif R == 3 :
        Joueur1.getTotalScore()