#Edoardo Zingaretti | Riccardo Flavianelli
#Briscola
import random, classMazzo, Tabellone, wx, Lobby, Risultati, Setting, finestraMazzi
from PIL import Image
class Game():
    def __init__(self):
        self.mazzo = classMazzo.Mazzo().mazzo
        random.shuffle(self.mazzo)
        self.countTurno = 0
        self.timerCPU = wx.Timer()
        self.timerCPU.Bind(wx.EVT_TIMER, self.GiocataCPU)
        
        self.timerAttesa = wx.Timer()
        self.timerAttesa.Bind(wx.EVT_TIMER, self.fineTurno)
        
        #Mani
        self.user = []
        self.cpu = []
        
        self.vincitoreTurno = ""
        #Carte
        self.cUser = ""
        self.cCPU = ""
        
        #Mazzi
        self.contaUSER = []
        self.contaCPU = []
        self.Punti = [0, 11, 0, 10, 0, 0, 0, 0, 2, 3, 4]
        self.importanza = [2,4,5,6,7,8,9,10,3,1]
        
        self.CONTA = 0
        self.turno = random.choice((True, False))
        print(self.turno)
        self.briscolaCarta = self.choiceBriscola()
        self.briscolaSeme = self.briscolaCarta[1]
        self.lobby = Lobby.Home()
        self.lobby.Show()
        self.lobby.nome.Bind(wx.EVT_TEXT_ENTER, self.Start)
        
        self.Setting = Setting.SETTING()
        self.Setting.Bind(wx.EVT_CLOSE, self.backLobby)
        self.Setting.Hide()
        self.COLORE = self.Setting.COLORE
        self.colore = self.Setting.colore
        self.colore.Bind(wx.EVT_COMBOBOX, self.getColour)
        self.Setting.tornaIndietro.Bind(wx.EVT_BUTTON, self.backLobby)
        self.DIMENSIONE = self.Setting.DIMENSIONE
        self.dimensione = self.Setting.dimensione
        self.Setting.dimensione.Bind(wx.EVT_COMBOBOX, self.getRes)
        self.lobby.b1.Bind(wx.EVT_BUTTON, self.openSetting)
        self.lobby.b2.Bind(wx.EVT_BUTTON, self.Start)
        self.Setting.random.Bind(wx.EVT_RADIOBUTTON, self.getDifficulty)
        self.Setting.normal.Bind(wx.EVT_RADIOBUTTON, self.getDifficulty)
        self.difficulty = True #random
        
        self.tabellone = Tabellone.Tabellone()
        self.tabellone.Hide()
        self.tabellone.U1.Bind(wx.EVT_BUTTON, self.GiocataUSER)
        self.tabellone.U2.Bind(wx.EVT_BUTTON, self.GiocataUSER)
        self.tabellone.U3.Bind(wx.EVT_BUTTON, self.GiocataUSER)
        
        self.homeFinale = Risultati.Home()
        self.homeFinale.Hide()
        self.contaBarra = 0
        self.barra = self.homeFinale.barra
        self.timerBarra = wx.Timer()
        self.timerBarra.Bind(wx.EVT_TIMER, self.OnTimer)
        self.checkGauge = True
        return
    
    def openSetting(self, evt):
        self.lobby.Enable(False)
        self.Setting.Show()
        return
    def getRes(self, evt):
        dim = self.dimensione.GetStringSelection()
        self.DIMENSIONE = dim
        if self.DIMENSIONE == "FULLSCREEN":
            self.tabellone.Maximize()
        elif self.DIMENSIONE == "1200x950":
            self.tabellone.SetSize((1200, 950))
        elif self.DIMENSIONE == "950x950":
            self.tabellone.SetSize((950,950))
        return
    def getColour(self,evt):
        colore = self.colore.GetStringSelection()
        self.COLORE = colore
        self.lobby.panel.SetBackgroundColour(self.COLORE)
        self.Setting.panel.SetBackgroundColour(self.COLORE)
        self.tabellone.panel.SetBackgroundColour(self.COLORE)
        self.homeFinale.panel.SetBackgroundColour(self.COLORE)
        self.Setting.Refresh()
        self.lobby.Refresh()
        self.homeFinale.Refresh()
        return
    def getDifficulty(self, evt):
        self.lobby.Enable(True)
        if self.Setting.random.GetValue():
            self.difficulty = True
            self.lobby.st2.SetLabel("DIFFICULTY SELECTED: RANDOM")
        else:
            self.difficulty = False
            self.lobby.st2.SetLabel("DIFFICULTY SELECTED: HARD")
        self.lobby.Enable(False)
        return
    def backLobby(self, evt):
        self.Setting.Hide()
        self.lobby.Enable(True)
        self.lobby.Raise()
        return

    def startGame(self):
        self.nome = self.lobby.nome.GetValue()
        while len(self.user) != 3:
            if self.turno:
                carta = self.mazzo.pop()
                self.user.append(carta)
                carta = self.mazzo.pop()
                self.cpu.append(carta)
            else:
                carta = self.mazzo.pop() 
                self.cpu.append(carta)
                carta = self.mazzo.pop()
                self.user.append(carta)  
        
        #Imposto la mano della CPU
        self.tabellone.C1.SetLabel(str(self.cpu[0][0]) + self.cpu[0][1])
        self.tabellone.C2.SetLabel(str(self.cpu[1][0]) + self.cpu[1][1])
        self.tabellone.C3.SetLabel(str(self.cpu[2][0]) + self.cpu[2][1])
        
        #Imposto la Briscola e il self.mazzo nel tabellone
        self.tabellone.S4.SetLabel(str(self.briscolaCarta[0]) + self.briscolaCarta[1])
        img = Image.open("../carte/" + str(self.briscolaCarta[1]) + str(self.briscolaCarta[0]) + ".jpg")
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img2.size[0], img2.size[1])
        wx_Image.SetData(img2.convert("RGB").tobytes())
        self.bitmapBriscola = wx.Bitmap(wx_Image)
        self.tabellone.S4.Bitmap = self.bitmapBriscola
        
        #Imposto la mano dell'User
        #Carta 1
        self.tabellone.U1.SetLabel(str(self.user[0][0]) + self.user[0][1])
        img = Image.open("../carte/" + self.user[0][1] + str(self.user[0][0]) + ".jpg")
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img2.size[0], img2.size[1])
        wx_Image.SetData(img2.convert("RGB").tobytes())
        self.tabellone.U1.Bitmap = wx.Bitmap(wx_Image)
        
        #Carta 2
        self.tabellone.U2.SetLabel(str(self.user[1][0]) + self.user[1][1])
        img = Image.open("../carte/" + self.user[1][1] + str(self.user[1][0]) + ".jpg")
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img2.size[0], img2.size[1])
        wx_Image.SetData(img2.convert("RGB").tobytes())
        self.tabellone.U2.Bitmap = wx.Bitmap(wx_Image)
        
        #Carta 3
        self.tabellone.U3.SetLabel(str(self.user[2][0]) + self.user[2][1])
        img = Image.open("../carte/" + self.user[2][1] + str(self.user[2][0]) + ".jpg")
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img2.size[0], img2.size[1])
        wx_Image.SetData(img2.convert("RGB").tobytes())
        self.tabellone.U3.Bitmap = wx.Bitmap(wx_Image)
        
        #carta coperta (mano CPU)
        img = Image.open(self.Setting.BackType[self.Setting.retro])
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img2.size[0], img2.size[1])
        wx_Image.SetData(img2.convert("RGB").tobytes())
        self.retro = wx.Bitmap(wx_Image)
        
        self.tabellone.C1.Bitmap = self.retro
        self.tabellone.C2.Bitmap = self.retro
        self.tabellone.C3.Bitmap = self.retro
        self.tabellone.S5.Bitmap = self.retro
        return
    
    def choiceBriscola(self):
        briscola = self.mazzo.pop()
        return briscola
    
    def GiocataUSER(self, evt):
        if self.turno:
            puls = (self.tabellone.U1, self.tabellone.U2, self.tabellone.U3)
            cartaClickata = puls[evt.GetId() - 4].GetLabel()
            for n in puls:
                if n.GetLabel() == cartaClickata:
                    for i in self.user:
                        if n.GetLabel() == (str(i[0]) + i[1]):
                            cartaScelta = i
                    
                    self.tabellone.S2.SetLabel(cartaClickata)
                    self.tabellone.S2.Show()
                    self.tabellone.S2.Bitmap = n.Bitmap
                    
                    n.SetLabel("")
                    n.Hide()
                    self.user.remove(cartaScelta)
                    self.cUser = cartaScelta

        self.turno = False
        if self.GiocataCompleta():
            self.timerAttesa.StartOnce(1000)
            return
        self.timerCPU.StartOnce(1000)
        return
    
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
    def GiocataCPU(self, evt):
        #print(self.cpu)
        if not self.turno:
            if self.difficulty:
                cartaCPU = random.choice(self.cpu)
            else:
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
                        #print("a")
                        #Se la CPU non ha briscola gioca + basso poss
                        if self.briscolaSeme not in self.semiCPU:
                            cartaCPU = self.GiocataLOW()
                            #print("b")
                        #Se invece la ha 
                        else:
                            #e se è > di un 9 prova a prenderla, altrimenti gioca + basso poss
                            if self.importanza.index(self.cUser[0]) > 5:
                                carteMaggiori = []
                                for carta in self.cpu:
                                    if carta[1] == self.briscolaSeme and self.importanza.index(carta[0]) > self.importanza.index(self.cUser[0]):
                                        carteMaggiori.append(carta)
                                if len(carteMaggiori) == 0:
                                    cartaCPU = self.GiocataLOW()
                                    #print("c")
                                else:
                                    lista = []
                                    for carta in carteMaggiori:
                                        lista.append(self.importanza.index(carta[0]))
                                    x = max(lista)
                                    cartaCPU = [self.importanza[x], self.briscolaSeme]
                                    #print("d")
                            else:
                                cartaCPU = self.GiocataLOW()
                                #print("e")
                    elif self.importanza.index(self.cUser[0]) > 6 and self.briscolaSeme in self.semiCPU:
                        briscole = []
                        for carta in self.cpu:
                            if carta[1] == self.briscolaSeme:
                                briscole.append(self.importanza.index(carta[0]))
                        if len(briscole) > 0:
                            x = max(briscole)
                            cartaCPU = [self.importanza[x], self.briscolaSeme]
                            #print("f")
                        else:
                            cartaCPU = self.GiocataLOW()
                            #print("g")
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
                            #print("h")
                        else:
                            maggiori = []
                            for carta in lista:
                                maggiori.append(self.importanza.index(carta[0]))
                            x = min(maggiori)
                            cartaCPU = [self.importanza[x], self.cUser[1]]
                            #print("i")
                    else:
                        cartaCPU = self.GiocataLOW()
                        #print("l")
            if self.cCPU == cartaCPU:
                cartaCPU = random.choice(self.cpu)
            for n in (self.tabellone.C1, self.tabellone.C2, self.tabellone.C3):
                label = str(cartaCPU[0]) + cartaCPU[1]
                if n.GetLabel() == label:
                    self.turno = True
                    self.tabellone.S1.SetLabel(str(cartaCPU[0]) + cartaCPU[1])
                    
                    img = Image.open("../carte/" + cartaCPU[1] + str(cartaCPU[0]) + ".jpg")
                    img = img.resize((150,250))
                    img2 = img.copy()
                    wx_Image = wx.Image(img2.size[0], img2.size[1])
                    wx_Image.SetData(img2.convert("RGB").tobytes())
                    self.tabellone.S1.Show()
                    self.tabellone.S1.Bitmap = wx.Bitmap(wx_Image)
                    
                    n.SetLabel("")
                    n.Hide()
                    self.cpu.remove(cartaCPU)
                    self.cCPU = cartaCPU
        if self.GiocataCompleta():
            self.timerAttesa.StartOnce(1000)
            return
        return
   
    def GiocataCompleta(self):
        if self.tabellone.S1.GetLabel() != "" and self.tabellone.S2.GetLabel() != "":
            self.countTurno += 1
            return True
        return False
    
    def fineTurno(self, evt):
        if self.countTurno != 0:
            vincitoreTurno = self.Played(self.cUser,self.cCPU)
            if vincitoreTurno == self.nome:
                self.contaUSER.append([self.cUser[0], self.cUser[1]])
                self.contaUSER.append([self.cCPU[0], self.cCPU[1]])
                self.tabellone.Count2.SetLabel(str((int(self.tabellone.Count2.GetLabel()) + 2)))
            else:
                self.contaCPU.append([self.cCPU[0], self.cCPU[1]])
                self.contaCPU.append([self.cUser[0], self.cUser[1]])
                self.tabellone.Count1.SetLabel(str((int(self.tabellone.Count1.GetLabel()) + 2)))
            self.tabellone.turnWinner.SetLabel("Prende: " + vincitoreTurno)
            self.PulisciCampo()
            self.pescaCarta()
            self.tabellone.S1.Hide()
            self.tabellone.S2.Hide()
            if self.vincitoreTurno != self.nome and self.CONTA < 4:
                self.timerCPU.StartOnce(1000)
        return
    
    def pescaCarta(self):
        if len(self.mazzo) > 1:
            if self.vincitoreTurno == self.nome:
                carta = self.mazzo.pop()
                self.user.append(carta)
                for u in (self.tabellone.U1, self.tabellone.U2, self.tabellone.U3):
                    if u.GetLabel() == "":
                        u.SetLabel(str(carta[0]) + carta[1])
                        cartaU = u
                carta2 = self.mazzo.pop()
                self.cpu.append(carta2)
                for c in (self.tabellone.C1, self.tabellone.C2, self.tabellone.C3):
                    if c.GetLabel() == "":
                        c.SetLabel(str(carta2[0]) + carta2[1])
                        cartaC = c
            else:
                carta2 = self.mazzo.pop()
                self.cpu.append(carta2)
                for c in (self.tabellone.C1, self.tabellone.C2, self.tabellone.C3):
                    if c.GetLabel() == "":
                        c.SetLabel(str(carta2[0]) + carta2[1])
                        cartaC = c
                carta = self.mazzo.pop()
                self.user.append(carta)
                for u in (self.tabellone.U1, self.tabellone.U2, self.tabellone.U3):
                    if u.GetLabel() == "":
                        u.SetLabel(str(carta[0]) + carta[1])
                        cartaU = u
                        
            #carta pescata dall'utente
            img = Image.open("../carte/" + carta[1] + str(carta[0]) + ".jpg")
            img = img.resize((150,250))
            img2 = img.copy()
            wx_Image = wx.Image(img2.size[0], img2.size[1])
            wx_Image.SetData(img2.convert("RGB").tobytes())
            cartaU.Show()
            cartaU.Bitmap = wx.Bitmap(wx_Image)
            
            #carta pescata dalla cpu
            cartaC.Show()
            cartaC.Bitmap = self.retro
        else:
            self.CONTA += 1
            if self.CONTA == 4:
                self.Results()
                return
            if self.CONTA == 1:
                if self.vincitoreTurno == self.nome:
                    carta = self.mazzo.pop()
                    self.user.append(carta)
                    for u in (self.tabellone.U1, self.tabellone.U2, self.tabellone.U3):
                        if u.GetLabel() == "":
                            u.SetLabel(str(carta[0]) + carta[1])
                            cartaU = u
                    carta2 = self.briscolaCarta
                    self.cpu.append(carta2)
                    for c in (self.tabellone.C1, self.tabellone.C2, self.tabellone.C3):
                        if c.GetLabel() == "":
                            c.SetLabel(str(carta2[0]) + carta2[1])
                            cartaC = c
                else:
                    carta2 = self.mazzo.pop()
                    self.cpu.append(carta2)
                    for c in (self.tabellone.C1, self.tabellone.C2, self.tabellone.C3):
                        if c.GetLabel() == "":
                            c.SetLabel(str(carta2[0]) + carta2[1])
                            cartaC = c
                    carta = self.briscolaCarta
                    self.user.append(carta)
                    for u in (self.tabellone.U1, self.tabellone.U2, self.tabellone.U3):
                        if u.GetLabel() == "":
                            u.SetLabel(str(carta[0]) + carta[1])
                            cartaU = u
                            
                self.tabellone.S4.Hide()
                self.tabellone.S5.Hide()

                #carta pescata dall'utente
                cartaU.Show()
                cartaU.Bitmap = self.bitmapBriscola
                
                #carta pescata dalla cpu
                cartaC.Show()
                cartaC.Bitmap = self.retro
        return
    
    def Results(self):
        self.tabellone.Hide()
        self.homeFinale.Show()
        self.timerBarra.Start(1)
        return
    def OnTimer(self, event):
        if self.checkGauge:
            self.contaBarra += 1
            self.barra.SetValue(self.contaBarra)
            if self.barra.GetValue() == (self.barra.GetRange() + 50):
                self.barra.Destroy()
                self.checkGauge = False
        else:
            self.timerBarra.Stop()
            puntiUtente = self.contaPunti(self.contaUSER)
            puntiCpu = self.contaPunti(self.contaCPU)
            if puntiUtente > puntiCpu:
                self.homeFinale.winner.SetLabel("Congratulations! You are the winner!")
            elif puntiUtente < puntiCpu:
                self.homeFinale.winner.SetLabel("CPU is the winner! Try again ;)")
            else:
                self.homeFinale.winner.SetLabel("None has won...")
            self.homeFinale.risultati.SetLabel("Punti CPU: " + str(puntiCpu) + "\nI tuoi Punti" + ": " + str(puntiUtente))
            self.homeFinale.b1.Bind(wx.EVT_BUTTON, self.openMazzi)
        return
    
    def openMazzi(self, evt):
        finestra = finestraMazzi.Home(self.contaUSER, self.contaCPU, self.nome)
        finestra.Show()
        return
    
    def PulisciCampo(self):
        self.tabellone.S1.SetLabel("")
        self.cCPU = ""
        self.tabellone.S2.SetLabel("")
        self.cUser = ""
        return
    
    def Played(self,cartaUser,cartaCPU):  
        #Controllo chi ha vinto (il turno)
        if cartaUser[1] == cartaCPU[1]:
            if cartaUser[0] == 1:
                self.vincitoreTurno = self.nome
                self.turno = True
                return self.vincitoreTurno
            elif cartaUser[0] == 3 and cartaCPU[0] != 1:
                self.vincitoreTurno = self.nome
                self.turno = True
                return self.vincitoreTurno
            elif cartaCPU[0] == 1:
                self.vincitoreTurno = "CPU"
                self.turno = False
                return self.vincitoreTurno
            elif cartaCPU[0] == 3 and cartaUser[0] != 1:
                self.vincitoreTurno = "CPU"
                self.turno = False
                return self.vincitoreTurno
            
            if cartaUser[0] > cartaCPU[0]:
                self.vincitoreTurno = self.nome
                self.turno = True
            else:
                self.vincitoreTurno = "CPU"
                self.turno = False
            return self.vincitoreTurno
        
        if cartaUser[1] == self.briscolaSeme:
            self.vincitoreTurno = self.nome
            self.turno = True
            return self.vincitoreTurno
        
        if cartaCPU[1] == self.briscolaSeme:
            self.vincitoreTurno = "CPU"
            self.turno = False
            return self.vincitoreTurno
    
        if self.turno:
            self.vincitoreTurno = self.nome
            return self.vincitoreTurno
        else:
            self.vincitoreTurno = "CPU"
            return self.vincitoreTurno
        
    def contaPunti(self, l):
        lista = l
        somma = 0
        for n in lista:
            somma += self.Punti[n[0]]
        return somma
    
    def Start(self, evt):                 #Gioco vero e proprio (inizia e lascia giocare)
        self.lobby.Destroy()
        self.startGame()
        self.tabellone.Show()
        if not self.turno:
            self.timerCPU.StartOnce(1000)
        return
    
#fix risoluzioni
#sfondo
#icone
#colorazioni
#descrizione turno 
if __name__ == "__main__":
    app = wx.App()
    a = Game()
    app.MainLoop()