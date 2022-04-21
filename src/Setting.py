import wx
from PIL import Image
class SETTING(wx.Frame):

    def __init__(self):
        super().__init__(None, title="BRISCOLA | SETTINGS")
        self.panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        vbox = wx.StaticBoxSizer(wx.VERTICAL, self.panel,"SETTING")
        
        st1 = wx.StaticText(self.panel, label="Background Colour:")
        colori = ["red", "green", "white", "yellow", "blue"]
        self.colore = wx.ComboBox(self.panel, choices = colori, style = wx.CB_READONLY | wx.CB_SORT)
        self.panel.SetBackgroundColour("white")
        self.COLORE = "white"
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(st1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox.Add(self.colore, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox,proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        
        st2 = wx.StaticText(self.panel, label="Resolution:")
        dim = ["FULLSCREEN", "1200x780", "960x540"]
        self.dimensione = wx.ComboBox(self.panel, choices = dim, style = wx.CB_READONLY)
        self.DIMENSIONE = "400x250"
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(st2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox2.Add(self.dimensione, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox2,proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        
        st3 = wx.StaticText(self.panel, label="Difficulty:")
        self.random = wx.RadioButton(self.panel, label="Random", style=wx.RB_GROUP)
        self.normal = wx.RadioButton(self.panel, label="Normal")
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(st3, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL , border=5)
        vbox2=wx.BoxSizer(wx.VERTICAL)
        vbox2.Add(self.random, proportion=1, flag=wx.ALL, border=5)
        vbox2.Add(self.normal, proportion=1, flag=wx.ALL, border=5)
        hbox3.Add(vbox2, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox3,proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st4 = wx.StaticText(self.panel, label = "Retro Carte: Yu-Gi-Oh!")
        self.retro = "Yu-Gi-Oh!"
        
        img = Image.open("carte/Retro1.jpg")
        img = img.resize((30,50))
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
        self.bRetro1 = wx.BitmapButton(self.panel, bitmap = bitmap)
        
        img = Image.open("carte/Retro2.jpg")
        img = img.resize((30,50))
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
        self.bRetro2 = wx.BitmapButton(self.panel, bitmap = bitmap)
        
        hbox4.Add(st4, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL, border=5)
        hbox4.Add(self.bRetro1, proportion=0, flag=wx.ALL, border=5)
        hbox4.Add(self.bRetro2, proportion=0, flag=wx.ALL, border=5)
        vbox.Add(hbox4, proportion=1, flag=wx.ALL, border=5)
        
        self.tornaIndietro = wx.Button(self.panel, label = "Back to the lobby")

        vbox.Add(wx.StaticText(self.panel, label=""), proportion=1, flag=wx.EXPAND)
        vbox.Add(self.tornaIndietro, proportion=0, flag=wx.ALL | wx.ALIGN_RIGHT, border=5)
        
        box.Add(vbox, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.SetMinSize((400, 500))
        self.SetMaxSize((400, 500))
        self.panel.SetSizer(box)
        self.Centre()
        self.Move((400,150))

# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = SETTING()
    window.Show()
    app.MainLoop()

