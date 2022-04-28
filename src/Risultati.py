import wx

class Home(wx.Frame):

    def __init__(self):
        super().__init__(None, title="BRISCOLA | RESULTS")
        self.panel = wx.Panel(self)
        
        font = wx.Font(20,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        vbox  = wx.BoxSizer(wx.VERTICAL)
        staticText = wx.StaticText(self.panel, label = "THANK YOU\nFOR HAVING PLAYED!")
        staticText.SetFont(font)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(staticText, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)

        self.winner = wx.StaticText(self.panel, label = "")
        font2 = wx.Font(12,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.winner.SetFont(font2)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.winner, proportion=1, flag=wx.ALL, border=0)
        vbox.Add(hbox2, proportion=1, flag=wx.ALL | wx.EXPAND, border=0)
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.risultati = wx.StaticText(self.panel, label="")
        hbox4.Add(self.risultati, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox4, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.b1 = wx.Button(self.panel, label="PRESE", size=(50,50))
        self.b3 = wx.Button(self.panel, label="CLOSE", size=(50,50))
        
        self.b3.Bind(wx.EVT_BUTTON, self.Chiudi)
        
        hbox3.Add(self.b1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox3.Add(self.b3, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox.Add(hbox3, proportion=1, flag=wx.ALL | wx.EXPAND, border=0)
        
        
        self.panel.SetSizer(vbox)
        self.SetMinSize((400,250))
        self.SetMaxSize((400,250))
        self.Centre()
        
    def Chiudi(self, evt):
        self.Close()
        return

# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = Home()
    window.Show()
    app.MainLoop()