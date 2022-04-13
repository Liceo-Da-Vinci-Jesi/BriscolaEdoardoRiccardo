import wx, wx.adv, webbrowser, wx.html2

class RULES(wx.Frame):

    def __init__(self):
        super().__init__(None, title="BRISCOLA | RULES")
        self.panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        vbox = wx.StaticBoxSizer(wx.VERTICAL, self.panel,"RULES")
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        flex = wx.FlexGridSizer(rows=1,cols=2, hgap=5, vgap=5)
        
        regole = wx.StaticText(self.panel, label = "Link: ")
        text = wx.adv.HyperlinkCtrl(self.panel, label="https://en.wikipedia.org/wiki/Briscola")
        text.SetURL("https://en.wikipedia.org/wiki/Briscola")
        self.button = wx.Button(self.panel, label="Back to the lobby")
        
        text.Bind(wx.adv.EVT_HYPERLINK, self.openBrowser)
        
        flex.Add(regole, proportion=1, flag=wx.ALL | wx.ALIGN_CENTRE, border=0)
        flex.Add(text, proportion=1, flag=wx.ALL | wx.EXPAND, border=0)
        flex.AddGrowableCol(1)
        hbox.Add(flex, proportion=1, flag=wx.ALL, border=5)
        vbox.Add(hbox, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(self.button, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        
        
        box.Add(vbox, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
        
        self.panel.SetSizer(box)
        self.SetMinSize((300,150))
        self.SetMaxSize((300,150))
        self.Centre()
        self.Move((1000,300))

    def openBrowser(self, evt):
        webbrowser.open("https://en.wikipedia.org/wiki/Briscola")
#         dial = wx.MessageDialog(None, "Ora della merenda", "RULES", wx.OK)
#         url = "https://en.wikipedia.org/wiki/Briscola"
#         dial.ShowModal()
#         x = wx.html2.WebView.LoadURL("https://en.wikipedia.org/wiki/Briscola")
        return
# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = RULES()
    window.Show()
    app.MainLoop()


