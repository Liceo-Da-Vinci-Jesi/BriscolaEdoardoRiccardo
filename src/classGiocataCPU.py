#classe che esegue la giocata del computer
import random
class Giocata:
    def __init__(self, mano, difficolta, briscola, cartaUtente, vincitoreTurno):
        self.difficolta = difficolta
        self.cpu = mano
        self.briscolaSeme = briscola
        self.cUser = cartaUtente
        self.importanza = [2,4,5,6,7,8,9,10,3,1]
        self.vincitoreTurno = vincitoreTurno
        return
    
    def Gioca(self):
        if self.difficolta:
            cartaCPU = random.choice(self.cpu)
        else:
            cartaCPU = self.ScegliCarta()
        return cartaCPU
    
    def ScegliCarta(self):
        self.semiCPU = []
        for x in self.cpu:
            self.semiCPU.append(x[1])
        if self.vincitoreTurno == "":
            cartaCPU = self.GiocataLOW()
        elif self.vincitoreTurno == "CPU":
            cartaCPU = self.GiocataLOW()
        else:
            #Ha giocato l'utente
            #Se gioca briscola
            if self.cUser[1] == self.briscolaSeme:
                print("a")
                #Se la CPU non ha briscola gioca + basso poss
                if self.briscolaSeme not in self.semiCPU:
                    cartaCPU = self.GiocataLOW()
                    print("b")
                #Se invece la ha 
                else:
                    #e se è > di un 9 prova a prenderla, altrimenti gioca + basso poss
                    if self.importanza.index(self.cUser[0]) > 5:
                        carteMaggiori = []
                        for carta in self.cpu:
                            if carta[1] == self.briscolaSeme and self.importanza.index(carta[0]) > self.importanza.index(self.cUser[0]):
                                carteMaggiori.append(carta)
                        #se non può prendere, gioca la carta con MENO punti possibili (anche se fosse briscola)
                        if len(carteMaggiori) == 0:
                            cartaCPU = self.GiocataLOW()
                            if cartaCPU[1] != self.briscolaSeme:
                                for carta in self.cpu:
                                    if self.importanza.index(cartaCPU[0]) > self.importanza.index(carta[0]) and self.importanza.index(carta[0]) < 6:
                                        cartaCPU = carta
                            print("c")
                        else:
                            lista = []
                            for carta in carteMaggiori:
                                lista.append(self.importanza.index(carta[0]))
                            x = max(lista)
                            cartaCPU = [self.importanza[x], self.briscolaSeme]
                            print("d")
                    else:
                        cartaCPU = self.GiocataLOW()
                        print("e")
            elif self.importanza.index(self.cUser[0]) > 6 and self.briscolaSeme in self.semiCPU:
                briscole = []
                for carta in self.cpu:
                    if carta[1] == self.briscolaSeme:
                        briscole.append(self.importanza.index(carta[0]))
                if len(briscole) > 0:
                    x = max(briscole)
                    cartaCPU = [self.importanza[x], self.briscolaSeme]
                    print("f")
                else:
                    cartaCPU = self.GiocataLOW()
                    print("g")
            #se l'user gioca una carta e la cpu ha il suo stesso seme e vale di più la prende
            elif self.cUser[1] in self.semiCPU:
                lista = []
                for carta in self.cpu:
                        if carta[1] == self.cUser[1]:
                            if self.importanza.index(carta[0]) > self.importanza.index(self.cUser[0]):
                                lista.append(carta)
                #se la CPU non può prendere la carta dell'utente, gioca il + basso poss
                if len(lista) == 0:
                    cartaCPU = self.GiocataLOW()
                    print("h")
                else:
                    maggiori = []
                    for carta in lista:
                        maggiori.append(self.importanza.index(carta[0]))
                    x = min(maggiori)
                    cartaCPU = [self.importanza[x], self.cUser[1]]
                    print("i")
            else:
                cartaCPU = self.GiocataLOW()
                print("l")
        return cartaCPU
        
    def GiocataLOW(self):
        if self.semiCPU.count(self.briscolaSeme) != len(self.cpu):
            for c in self.importanza:
                for x in self.cpu:
                    if x[1]!=self.briscolaSeme and x[0]==c:
                        return x
        else:
            numeri = []
            for x in self.cpu:
                numeri.append(x[0])
            if 1 in numeri and len(numeri) != 1:
                numeri.remove(1)
            if 3 in numeri and len(numeri) != 1:
                numeri.remove(3)
            x = min(numeri)
            return [x, self.briscolaSeme]
        
if __name__ == "__main__":
    #manoCPU, difficoltà, seme briscola, carta utente e vincitoreTurno
    #Prova
    classe = Giocata([[1, "Denari"],[3, "Coppe"],[10,"Bastoni"]], False, "Bastoni", [10, "Bastoni"], "UTENTE")
    print(classe.Gioca())