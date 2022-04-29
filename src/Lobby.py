import wx, webbrowser
from PIL import Image

class Home(wx.Frame):

    def __init__(self):
        super().__init__(None, title="BRISCOLA | HOME")
        self.panel = wx.Panel(self)
        
        font = wx.Font(35,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        vbox  = wx.BoxSizer(wx.VERTICAL)
        staticText = wx.StaticText(self.panel, label = "WELCOME!")
        staticText.SetForegroundColour("red")
        staticText.SetFont(font)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(staticText, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)

        self.st2 = wx.StaticText(self.panel, label = "DIFFICULTY SELECTED: RANDOM")
        font2 = wx.Font(10,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.st2.SetFont(font2)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.st2, proportion=1, flag=wx.ALL, border=0)
        vbox.Add(hbox2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=0)
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(self.panel, label="Username:")
        self.nome = wx.TextCtrl(self.panel, style = wx.TE_PROCESS_ENTER)
        hbox4.Add(st3, proportion=1, flag=wx.ALL, border=5)
        hbox4.Add(self.nome, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox4, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        self.nome.Bind(wx.EVT_TEXT, self.pulsanteStart)
        
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        img = Image.open("../carte/settingIcon.png")
        img = img.resize((100,40))
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
        self.b1 = wx.BitmapButton(self.panel, bitmap = bitmap, size=(50,50))
        self.b1.SetBackgroundColour("white")
        
        img = Image.open("../carte/startIcon.png")
        img = img.resize((116,50))
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
        self.b2 = wx.BitmapButton(self.panel, bitmap = bitmap, size=(50,50))
        self.b2.Enable(False)
        
        img = Image.open("../carte/RulesIcon.png")
        img = img.resize((60,45))
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
        self.b3 = wx.BitmapButton(self.panel, bitmap = bitmap, size=(50,50))
        
        self.b3.Bind(wx.EVT_BUTTON, self.openBrowser)
        
        hbox3.Add(self.b1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox3.Add(self.b2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        hbox3.Add(self.b3, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox.Add(hbox3, proportion=1, flag=wx.ALL | wx.EXPAND, border=0)
        
        self.SetMinSize((400,250))
        self.SetMaxSize((400,250))
        self.panel.SetSizer(vbox)
        self.Centre()
    
    def pulsanteStart(self, evt):
        if self.nome.GetValue() != "":
            self.b2.Enable(True)
        else:
            self.b2.Enable(False)
        return
        if len(self.nome.GetValue()) >=7:
            stringa = ""
            for x in range(7):
                stringa += self.nome.GetValue()[x]
            self.nome.SetValue(stringa)
        return
    
    def openBrowser(self, evt):
        webbrowser.open("https://en.wikipedia.org/wiki/Briscola")
        return


# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = Home()
    window.Show()
    app.MainLoop()