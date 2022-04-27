from briscola import gioco
import wx

def run():
    app = wx.App()
    a = gioco.Game()
    return app.MainLoop()

