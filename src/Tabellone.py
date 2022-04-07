import wx

class Tabellone(wx.Frame):
   def __init__(self):
        super().__init__(None, title="BRISCOLA | GAME")
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.C1 = wx.Button(self.panel, label="", id=1)
        self.C2 = wx.Button(self.panel, label="", id=2)
        self.C3 = wx.Button(self.panel, label="", id=3)
        hbox.Add(self.C1, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        hbox.Add(self.C2, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        hbox.Add(self.C3, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        
        grid = wx.GridSizer(rows=1, cols=5, vgap=5, hgap=5)
        #S = linea centrale: 5 colonne (1° carta CPU, 2° carta User, 3° vuoto, 4° Briscola, 5° Mazzo)
        #S1 = CARTA CPU
        self.S1 = wx.Button(self.panel, label="")
        self.S1.Hide()
        #S2 = CARTA USER
        self.S2 = wx.Button(self.panel, label="")
        self.S2.Hide()
        h = wx.BoxSizer(wx.HORIZONTAL)
        self.S3 = wx.StaticText(self.panel, label="")
        h.Add(self.S3, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        self.S4 = wx.Button(self.panel, label="BRISCOLA")
        self.S5 = wx.Button(self.panel, label="MAZZO")
        
        self.S4.Enable(False)
        self.S5.Enable(False)
        grid.Add(self.S4, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        grid.Add(self.S1, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        grid.Add(h, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        grid.Add(self.S2, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        grid.Add(self.S5, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(grid, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.U1 = wx.Button(self.panel, label="USER", id=4)
        self.U2 = wx.Button(self.panel, label="USER", id=5)
        self.U3 = wx.Button(self.panel, label="USER", id=6)
        hbox2.Add(self.U1, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        hbox2.Add(self.U2, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        hbox2.Add(self.U3, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        
        
        
        self.SetMinSize((960, 540))
        self.panel.SetSizer(vbox)
        return



# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = Tabellone()
    window.Show()
    app.MainLoop()