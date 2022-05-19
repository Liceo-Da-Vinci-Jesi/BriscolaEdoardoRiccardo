#Edoardo Zingaretti | Riccardo Flavianelli
#Briscola
import random, classMazzo, Tabellone, wx, Lobby, Risultati, Setting, finestraMazzi, classGiocataCPU
from PIL import Image
class Game:
    def __init__(self):
        self.mazzo = classMazzo.Mazzo().generaMazzo()
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
    
        self.lobby = Lobby.Home()
        self.lobby.Show()
        self.lobby.nome.Bind(wx.EVT_TEXT_ENTER, self.Start)
        self.lobby.b1.Bind(wx.EVT_BUTTON, self.openSetting)
        self.lobby.b2.Bind(wx.EVT_BUTTON, self.Start)
        
        self.Setting = Setting.SETTING()
        self.Setting.Bind(wx.EVT_CLOSE, self.backLobby)
        self.Setting.Hide()
        
        #COLORE e DIMENSIONE sono le variabili, colore e dimensione sono le rispettive checkbox
        self.COLORE = self.Setting.COLORE
        self.colore = self.Setting.colore
        self.DIMENSIONE = self.Setting.DIMENSIONE
        self.dimensione = self.Setting.dimensione
        
        self.colore.Bind(wx.EVT_COMBOBOX, self.getColour)
        self.Setting.dimensione.Bind(wx.EVT_COMBOBOX, self.getRes)
        self.Setting.random.Bind(wx.EVT_RADIOBUTTON, self.getDifficulty)
        self.Setting.normal.Bind(wx.EVT_RADIOBUTTON, self.getDifficulty)
        self.Setting.tornaIndietro.Bind(wx.EVT_BUTTON, self.backLobby)
        self.difficulty = True #random
        
        self.tabellone = Tabellone.Tabellone()
        return
    
    def Start(self, evt):                 #Gioco vero e proprio (inizia e lascia giocare)
        self.lobby.Hide()
        self.startGame()
        self.tabellone.Show()
        self.tabellone.Centre()
        if not self.turno:
            self.timerCPU.StartOnce(1000)
        return

    def startGame(self):
        self.tabellone.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.tabellone.SetMaxSize(self.tabellone.res)
        self.tabellone.SetMinSize(self.tabellone.res)
        self.tabellone.mazzoCPU.SetBitmap(wx.Bitmap())
        self.tabellone.mazzoUtente.SetBitmap(wx.Bitmap())
        #collego i pulsanti  giocabili dall'utente alla loro funzione
        for pulsante in (self.tabellone.U1, self.tabellone.U2, self.tabellone.U3):
            pulsante.Bind(wx.EVT_BUTTON, self.GiocataUSER)
        
        self.nome = self.lobby.nome.GetValue()
        if self.turno:
            ordine = (self.user, self.cpu)
        else:
            ordine = (self.cpu, self.user)
        for n in range(3):
            for mano in ordine:
                carta = self.mazzo[0]
                self.mazzo.remove(self.mazzo[0])
                mano.append(carta)
                
        self.briscolaCarta = self.choiceBriscola()
        self.briscolaSeme = self.briscolaCarta[1]
        
        #carta coperta (mano CPU)
        img = Image.open(self.Setting.BackType[self.Setting.retro])
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        self.retro = wx.Bitmap(wx_Image)   
        
        #Imposto la mano della CPU
        c = 0
        for x in (self.tabellone.C1, self.tabellone.C2, self.tabellone.C3):
            x.SetLabel(str(self.cpu[c][0]) + self.cpu[c][1])
            x.SetBitmap(self.retro)
            c+=1
        
        #Imposto la Briscola e il mazzo nel tabellone
        self.tabellone.S4.SetLabel(str(self.briscolaCarta[0]) + self.briscolaCarta[1])
        self.ImpostaBitmap(self.briscolaCarta, self.tabellone.S4)
        self.tabellone.S5.SetBitmap(self.retro)
        
        #Imposto la mano dell'User
        c = 0
        for carta in (self.tabellone.U1, self.tabellone.U2, self.tabellone.U3):
            carta.SetLabel(str(self.user[c][0]) + self.user[c][1])
            self.ImpostaBitmap(self.user[c], carta)
            c += 1
        return
    
    def choiceBriscola(self):
            briscola = self.mazzo.pop()
            #aggiungo la briscola al mazzo in modo che venga pescata per ultima
            self.mazzo.append([briscola[0], briscola[1]])
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
                    self.ImpostaBitmap(cartaScelta, self.tabellone.S2)
                    self.tabellone.S2.SetLabel(cartaClickata)
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
                    self.ImpostaBitmap(cartaCPU , self.tabellone.S1)
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
                if len(self.contaUSER) == 0:
                    self.tabellone.mazzoUtente.SetBitmap(self.retro)
                self.contaUSER.append([self.cUser[0], self.cUser[1]])
                self.contaUSER.append([self.cCPU[0], self.cCPU[1]])
                self.tabellone.Count2.SetLabel(str((int(self.tabellone.Count2.GetLabel()) + 2)))
            else:
                if len(self.contaCPU) == 0:
                    self.tabellone.mazzoCPU.SetBitmap(self.retro)
                self.contaCPU.append([self.cCPU[0], self.cCPU[1]])
                self.contaCPU.append([self.cUser[0], self.cUser[1]])
                self.tabellone.Count1.SetLabel(str((int(self.tabellone.Count1.GetLabel()) + 2)))
            if len(self.mazzo) - 3 > 0:
                carteMazzo = len(self.mazzo) - 3
            else:
                carteMazzo = 0
            self.tabellone.carteMazzo.SetLabel(str(carteMazzo))
            self.tabellone.turnWinner.SetLabel("TAKES: " + vincitoreTurno)
            self.PulisciCampo()
            self.pescaCarta()
            self.tabellone.S1.Hide()
            self.tabellone.S2.Hide()
            if self.vincitoreTurno != self.nome and self.CONTA < 4:
                self.timerCPU.StartOnce(750)
        return
    
    #funzione che gestisce le pescate
    def pescaCarta(self):
        if self.vincitoreTurno == self.nome:
            ordine = ("u", "c")
        else:
            ordine = ("c", "u")
        if len(self.mazzo) > 3:
            self.Pescata(ordine)
        else:
            self.CONTA += 1
            if self.CONTA == 4:
                self.Results()
                return 
            if self.CONTA == 1: #faccio l'ultima pescata e nascondo la briscola e il mazzo
                self.Pescata(ordine)
                self.tabellone.S4.Hide()
                self.tabellone.S5.Hide()
        return
    
    #funzione che pesca
    def Pescata(self, ordine): #pescata normale
        for giocatore in ordine:
            carta = self.mazzo[0]
            self.mazzo.remove(self.mazzo[0])
            if giocatore == "u":
                self.user.append(carta)
                for u in (self.tabellone.U1, self.tabellone.U2, self.tabellone.U3):
                    if u.GetLabel() == "":
                        u.SetLabel(str(carta[0]) + carta[1])
                        cartaU = u
                        self.ImpostaBitmap(carta, cartaU)
            else:
                self.cpu.append(carta)
                for c in (self.tabellone.C1, self.tabellone.C2, self.tabellone.C3):
                    if c.GetLabel() == "":
                        c.SetLabel(str(carta[0]) + carta[1])
                        cartaC = c
                        cartaC.Show()
                        cartaC.Bitmap = self.retro

    def PulisciCampo(self):
        self.tabellone.S1.SetLabel("")
        self.cCPU = ""
        self.tabellone.S2.SetLabel("")
        self.cUser = ""
        self.tabellone.cartaUTENTE.SetLabel("")
        self.tabellone.cartaCPU.SetLabel("")
        return
    
    def Played(self,cartaUser,cartaCPU):  
        #ritorna il vincitore del turno
        importanza = [2,4,5,6,7,8,9,10,3,1]
        if cartaUser[1] == cartaCPU[1]:
            if importanza.index(cartaUser[0]) > importanza.index(cartaCPU[0]):
                self.vincitoreTurno = self.nome
            else:
                self.vincitoreTurno = "CPU"
        elif self.briscolaSeme in [cartaUser[1], cartaCPU[1]]:
            if cartaUser[1] == self.briscolaSeme:
                self.vincitoreTurno = self.nome
            else:
                self.vincitoreTurno = "CPU"
        else:
            if self.turno:
                self.vincitoreTurno = self.nome
            else:
                self.vincitoreTurno = "CPU"
        if self.vincitoreTurno == self.nome:
            self.turno = True
        else:
            self.turno = False
        return self.vincitoreTurno
    
