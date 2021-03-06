import wx, Tabellone
from PIL import Image

import finestraMazzi

# ---------------------------------
import os
module_dir = os.path.dirname(__file__)
# ---------------------------------

class Home(wx.Frame):

    def __init__(self, preseUTENTE, preseCPU, nome, colore):
        super().__init__(None, title="BRISCOLA | RESULTS")
        panel = wx.Panel(self)
        self.SetIcon(wx.Icon( os.path.join(module_dir,"icone/briscola.ico") ))
        res = Tabellone.Tabellone().res
        print(res)
        if res[0] >= 1500 and res[1] >= 950:
            self.SetMinSize((res[0]/3.7,res[1]/2.5))
            self.SetMaxSize((res[0]/3.7,res[1]/2.5))
        elif res[0] >= 950 and res[1] >= 700:
            self.SetMinSize((res[0]/2.9,res[1]/1.9))
            self.SetMaxSize((res[0]/2.9,res[1]/1.9))
        else: #res minima (800x600)
            self.SetMinSize((res[0]/2,res[1]/1.5))
            self.SetMaxSize((res[0]/2,res[1]/1.5))
            
        self.SetBackgroundColour("dark grey")
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
        staticText = wx.StaticText(panel, label = "THANK YOU FOR\nHAVING PLAYED!")
        staticText.SetForegroundColour("white")
        staticText.SetFont(font)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(staticText, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)

        self.winner = wx.StaticText(panel, label = "Calculating scores, please wait ...")
        self.winner.SetForegroundColour("light grey")
        font2 = wx.Font(13,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.winner.SetFont(font2)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.winner, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        v = wx.StaticBoxSizer(wx.VERTICAL, panel, "SCORE")
        self.risultati = wx.StaticText(panel, label="CPU:\nYOU:")
        self.risultati.SetForegroundColour("white")
        v.Add(self.risultati, proportion=1, flag=wx.ALL, border=5)
        
        self.immagine = wx.StaticBitmap(panel, bitmap = self.ImpostaBitmap( os.path.join(module_dir,"icone/loadingIcon.png"), (125,100)), size=(200,75))
        v2 = wx.BoxSizer(wx.VERTICAL)
        v2.Add(self.immagine, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        hbox4.Add(v, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL, border=5)
        hbox4.Add(v2, proportion=0, flag=wx.ALL, border=5)
        vbox.Add(hbox4, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        
        self.barra = wx.Gauge(panel, range=25)
        vbox.Add(self.barra, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        bitmap = self.ImpostaBitmap( os.path.join(module_dir,"icone/cardsIcon.png"), (125,85))
        self.b1 = wx.BitmapButton(panel, bitmap = bitmap, size=(75,75))
        bitmap = self.ImpostaBitmap( os.path.join(module_dir,"icone/restartIcon.png"), (125,75))
        self.b2 = wx.BitmapButton(panel, bitmap=bitmap, size=(75,75))
        bitmap = self.ImpostaBitmap( os.path.join(module_dir,"icone/closeIcon.png"), (75,75))
        self.b3 = wx.BitmapButton(panel, bitmap=bitmap, size=(75,75))
        self.b1.Bind(wx.EVT_BUTTON, self.openMazzi)
        self.b3.Bind(wx.EVT_BUTTON, self.Chiudi)
        self.b1.Enable(False)
        self.b2.Enable(False)
        self.b3.Enable(False)
        
        er = wx.StaticBitmap(panel, bitmap=self.ImpostaBitmap( os.path.join(module_dir,"icone/ER.png"), (50,25)))
        
        hbox3.Add(self.b1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox3.Add(self.b2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox3.Add(self.b3, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox.Add(hbox3, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=0)
        panel.SetSizer(vbox)
        self.Centre()
        
    def Chiudi(self, evt):
        self.Close()
        wx.Exit()
        return
    
    def caricaBarra(self, evt):
        if self.checkGauge:
            self.contaBarra += 1
            # PROF: Come era prima non aveva senso... se mettete una barra da 25, a 25 vi fermate...
            # PROF: o la fate più lunga... o più lenta
            if self.contaBarra <= 25:
                self.barra.SetValue(self.contaBarra)
            else:
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
                self.winner.SetLabel("Well Done! You are the winner!!!")
                bitmap = self.ImpostaBitmap( os.path.join(module_dir,"icone/winIcon2.png"), (125,75))
            elif puntiUtente < puntiCpu:
                self.winner.SetLabel("CPU has won the game! Try again ;)")
                bitmap = self.ImpostaBitmap( os.path.join(module_dir,"icone/loseIcon.png"), (150,75))
            else:
                self.winner.SetLabel("None has won the game, try again!")
                bitmap = self.ImpostaBitmap( os.path.join(module_dir,"icone/drawIcon.jpg"), (150,75))
            self.immagine.SetBitmap(bitmap)
            self.risultati.SetLabel("CPU: " + str(puntiCpu) + "\nYOU" + ": " + str(puntiUtente))
            return
        
    def contaPunti(self, l):
        somma = 0
        for n in l:
            somma += self.Punti[n[0]]
        return somma
    
    def openMazzi(self, evt):
        self.Enable(False)
        self.finestra = finestraMazzi.Home(self.contaUSER, self.contaCPU, self.nome, self.colore)
        self.finestra.Show()
    #self.finestra.button.Bind(wx.EVT_BUTTON, self.closeMazzi)
        self.finestra.Bind(wx.EVT_CLOSE, self.closeMazzi)
        return
    
    def closeMazzi(self, evt):
        self.finestra.Destroy()
        self.Raise()
        self.Enable(True)
        return
    
    def ImpostaBitmap(self, file, dim):
        img = Image.open(file)
        img = img.resize((dim)) #150x75 o 75x75
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
        return bitmap
# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = Home([[2, "Denari"]], [[1, "Coppe"]], "nome", "dark green")
    window.Show()
    app.MainLoop()
