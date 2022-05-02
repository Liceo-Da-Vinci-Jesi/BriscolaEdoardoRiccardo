#Edoardo Zingaretti | Riccardo Flavianelli
#Briscola
import random, classMazzo, Tabellone, wx, Lobby, Risultati, Setting, finestraMazzi, classGiocataCPU
from PIL import Image
class Game:
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
        self.difficulty = True
        #random
        
        self.tabellone = Tabellone.Tabellone()
        self.tabellone.Hide()
        self.tabellone.U1.Bind(wx.EVT_BUTTON, self.GiocataUSER)
        self.tabellone.U2.Bind(wx.EVT_BUTTON, self.GiocataUSER)
        self.tabellone.U3.Bind(wx.EVT_BUTTON, self.GiocataUSER)
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
            res = self.tabellone.GetSize()
            self.tabellone.SetMinSize(res)
            self.tabellone.SetMaxSize(res)
        elif self.DIMENSIONE == "1300x1000":
            self.tabellone.SetMinSize((1300, 1000))
            self.tabellone.SetMaxSize((1300, 1000))
        elif self.DIMENSIONE == "1000x1000":
            self.tabellone.SetMinSize((1000,1000))
            self.tabellone.SetMaxSize((1000,1000))
        return
    def getColour(self,evt):
        colore = self.colore.GetStringSelection()
        self.COLORE = colore
        self.Setting.panel.SetBackgroundColour(self.COLORE)
        self.tabellone.panel.SetBackgroundColour(self.COLORE)
        self.Setting.Refresh()
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
                    self.tabellone.cartaUTENTE.SetLabel(str(cartaScelta[0]) + " " + cartaScelta[1])
                    self.user.remove(cartaScelta)
                    self.cUser = cartaScelta

        self.turno = False
        if self.GiocataCompleta():
            self.timerAttesa.StartOnce(1000)
            return
        self.timerCPU.StartOnce(1000)
        return

    def GiocataCPU(self, evt):
        #print(self.cpu)
        if not self.turno:
            cartaCPU = classGiocataCPU.Giocata(self.cpu, self.difficulty, self.briscolaSeme, self.cUser, self.vincitoreTurno).ScegliCarta()
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
                    self.tabellone.cartaCPU.SetLabel(str(cartaCPU[0]) + " " + cartaCPU[1])
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
            if len(self.mazzo) - 2 > 0:
                carteMazzo = len(self.mazzo) - 2
            else:
                carteMazzo = 0
            self.tabellone.carteMazzo.SetLabel(str(carteMazzo))
            self.tabellone.turnWinner.SetLabel("TAKES: " + vincitoreTurno)
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
        self.homeFinale = Risultati.Home(self.contaUSER, self.contaCPU, self.nome, self.COLORE)
        self.homeFinale.b2.Bind(wx.EVT_BUTTON, self.Restart)
        self.homeFinale.Show()
        return
    
    def PulisciCampo(self):
        self.tabellone.S1.SetLabel("")
        self.cCPU = ""
        self.tabellone.S2.SetLabel("")
        self.cUser = ""
        self.tabellone.Update()
        self.tabellone.Refresh()
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
    
    def Start(self, evt):                 #Gioco vero e proprio (inizia e lascia giocare)
        self.lobby.Destroy()
        self.startGame()
        self.tabellone.Show()
        if not self.turno:
            self.timerCPU.StartOnce(1000)
        return
    
    def Restart(self, evt):
        self.homeFinale.Destroy()
        self.__init__()
        return
#fix risoluzioni: fatto
#sfondo
#icone
#colorazioni
#descrizione turno: fatto
#fix nome (max 7 caratteri): fatto
#Restart: fatto
#giocataCPU in altro file: fatto
#fare che non si può aprire una nuova scheda 'taken' se una è già aperta
#aggiornare il file 'Risultati' inserendo che è lui che gestisce le 'taken'
#rivedere la funzione 'pescaCarta': può essere molto sintetizzata magari con un for e una lista

if __name__ == "__main__":
    app = wx.App()
    a = Game()
    app.MainLoop()