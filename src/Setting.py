import wx
from PIL import Image
class SETTING(wx.Frame):

    def __init__(self):
        super().__init__(None, title="BRISCOLA | SETTINGS")
        self.panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        vbox = wx.StaticBoxSizer(wx.VERTICAL, self.panel,"SETTING")

        st1 = wx.StaticText(self.panel, label="Background Colour:")
        colori = ["brown", "dark green", "grey", "orange", "purple"]
        self.colore = wx.ComboBox(self.panel, choices = colori, style = wx.CB_READONLY | wx.CB_SORT)
        self.COLORE = "dark green"
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(st1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox.Add(self.colore, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox,proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        
        st2 = wx.StaticText(self.panel, label="Resolution:")
        dim = ["FULLSCREEN", "1300x1000", "1000x1000"]
        self.dimensione = wx.ComboBox(self.panel, choices = dim, style = wx.CB_READONLY)
        self.DIMENSIONE = "1000x1000"
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(st2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox2.Add(self.dimensione, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox2,proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        
        st3 = wx.StaticText(self.panel, label="Difficulty:")
        self.random = wx.RadioButton(self.panel, label="Random", style=wx.RB_GROUP)
        self.normal = wx.RadioButton(self.panel, label="Hard")
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(st3, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL , border=5)
        vbox2=wx.BoxSizer(wx.VERTICAL)
        vbox2.Add(self.random, proportion=1, flag=wx.ALL, border=5)
        vbox2.Add(self.normal, proportion=1, flag=wx.ALL, border=5)
        hbox3.Add(vbox2, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox3,proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.st4 = wx.StaticText(self.panel, label = "Back of cards: Piacentine")
        self.retro = "Piacentine"
        
        self.BackType = {"Piacentine":"../carte/Retro1.jpg", "Yu-Gi-Oh":"../carte/Retro2.jpg"}
        
        img = Image.open("../carte/Retro1.jpg")
        img = img.resize((30,50))
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
        bRetro1 = wx.BitmapButton(self.panel, bitmap = bitmap, id=1)
        
        img = Image.open("../carte/Retro2.jpg")
        img = img.resize((30,50))
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
        bRetro2 = wx.BitmapButton(self.panel, bitmap = bitmap, id=2)
        
        hbox4.Add(self.st4, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL, border=5)
        hbox4.Add(wx.StaticText(self.panel, label=""), proportion=1, flag=wx.ALL, border=5)
        hbox4.Add(bRetro1, proportion=0, flag=wx.ALL, border=5)
        hbox4.Add(bRetro2, proportion=0, flag=wx.ALL, border=5)
        hbox4.Add(wx.StaticText(self.panel, label=""), proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox4, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        
        bRetro1.Bind(wx.EVT_BUTTON, self.getBackType)
        bRetro2.Bind(wx.EVT_BUTTON, self.getBackType)
        
        img = Image.open("../carte/goback.png")
        img = img.resize((75,50))
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
        self.tornaIndietro = wx.BitmapButton(self.panel, bitmap = bitmap)

        vbox.Add(wx.StaticText(self.panel, label=""), proportion=1, flag=wx.EXPAND)
        vbox.Add(self.tornaIndietro, proportion=0, flag=wx.ALL | wx.ALIGN_RIGHT, border=5)
        
        box.Add(vbox, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        
        self.SetMinSize((400, 500))
        self.SetMaxSize((400, 500))
        self.panel.SetSizer(box)
        self.Centre()
        self.Move((400,150))

    def getBackType(self, evt):
        if evt.GetId() == 1:
            self.retro = "Piacentine"
            self.st4.SetLabel("Back of cards: Piacentine")
        else:
            self.retro = "Yu-Gi-Oh"
            self.st4.SetLabel("Back of cards: Yu-Gi-Oh!")
# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = SETTING()
    window.Show()
    app.MainLoop()

