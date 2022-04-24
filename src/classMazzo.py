import random
class Mazzo:
    def __init__(self):
        self.mazzo = self.generaMazzo()
        return
    
    def generaMazzo(self):
        mazzo = []
        numeri = []
        for n in range(1,11):
            numeri.append(n)
        semi = ("Bastoni", "Coppe", "Denari", "Spadi")
        for seme in semi:
            for numero in numeri:
                #False indica se la carta è coperta (False) o se scoperta (True)
                mazzo.append([numero, seme]) 
        #random.shuffle(mazzo)
        return mazzo
    
    
if __name__ == "__main__":
    a = Mazzo()
    print(a.mazzo)