#Ora le varie funzioni x le impostazioni
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
            self.tabellone.res = res
        elif self.DIMENSIONE == "1300x1050":
            self.tabellone.res = (1300, 1000)
        elif self.DIMENSIONE == "1050x1050":
            self.tabellone.res = (1000, 1000)
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
    
    def Results(self):
        self.tabellone.Hide()
        self.homeFinale = Risultati.Home(self.contaUSER, self.contaCPU, self.nome, self.COLORE)
        self.homeFinale.b2.Bind(wx.EVT_BUTTON, self.Restart)
        self.homeFinale.Show()
        return
    
    def Restart(self, evt):
        self.homeFinale.Destroy()
        self.__init__()
        return
    
    def OnEraseBackground(self, evt):
        dc = evt.GetDC()
        #print(dc)
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("../carte/Tavolo.jpg")
        dc.DrawBitmap(bmp, 0, 0)
    
    def ImpostaBitmap(self, carta, button):
        img = Image.open("../carte/" + carta[1] + str(carta[0]) + ".jpg")
        img = img.resize((150,250))
        img2 = img.copy()
        wx_Image = wx.Image(img2.size[0], img2.size[1])
        wx_Image.SetData(img2.convert("RGB").tobytes())
        button.Show()
        button.Bitmap = wx.Bitmap(wx_Image)
        return
if __name__ == "__main__":
    app = wx.App()
    a = Game()
    app.MainLoop()