import wx
from PIL import Image
class Home(wx.Frame):

    def __init__(self, utente, cpu, nome, colore):
        super().__init__(None, title="BRISCOLA | DECKs")
        panel = wx.Panel(self)
        
        font = wx.Font(20,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        flex = wx.FlexGridSizer(rows = 2, cols = 2, vgap=5, hgap=5)
        name = wx.StaticText(panel, label = nome)
        name.SetBackgroundColour("white")
        name.SetForegroundColour("black")
        name.SetFont(font)
        hname = wx.BoxSizer(wx.HORIZONTAL)
        hname.Add(name, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL)
        
        h1 = wx.BoxSizer(wx.HORIZONTAL)
        h2 = wx.BoxSizer(wx.HORIZONTAL)
        h5 = wx.BoxSizer(wx.HORIZONTAL)
        h6 = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        conta = -1
        for carta in utente:
            conta += 1
            front = "../carte/" + carta[1] + str(carta[0]) + ".jpg"
            img = Image.open(front)
            img = img.resize((50,100))
            wx_Image = wx.Image(img.size[0], img.size[1])
            wx_Image.SetData(img.convert("RGB").tobytes())
            bitmap = wx.Bitmap(wx_Image)
            bmp = wx.BitmapButton(panel, bitmap=bitmap)
            if conta < 10:
                h1.Add(bmp, proportion=0, flag=wx.ALL, border=5)
            else:
                if conta < 20:
                    h2.Add(bmp, proportion=0, flag=wx.ALL, border=5)
                else:
                    if conta < 30:
                        h5.Add(bmp, proportion=0, flag=wx.ALL, border=5)
                    else:
                        h6.Add(bmp, proportion=0, flag=wx.ALL, border=5)
        vbox.Add(h1, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox.Add(h2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox.Add(h5, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox.Add(h6, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        CPU = wx.StaticText(panel, label="CPU")
        CPU.SetBackgroundColour("white")
        CPU.SetForegroundColour("black")
        CPU.SetFont(font)
        hCPU = wx.BoxSizer(wx.HORIZONTAL)
        hCPU.Add(CPU, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE_VERTICAL, border=5)
        

        h3 = wx.BoxSizer(wx.HORIZONTAL)
        h4 = wx.BoxSizer(wx.HORIZONTAL)
        h7 = wx.BoxSizer(wx.HORIZONTAL)
        h8 = wx.BoxSizer(wx.HORIZONTAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        conta = -1
        for carta in cpu:
            conta += 1
            front = "../carte/" + carta[1] + str(carta[0]) + ".jpg"
            img = Image.open(front)
            img = img.resize((50,100))
            wx_Image = wx.Image(img.size[0], img.size[1])
            wx_Image.SetData(img.convert("RGB").tobytes())
            bitmap = wx.Bitmap(wx_Image)
            bmp = wx.BitmapButton(panel, bitmap=bitmap)
            if conta < 10:
                h3.Add(bmp, proportion=0, flag=wx.ALL, border=5)
            else:
                if conta < 20:
                    h4.Add(bmp, proportion=0, flag=wx.ALL, border=5)
                else:
                    if conta < 30:
                        h7.Add(bmp, proportion=0, flag=wx.ALL, border=5)
                    else:
                        h8.Add(bmp, proportion=0, flag=wx.ALL, border=5)
        vbox2.Add(h3, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox2.Add(h4, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox2.Add(h7, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        vbox2.Add(h8, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        flex.Add(hname, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        flex.Add(vbox, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        flex.Add(hCPU, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        flex.Add(vbox2, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=5)
        
        flex.AddGrowableCol(1)
        
        self.SetBackgroundColour(colore)

        v = wx.BoxSizer(wx.VERTICAL)
        v.Add(flex, proportion=1, flag=wx.ALL, border=5)
        
        img = Image.open("../carte/goback.png")
        img = img.resize((75,50))
        wx_Image = wx.Image(img.size[0], img.size[1])
        wx_Image.SetData(img.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_Image)
        self.button = wx.BitmapButton(panel, bitmap = bitmap)
        v.Add(self.button, proportion=0, flag=wx.ALL | wx.ALIGN_RIGHT, border=10)
        
        self.SetBackgroundColour(colore)
        panel.SetSizer(v)
        v.Fit(self)
        res = self.GetSize()
        self.SetMinSize(res)
        self.SetMaxSize(res)
        self.Centre()
# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    nome = "PROVA"
    utente = [[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],]
    cpu = [[4, "Spadi"],[7, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"],[1, "Bastoni"],[10, "Coppe"]]
    window = Home(utente, cpu, nome, "red")
    window.Show()
    app.MainLoop()