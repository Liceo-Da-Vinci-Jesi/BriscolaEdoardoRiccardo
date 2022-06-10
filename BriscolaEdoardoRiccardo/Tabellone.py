import wx
from PIL import Image

# ---------------------------------
import os
module_dir = os.path.dirname(__file__)
# ---------------------------------

class Tabellone(wx.Frame):
   def __init__(self):
        super().__init__(None, title="BRISCOLA | GAME")
        self.panel = wx.Panel(self)
        self.Maximize()
        self.res = self.GetSize()
        #print(self.res)
        self.SetMinSize(self.res)
        self.SetMaxSize(self.res)
        if self.res[0] >= 1600 and self.res[1] >= 1000:
            self.SizeX = int(self.res[0] / 13)
            self.SizeY = int(self.res[1] / 4.2)
        else:
            self.SizeX = int(self.res[0] / 15)
            self.SizeY = int(self.res[1] / 5.7)
        vbox = wx.BoxSizer(wx.VERTICAL)        
        self.SetIcon(wx.Icon("icone/briscola.ico"))
          
        img = Image.open("carte/Retro1.jpg")
        img = img.resize((self.SizeX,self.SizeY))
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
                
        #Descrizione Turno
        h = wx.BoxSizer(wx.HORIZONTAL)
        v1 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, "CARD CPU")
        v2 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, "DECK's CARDS")
        v3 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, "CARD PLAYED")
        self.cartaCPU = wx.StaticText(self.panel, label="10 BASTONI")
        self.cartaUTENTE = wx.StaticText(self.panel, label="10 BASTONI")
        self.carteMazzo = wx.StaticText(self.panel, label="33")
        font = wx.Font(12,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        for x in (self.cartaCPU,self.cartaUTENTE,self.carteMazzo):
            x.SetFont(font)
            x.SetForegroundColour("white")
        v1.Add(self.cartaCPU, proportion=1, flag=wx.ALL, border=0)
        v2.Add(self.carteMazzo, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=0)
        v3.Add(self.cartaUTENTE, proportion=1, flag=wx.ALL, border=0)
        for x in (v1, v2, v3):
            h.Add(x, proportion=1, flag=wx.ALL, border=5)
        self.cartaCPU.SetLabel("")
        self.cartaUTENTE.SetLabel("")
        vbox.Add(h, proportion=0, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        #Mano CPU
        h = wx.BoxSizer(wx.HORIZONTAL)
        hbox = wx.StaticBoxSizer(wx.HORIZONTAL, self.panel, "CPU's HAND")
        
        self.C1 = wx.StaticBitmap(self.panel, bitmap=bitmap, id=1, name = "")
        self.C2 = wx.StaticBitmap(self.panel, bitmap=bitmap, id=2, name = "")
        self.C3 = wx.StaticBitmap(self.panel, bitmap=bitmap, id=3, name = "")
        hbox.Add(self.C1, proportion=1, flag=wx.ALL, border=5)
        hbox.Add(self.C2, proportion=1, flag=wx.ALL, border=5)
        hbox.Add(self.C3, proportion=1, flag=wx.ALL, border=5)
        
        self.mazzoCPU = wx.StaticBitmap(self.panel, bitmap=bitmap, size=(self.SizeX,self.SizeY))
        h.Add(hbox, proportion=2, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        h.Add(self.mazzoCPU, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL, border=5)
        vbox.Add(h, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        grid = wx.GridSizer(rows=1, cols=5, vgap=5, hgap=5)
        #S = linea centrale: 5 colonne (1° carta CPU, 2° carta User, 3° vuoto, 4° Briscola, 5° Mazzo)
        #S1 = CARTA CPU
        self.S1 = wx.StaticBitmap(self.panel, bitmap=bitmap)
        #S2 = CARTA USER
        self.S2 = wx.StaticBitmap(self.panel, bitmap=bitmap)
        
        h = wx.StaticBoxSizer(wx.VERTICAL, self.panel, "TAKEN")
        self.S3 = wx.StaticText(self.panel, label="")
        self.Count1 = wx.StaticText(self.panel, label = "0")
        font = wx.Font(17,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.Count2 = wx.StaticText(self.panel, label = "0")
        for x in (self.Count1, self.Count2):
            x.SetFont(font)
            x.SetForegroundColour("black")
            x.SetBackgroundColour("white")
        self.turnWinner = wx.StaticText(self.panel, label="Enjoy the game! ;)")
        self.turnWinner.SetForegroundColour("white")
        self.turnWinner.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        h.Add(self.Count1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        h.Add(self.turnWinner, proportion=0, flag=wx.ALL | wx.ALIGN_LEFT, border=5)
        h.Add(self.Count2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        self.S4 = wx.StaticBitmap(self.panel, bitmap=bitmap)
        self.S5 = wx.StaticBitmap(self.panel, bitmap=bitmap)
        
        h1 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, "BRISCOLA")
        h1.Add(self.S4, proportion=1, flag=wx.ALL, border=5)
        h2 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, "DECK")
        h2.Add(self.S5, proportion=1, flag=wx.ALL, border=5)
        
        grid.Add(h1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        grid.Add(self.S1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        grid.Add(h, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        grid.Add(self.S2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        grid.Add(h2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox.Add(grid, proportion=2, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        h = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.StaticBoxSizer(wx.HORIZONTAL, self.panel, "YOUR HAND")
        self.U1 = wx.BitmapButton(self.panel, bitmap=bitmap, id=4, name = "USER")
        self.U2 = wx.BitmapButton(self.panel, bitmap=bitmap, id=5, name = "USER")
        self.U3 = wx.BitmapButton(self.panel, bitmap=bitmap, id=6, name = "USER")
        hbox2.Add(self.U1, proportion=1, flag=wx.ALL, border=5)
        hbox2.Add(self.U2, proportion=1, flag=wx.ALL, border=5)
        hbox2.Add(self.U3, proportion=1, flag=wx.ALL, border=5)
        h.Add(hbox2, proportion=2, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        self.mazzoUtente = wx.StaticBitmap(self.panel, bitmap=bitmap, size=(self.SizeX,self.SizeY))
        h.Add(self.mazzoUtente, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL, border=5)
        
        vbox.Add(h, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        self.SetBackgroundColour("dark green")
        
        self.panel.SetSizer(vbox)
        vbox.Fit(self)
        return
            # ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = Tabellone()
    window.Show()
    app.MainLoop()
