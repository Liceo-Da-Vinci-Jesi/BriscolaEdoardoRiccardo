import wx, finestraMazzi

class Home(wx.Frame):

    def __init__(self, preseUTENTE, preseCPU, nome, colore):
        super().__init__(None, title="BRISCOLA | RESULTS")
        self.panel = wx.Panel(self)
        self.colore = colore
        
        self.contaBarra = 0
        self.timerBarra = wx.Timer()
        self.timerBarra.Bind(wx.EVT_TIMER, self.caricaBarra)
        self.checkGauge = True #è attiva
        self.timerBarra.Start(1)
        
        self.contaUSER = preseUTENTE
        self.contaCPU = preseCPU
        self.nome = nome
        self.Punti = [0, 11, 0, 10, 0, 0, 0, 0, 2, 3, 4]
        
        font = wx.Font(20,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        vbox  = wx.BoxSizer(wx.VERTICAL)
        staticText = wx.StaticText(self.panel, label = "THANK YOU\nFOR HAVING PLAYED!")
        staticText.SetFont(font)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(staticText, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)

        self.winner = wx.StaticText(self.panel, label = "Calculating scores, please wait")
        font2 = wx.Font(12,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.winner.SetFont(font2)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.winner, proportion=1, flag=wx.ALL, border=0)
        vbox.Add(hbox2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=0)
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        v = wx.StaticBoxSizer(wx.VERTICAL, self.panel, "SCORE")
        self.risultati = wx.StaticText(self.panel, label="CPU:\nYOU:")
        v.Add(self.risultati, proportion=1, flag=wx.ALL, border=5)
        
        
        hbox4.Add(v, proportion=0, flag=wx.ALL , border=5)
        vbox.Add(hbox4, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        
        self.barra = wx.Gauge(self.panel, range=50)
        vbox.Add(self.barra, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.b1 = wx.Button(self.panel, label="TAKEN", size=(50,50))
        self.b2 = wx.Button(self.panel, label="RESTART", size=(50,50))
        self.b3 = wx.Button(self.panel, label="CLOSE", size=(50,50))
        self.b1.Bind(wx.EVT_BUTTON, self.openMazzi)
        self.b3.Bind(wx.EVT_BUTTON, self.Chiudi)
        self.b1.Enable(False)
        self.b2.Enable(False)
        self.b3.Enable(False)
        
        hbox3.Add(self.b1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox3.Add(self.b2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox3.Add(self.b3, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox.Add(hbox3, proportion=1, flag=wx.ALL | wx.EXPAND, border=0)
        
        self.SetBackgroundColour(self.colore)
        self.panel.SetSizer(vbox)
        self.SetMinSize((400,300))
        self.SetMaxSize((400,300))
        self.Centre()
        
    def Chiudi(self, evt):
        self.Close()
        return
    
    def caricaBarra(self, evt):
        if self.checkGauge:
            self.contaBarra += 1
            self.barra.SetValue(self.contaBarra)
            if self.barra.GetValue() == (self.barra.GetRange() + 50):
                self.barra.Destroy()
                self.checkGauge = False
        else:
            self.b1.Enable(True)
            self.b2.Enable(True)
            self.b3.Enable(True)
            self.timerBarra.Stop()
            puntiUtente = self.contaPunti(self.contaUSER)
            puntiCpu = self.contaPunti(self.contaCPU)
            if puntiUtente > puntiCpu:
                self.winner.SetLabel("Congratulations! You are the winner!")
            elif puntiUtente < puntiCpu:
                self.winner.SetLabel("CPU is the winner! Try again ;)")
            else:
                self.winner.SetLabel("None has won...")
            self.risultati.SetLabel("CPU: " + str(puntiCpu) + "\nYOU" + ": " + str(puntiUtente))
            return
        
    def contaPunti(self, l):
        lista = l
        somma = 0
        for n in lista:
            somma += self.Punti[n[0]]
        return somma
    
    def openMazzi(self, evt):
        self.Enable(False)
        self.finestra = finestraMazzi.Home(self.contaUSER, self.contaCPU, self.nome, self.colore)
        self.finestra.Show()
        self.finestra.button.Bind(wx.EVT_BUTTON, self.closeMazzi)
        self.finestra.Bind(wx.EVT_CLOSE, self.closeMazzi)
        return
    
    def closeMazzi(self, evt):
        self.finestra.Destroy()
        self.Raise()
        self.Enable(True)
        return
# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = Home()
    window.Show()
    app.MainLoop()