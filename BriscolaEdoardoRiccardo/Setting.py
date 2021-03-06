import wx
from PIL import Image

# ---------------------------------
import os
module_dir = os.path.dirname(__file__)
# ---------------------------------

class SETTING(wx.Frame):

    def __init__(self):
        super().__init__(None, title="BRISCOLA | SETTINGS")
        self.panel = wx.Panel(self)
        self.SetIcon(wx.Icon( os.path.join(module_dir,"icone/briscola.ico") ))
        box = wx.BoxSizer(wx.VERTICAL)
        vbox = wx.StaticBoxSizer(wx.VERTICAL, self.panel,"SETTING")

        st1 = wx.StaticText(self.panel, label="Background Colour:")
        colori = ["brown", "dark green", "grey", "orange", "purple", "dark grey"]
        self.colore = wx.ComboBox(self.panel, choices = colori, style = wx.CB_READONLY | wx.CB_SORT)
        self.colore.SetValue("dark green")
        self.SetBackgroundColour("dark green")
        self.COLORE = "dark green"
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(st1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox.Add(self.colore, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox,proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        
        st2 = wx.StaticText(self.panel, label="Resolution:")
        #dim = ["FULLSCREEN", "1300x1050", "1050x1050"]
        dim = ["FULLSCREEN"]
        self.dimensione = wx.ComboBox(self.panel, choices = dim, style = wx.CB_READONLY)
        self.dimensione.SetValue("FULLSCREEN")
        self.DIMENSIONE = "1000x1050"
        
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
        
        self.BackType = {"Piacentine":os.path.join(module_dir,"carte/Retro1.jpg"), "Yu-Gi-Oh":os.path.join(module_dir,"carte/Retro2.jpg") }
        
        bitmap = self.ImpostaBitmap( os.path.join(module_dir,"carte/Retro1.jpg"), (30,50))
        bRetro1 = wx.BitmapButton(self.panel, bitmap = bitmap, id=1)
        
        bitmap = self.ImpostaBitmap( os.path.join(module_dir,"carte/Retro2.jpg"), (30,50))
        bRetro2 = wx.BitmapButton(self.panel, bitmap = bitmap, id=2)
        
        hbox4.Add(self.st4, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL, border=5)
        hbox4.Add(wx.StaticText(self.panel, label=""), proportion=1, flag=wx.ALL, border=5)
        hbox4.Add(bRetro1, proportion=0, flag=wx.ALL, border=5)
        hbox4.Add(bRetro2, proportion=0, flag=wx.ALL, border=5)
        hbox4.Add(wx.StaticText(self.panel, label=""), proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox4, proportion=0, flag=wx.ALL | wx.EXPAND, border=5)
        
        bRetro1.Bind(wx.EVT_BUTTON, self.getBackType)
        bRetro2.Bind(wx.EVT_BUTTON, self.getBackType)
        
        bitmap = self.ImpostaBitmap( os.path.join(module_dir,"icone/goback.png"), (75,50))
        self.tornaIndietro = wx.BitmapButton(self.panel, bitmap = bitmap)

        vbox.Add(wx.StaticText(self.panel, label=""), proportion=1, flag=wx.EXPAND)
        vbox.Add(self.tornaIndietro, proportion=0, flag=wx.ALL | wx.ALIGN_RIGHT, border=5)
        
        box.Add(vbox, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        
        self.panel.SetSizer(box)
        self.Maximize()
        res = self.GetSize()
        if res[0] >= 1600 and res[1] >= 1000:
            self.SetMinSize((res[0] / 4.8, res[1] / 2.3))
            self.SetMaxSize((res[0] / 4.8, res[1] / 2.3))
        else:
            self.SetMinSize((res[0] / 2.5, res[1] / 1.3 ))
            self.SetMaxSize((res[0] /2.5, res[1] / 1.3 ))
        self.Centre()
        self.Move((400,150))

    def getBackType(self, evt):
        if evt.GetId() == 1:
            self.retro = "Piacentine"
            self.st4.SetLabel("Back of cards: Piacentine")
        else:
            self.retro = "Yu-Gi-Oh"
            self.st4.SetLabel("Back of cards: Yu-Gi-Oh!")
    
    def ImpostaBitmap(self, file, dim):
        img = Image.open(file)
        img = img.resize((dim))
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
        return bitmap

# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = SETTING()
    window.Show()
    app.MainLoop()
