import wx, classMazzo, random
from PIL import Image

mazzo = classMazzo.Mazzo().mazzo
#random.shuffle(mazzo)
class provaCARTE(wx.Frame):
    def __init__(self):
        super().__init__(None, title="BRISCOLA | Prova CARTE")
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        grid = wx.FlexGridSizer(rows=4, cols=10, vgap=5, hgap=5) 
        
        for carta in mazzo:
            nomeCarta = carta[1] + str(carta[0]) + ".jpg"
            
            img = Image.open("carte/" + nomeCarta)
            img = img.resize((100,200))
            
            img2 = img.copy()
            wx_Image = wx.Image(img2.size[0], img2.size[1])
            wx_Image.SetData(img2.convert("RGB").tobytes())

            bitmap = wx.Bitmap(wx_Image)
            button = wx.BitmapButton(panel, bitmap=bitmap, name=nomeCarta)
            grid.Add(button, proportion=1, flag=wx.ALL, border=5)
        
        
        panel.SetSizer(vbox)
        self.SetMinSize((500,350))
        vbox.Fit(self)
        self.Centre()

# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = provaCARTE()
    window.Show()
    app.MainLoop()