import random
class Mazzo:
    def __init__(self):
        self.mazzo = []
        return
    
    def generaMazzo(self):
        numeri = []
        for n in range(1,11):
            numeri.append(n)
        semi = ("Bastoni", "Coppe", "Denari", "Spadi")
        for seme in semi:
            for numero in numeri:
                self.mazzo.append([numero, seme]) 
        random.shuffle(self.mazzo)
        return self.mazzo
    
if __name__ == "__main__":
    a = Mazzo()
    print(a.generaMazzo())