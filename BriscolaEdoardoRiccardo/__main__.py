import sys
sys.path.append("BriscolaEdoardoRiccardo/")

import classMazzo, classGiocataCPU, finestraMazzi, Gioco, Lobby, Risultati, Setting, Tabellone
import wx

app = wx.App()
a = Gioco.Game()
app.MainLoop()
