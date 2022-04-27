import wx
from PIL import Image

class Tabellone(wx.Frame):
   def __init__(self):
        super().__init__(None, title="BRISCOLA | GAME")
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)        
        
        img = Image.open("carte/Retro1.jpg")
        img = img.resize((150,250))
        
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())

        bitmap = wx.Bitmap(wx_Image)
        
        hbox = wx.StaticBoxSizer(wx.HORIZONTAL, self.panel, "CPU's HAND")
        
        self.C1 = wx.BitmapButton(self.panel, bitmap=bitmap, id=1, name = "")
        self.C2 = wx.BitmapButton(self.panel, bitmap=bitmap, id=2, name = "")
        self.C3 = wx.BitmapButton(self.panel, bitmap=bitmap, id=3, name = "")
        hbox.Add(self.C1, proportion=1, flag=wx.ALL, border=5)
        hbox.Add(self.C2, proportion=1, flag=wx.ALL, border=5)
        hbox.Add(self.C3, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        grid = wx.GridSizer(rows=1, cols=5, vgap=5, hgap=5)
        #S = linea centrale: 5 colonne (1° carta CPU, 2° carta User, 3° vuoto, 4° Briscola, 5° Mazzo)
        #S1 = CARTA CPU
        self.S1 = wx.BitmapButton(self.panel, bitmap=bitmap, name = "")
        self.S1.Hide()
        #S2 = CARTA USER
        self.S2 = wx.BitmapButton(self.panel, bitmap=bitmap, name = "")
        self.S2.Hide()
        h = wx.BoxSizer(wx.VERTICAL)
        self.S3 = wx.StaticText(self.panel, label="")
        
        self.Count1 = wx.Button(self.panel, label = "0", pos=(100,0))
        font = wx.Font(10,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.Count1.SetFont(font)
        self.Count1.SetForegroundColour("white")
        self.Count1.SetBackgroundColour("black")
        self.Count2 = wx.Button(self.panel, label = "0", pos=(100,0))
        font = wx.Font(10,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.Count2.SetFont(font)
        self.Count2.SetForegroundColour("black")
        self.Count2.SetBackgroundColour("white")
        
        h.Add(self.Count1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        h.Add(self.Count2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        self.S4 = wx.BitmapButton(self.panel, bitmap=bitmap, name = "BRISCOLA")
        self.S5 = wx.BitmapButton(self.panel, bitmap=bitmap, name = "MAZZO")
        
        h1 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, "BRISCOLA")
        h1.Add(self.S4, proportion=1, flag=wx.ALL, border=5)
        self.h2 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, "DECK")
        self.h2.Add(self.S5, proportion=1, flag=wx.ALL, border=5)
        grid.Add(h1, proportion=1, flag=wx.ALL, border=5)
        grid.Add(self.S1, proportion=1, flag=wx.ALL, border=5)
        grid.Add(h, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        grid.Add(self.S2, proportion=1, flag=wx.ALL, border=5)
        grid.Add(self.h2, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(grid, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        hbox2 = wx.StaticBoxSizer(wx.HORIZONTAL, self.panel, "YOUR HAND")
        self.U1 = wx.BitmapButton(self.panel, bitmap=bitmap, id=4, name = "USER")
        self.U2 = wx.BitmapButton(self.panel, bitmap=bitmap, id=5, name = "USER")
        self.U3 = wx.BitmapButton(self.panel, bitmap=bitmap, id=6, name = "USER")
        hbox2.Add(self.U1, proportion=1, flag=wx.ALL, border=5)
        hbox2.Add(self.U2, proportion=1, flag=wx.ALL, border=5)
        hbox2.Add(self.U3, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)  
        
        #(BUG)
#         bmp = wx.Bitmap("../carte/Tavolo.jpg")
#         self.sfondo = wx.StaticBitmap(self.panel, bitmap = bmp)
          
        self.SetMinSize((960, 875))
        self.Move((350,50))
        self.panel.SetSizer(vbox)
        vbox.Fit(self)
        return



# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = Tabellone()
    window.Show()
    app.MainLoop()