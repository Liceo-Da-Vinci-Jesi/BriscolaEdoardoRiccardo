import wx, webbrowser, Tabellone
from PIL import Image

# ---------------------------------
import os
module_dir = os.path.dirname(__file__)
# ---------------------------------
import wx, webbrowser
from PIL import Image

class Home(wx.Frame):

    def __init__(self):
        super().__init__(None, title="BRISCOLA | HOME")
        panel = wx.Panel(self)
        
        self.SetIcon(wx.Icon("icone/briscola.ico"))
        
        font = wx.Font(55,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        vbox  = wx.BoxSizer(wx.VERTICAL)
        staticText = wx.StaticText(panel, label = "WELCOME!")
        staticText.SetForegroundColour("white")
        staticText.SetFont(font)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(staticText, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)

        self.st2 = wx.StaticText(panel, label = "DIFFICULTY SELECTED: RANDOM")
        self.st2.SetForegroundColour("light grey")
        font2 = wx.Font(15,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.st2.SetFont(font2)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.st2, proportion=1, flag=wx.ALL, border=0)
        vbox.Add(hbox2, proportion=0, flag=wx.ALL | wx.ALIGN_CENTRE, border=0)
        
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        powered = wx.StaticText(panel, label="Powered By:") #307-200
        font = wx.Font(12,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        powered.SetForegroundColour("white")
        powered.SetFont(font)
        er = wx.StaticBitmap(panel, bitmap = self.ImpostaBitmap("icone/ER.png", (50,35)))
        hbox5.Add(powered, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL, border=0)
        hbox5.Add(er, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL, border=0)
        vbox.Add(hbox5, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=0)
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(panel, label="Username:")
        st3.SetFont(font)
        st3.SetForegroundColour("grey")
        self.nome = wx.TextCtrl(panel, style = wx.TE_PROCESS_ENTER | wx.TE_CENTRE)
        hbox4.Add(st3, proportion=1, flag=wx.ALL, border=5)
        hbox4.Add(self.nome, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox4, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        self.nome.Bind(wx.EVT_TEXT, self.pulsanteStart)
        self.nome.SetMaxLength(8)
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        bitmap = self.ImpostaBitmap("icone/settingIcon.png", (150, 100))
        self.b1 = wx.BitmapButton(panel, bitmap = bitmap, size= (150,100))
        self.b1.SetBackgroundColour("white")
        
        bitmap = self.ImpostaBitmap("icone/startIcon.png", (150,125))
        self.b2 = wx.BitmapButton(panel, bitmap = bitmap, size=(150,75))
        self.b2.Enable(False)
        
        bitmap = self.ImpostaBitmap("icone/RulesIcon.png", (150,75))
        self.b3 = wx.BitmapButton(panel, bitmap = bitmap, size=(150,75))
        
        self.b3.Bind(wx.EVT_BUTTON, self.openBrowser)
        
        for x in (self.b1, self.b2, self.b3):
            x.SetBackgroundColour("dark grey")
        
        hbox3.Add(self.b1, proportion=2, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox3.Add(self.b2, proportion=2, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox3.Add(self.b3, proportion=2, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox.Add(hbox3, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=0)
        
        self.SetBackgroundColour("dark grey")
        panel.SetSizer(vbox)
        res = Tabellone.Tabellone().res
        if res[0] >= 1500 and res[1] >= 950:
            self.SetMinSize((res[0] / 3.94, res[1] / 3.04))
            self.SetMaxSize((res[0] / 3.94, res[1] / 3.04))
        else:
            self.SetMinSize((650, 400))
            self.SetMaxSize((650, 400))
        self.Centre()
        
    def pulsanteStart(self, evt):
        if self.nome.GetValue() != "":
            self.b2.Enable(True)
        else:
            self.b2.Enable(False)
        return
    
    def openBrowser(self, evt):
        webbrowser.open("https://en.wikipedia.org/wiki/Briscola")
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
    window = Home()
    window.Show()
    app.MainLoop()

