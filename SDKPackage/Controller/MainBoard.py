# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/6.

import wx
import PathBoard

app = wx.App()
window = wx.Frame(None, title="好玩友SDK导出工具", size=(500, 270), style=wx.CLOSE_BOX | wx.MINIMIZE_BOX)
panel = wx.Panel(window, -1)


PathBoard.openConfigBoard(window, "路径配置")

window.Show()
app.MainLoop()
