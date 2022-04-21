#Edoardo Zingaretti | Riccardo Flavianelli
#Briscola
import random, classMazzo, Tabellone, wx, Lobby, Risultati, time, Setting, webbrowser
from PIL import Image

mazzo = classMazzo.Mazzo().mazzo
class Game():
    def __init__(self):
        random.shuffle(mazzo)
        #Mani
        self.user = []
        self.cpu = []
        self.vincitoreTurno = ""
        self.cUser = ""
        self.cCPU = ""
        self.contaUSER = []
        self.contaCPU = []
        self.CONTA = 0
        self.turno = random.choice((True, False))
        print(self.turno)
        self.briscolaCarta = self.choiceBriscola()
        self.briscolaSeme = self.briscolaCarta[1]
        
        self.lobby = Lobby.Home()
        self.lobby.Show()
        
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
        self.lobby.b3.Bind(wx.EVT_BUTTON, self.openBrowser)
        
        self.tabellone = Tabellone.Tabellone()
        self.tabellone.Hide()
        self.tabellone.U1.Bind(wx.EVT_BUTTON, self.GiocataUSER)
        self.tabellone.U2.Bind(wx.EVT_BUTTON, self.GiocataUSER)
        self.tabellone.U3.Bind(wx.EVT_BUTTON, self.GiocataUSER)
        
        self.homeFinale = Risultati.Home()
        self.homeFinale.Hide()
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
        elif self.DIMENSIONE == "1200x780":
            self.tabellone.SetSize((1200, 780))
        elif self.DIMENSIONE == "960x540":
            self.tabellone.SetSize((960,540))
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
    def openBrowser(self, evt):
        webbrowser.open("https://en.wikipedia.org/wiki/Briscola")
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
                carta = mazzo.pop()
                carta[2] = True
                self.user.append(carta)
                carta = mazzo.pop()
                self.cpu.append(carta)
            else:
                carta = mazzo.pop() 
                self.cpu.append(carta)
                carta = mazzo.pop()
                carta[2] = True
                self.user.append(carta)  
        
        #Imposto la mano della CPU
        self.tabellone.C1.SetLabel(str(self.cpu[0][0]) + self.cpu[0][1])
        self.tabellone.C2.SetLabel(str(self.cpu[1][0]) + self.cpu[1][1])
        self.tabellone.C3.SetLabel(str(self.cpu[2][0]) + self.cpu[2][1])
        
        #Imposto la Briscola e il mazzo nel tabellone
        self.tabellone.S4.SetLabel(str(self.briscolaCarta[0]) + self.briscolaCarta[1])
        img = Image.open("carte/" + str(self.briscolaCarta[1]) + str(self.briscolaCarta[0]) + ".jpg")
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img2.size[0], img2.size[1])
        wx_Image.SetData(img2.convert("RGB").tobytes())
        self.tabellone.S4.Bitmap = wx.Bitmap(wx_Image)
        
        #Imposto la mano dell'User
        #Carta 1
        self.tabellone.U1.SetLabel(str(self.user[0][0]) + self.user[0][1])
        img = Image.open("carte/" + self.user[0][1] + str(self.user[0][0]) + ".jpg")
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img2.size[0], img2.size[1])
        wx_Image.SetData(img2.convert("RGB").tobytes())
        self.tabellone.U1.Bitmap = wx.Bitmap(wx_Image)
        
        #Carta 2
        self.tabellone.U2.SetLabel(str(self.user[1][0]) + self.user[1][1])
        img = Image.open("carte/" + self.user[1][1] + str(self.user[1][0]) + ".jpg")
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img2.size[0], img2.size[1])
        wx_Image.SetData(img2.convert("RGB").tobytes())
        self.tabellone.U2.Bitmap = wx.Bitmap(wx_Image)
        
        #Carta 3
        self.tabellone.U3.SetLabel(str(self.user[2][0]) + self.user[2][1])
        img = Image.open("carte/" + self.user[2][1] + str(self.user[2][0]) + ".jpg")
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img2.size[0], img2.size[1])
        wx_Image.SetData(img2.convert("RGB").tobytes())
        self.tabellone.U3.Bitmap = wx.Bitmap(wx_Image)
        
        self.tabellone.Refresh()
        
        #carta coperta (mano CPU)
        img = Image.open("carte/Retro2.jpg")
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img2.size[0], img2.size[1])
        wx_Image.SetData(img2.convert("RGB").tobytes())
        self.retro = wx.Bitmap(wx_Image)
        return
    
    def choiceBriscola(self):
        briscola = mazzo.pop()
        briscola[2] = True
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
            self.fineTurno()
            return
        self.GiocataCPU()
        return 
    
    def GiocataCPU(self):
        if not self.turno:
            cartaCPU = random.choice(self.cpu)
            for n in (self.tabellone.C1, self.tabellone.C2, self.tabellone.C3):
                if n.GetLabel() == (str(cartaCPU[0]) + cartaCPU[1]):
                    self.turno = True
                    self.tabellone.S1.SetLabel(str(cartaCPU[0]) + cartaCPU[1])
                    
                    img = Image.open("carte/" + cartaCPU[1] + str(cartaCPU[0]) + ".jpg")
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
        cartaCPU[2] = True
        if not self.GiocataCompleta():
            return
        self.fineTurno()
        return
   
    def GiocataCompleta(self):
        if self.tabellone.S1.GetLabel() != "" and self.tabellone.S2.GetLabel() != "":
            return True
        return False
    
    def fineTurno(self):
        print(len(mazzo))
        vincitoreTurno = self.Played(self.cUser,self.cCPU)
        self.tabellone.S3.SetLabel("DESCRIZIONE TURNO: \nCarta CPU: " + str(self.cCPU[0]) + " " + self.cCPU[1] + "\nCarta User: " + str(self.cUser[0]) + " " + self.cUser[1] + "\nVincitore Turno: " + vincitoreTurno + "\nCarte Mazzo: " + str(len(mazzo)))
        if vincitoreTurno == self.nome:
            self.contaUSER.append(self.cUser[0])
            self.contaUSER.append(self.cCPU[0])
        else:
            self.contaCPU.append(self.cCPU[0])
            self.contaCPU.append(self.cUser[0])
        self.tabellone.S5.SetLabel("MAZZO\nCarte Rimanenti: " + str(len(mazzo)))
        self.PulisciCampo()
        self.pescaCarta()
        time.sleep(1)
        self.tabellone.S1.Hide()
        self.tabellone.S2.Hide()
        if self.vincitoreTurno != self.nome:
            self.GiocataCPU()
        return
    
    def pescaCarta(self):
        if len(mazzo) > 1:
            if self.turno:
                carta = mazzo.pop()
                self.user.append(carta)
                for u in (self.tabellone.U1, self.tabellone.U2, self.tabellone.U3):
                    if u.GetLabel() == "":
                        u.SetLabel(str(carta[0]) + carta[1])
                        cartaU = u
                carta2 = mazzo.pop()
                self.cpu.append(carta2)
                for c in (self.tabellone.C1, self.tabellone.C2, self.tabellone.C3):
                    if c.GetLabel() == "":
                        c.SetLabel(str(carta2[0]) + carta2[1])
                        cartaC = c
            else:
                carta2 = mazzo.pop()
                self.cpu.append(carta2)
                for c in (self.tabellone.C1, self.tabellone.C2, self.tabellone.C3):
                    if c.GetLabel() == "":
                        c.SetLabel(str(carta2[0]) + carta2[1])
                        cartaC = c
                carta = mazzo.pop()
                self.user.append(carta)
                for u in (self.tabellone.U1, self.tabellone.U2, self.tabellone.U3):
                    if u.GetLabel() == "":
                        u.SetLabel(str(carta[0]) + carta[1])
                        cartaU = u
                        
            #carta pescata dall'utente
            img = Image.open("carte/" + carta[1] + str(carta[0]) + ".jpg")
            img = img.resize((150,250))
            img2 = img.copy()
            wx_Image = wx.Image(img2.size[0], img2.size[1])
            wx_Image.SetData(img2.convert("RGB").tobytes())
            cartaU.Show()
            cartaU.Bitmap = wx.Bitmap(wx_Image)
            
            #carta pescata dalla cpu
            cartaC.Show()
            cartaC.Bitmap = self.retro
        #Se le carta del mazzo sono finite, non pesco più
            
        else:
            self.CONTA += 1
            if self.CONTA == 4:
                self.Results()
                
            if self.CONTA == 1:
                if self.turno:
                    carta = mazzo.pop()
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
                    carta2 = mazzo.pop()
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

                #carta pescata dall'utente
                img = Image.open("carte/" + carta[1] + str(carta[0]) + ".jpg")
                img = img.resize((150,250))
                img2 = img.copy()
                wx_Image = wx.Image(img2.size[0], img2.size[1])
                wx_Image.SetData(img2.convert("RGB").tobytes())
                cartaU.Bitmap = wx.Bitmap(wx_Image)
                
                #carta pescata dalla cpu
                cartaC.Bitmap = self.retro
        print(len(mazzo))
        return
    
    def Results(self):
        self.tabellone.S3.SetLabel("THE GAME IS OVER!\nCalculating scores...")
        self.tabellone.Enable(False)
        puntiUtente = self.contaPunti(self.contaUSER)
        puntiCpu = self.contaPunti(self.contaCPU)
        self.homeFinale.Show()
        if puntiUtente > puntiCpu:
            self.homeFinale.winner.SetLabel("Congratulations! You are the winner!")
        elif puntiUtente < puntiCpu:
            self.homeFinale.winner.SetLabel("CPU is the winner of the match! Try again ;)")
        else:
            self.homeFinale.winner.SetLabel("None has won...")
        self.homeFinale.risultati.SetLabel("Punti CPU: " + str(puntiCpu) + "\nPunti USER: " + str(puntiUtente))
        self.tabellone.Hide()
        
        return
    
    def PulisciCampo(self):
        self.tabellone.S1.SetLabel("")
        self.contaCPU.append(self.cCPU)
        self.cCPU[2] = False
        self.cCPU = ""
        self.tabellone.S2.SetLabel("")
        self.contaUSER.append(self.cUser)
        self.cUser[2] = False
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
        for numero in lista:
            if numero == 10:
                somma += 4
            elif numero == 9:
                somma += 3
            elif numero == 8:
                somma += 2
            elif numero == 3:
                somma += 10
            elif numero == 1:
                somma += 11
        return somma
    
    def Start(self, evt):                 #Gioco vero e proprio (inizia e lascia giocare)
        self.lobby.Destroy()
        self.startGame()
        self.tabellone.Show()
        if not self.turno:
            self.GiocataCPU()
        return

#add tabelloni di gioco
if __name__ == "__main__":
    app = wx.App()
    a = Game()
    app.MainLoop()