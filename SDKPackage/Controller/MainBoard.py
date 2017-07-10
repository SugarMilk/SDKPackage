# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/6.

from wxPython.wxPythonEnum import *
from wxPython.wxPythonStaticText import StaticText
from wxPython.wxPythonBitmapButton import BitmapButton
from wxPython.wxPythonButton import Button
from wxPython.wxPythonTextfield import Textfield
from wxPython.wxPythonRadioBox import RadioBox
import wx
import PathBoard

app = wx.App()
window = wx.Frame(None, title="好玩友SDK导出工具", size=(500, 270), style=wx.CLOSE_BOX | wx.MINIMIZE_BOX)
panel = wx.Panel(window, -1)

""""""""""" 开始搭建界面 """""""""""


# 设置按钮

def onSettingButtonAction(event):
    PathBoard.openConfigBoard(window, "路径配置")

settingButton = BitmapButton(panel, imagePath='../Resource/setting.png', onClick=onSettingButtonAction)
settingButton.setOrigin((450, 10))

# 模式

modeLabel = StaticText(panel)
modeLabel.setFont(16)
modeLabel.setText("模式： ")
modeLabel.setOrigin((20, 20))

# 模式单选

modeRadioList = ["Debug", "Release"]

modeRadio = RadioBox(panel, modeRadioList)
modeRadio.SetPosition((70, 15))

# 目的

targetLabel = StaticText(panel)
targetLabel.setFont(16)
targetLabel.setText("目的： ")
targetLabel.setOrigin((20, 60))

# 目的单选

targetRadioList = [u"接入游戏自测", u"给SDK质检测试", u"给游戏质检测试"]

targetRadio = RadioBox(panel, targetRadioList)
targetRadio.SetPosition((70, 55))

# 备注

noteLabel = StaticText(panel)
noteLabel.setFont(16)
noteLabel.setText("备注： ")
noteLabel.setOrigin((20, 102))

# 备注输入框

noteTf = Textfield(panel)
noteTf.setOrigin((73, 100))
noteTf.setSize((370, 25))
noteTf.setFont(15)

# 旧版本号

oldVersionLabel = StaticText(panel)
oldVersionLabel.setFont(16)
oldVersionLabel.setText("旧版本号： ")
oldVersionLabel.setOrigin((20, 143))

# 旧版本号输入框

oldVersionTf = Textfield(panel, style=textFieldType.readonly)
oldVersionTf.setOrigin((100, 140))
oldVersionTf.setSize((120, 25))
oldVersionTf.setFont(16)
oldVersionTf.setTextColor("gray")
# oldVersionTf.text(SDKVersionManager.get_old_version())

# 新版本号

newVersionLabel = StaticText(panel)
newVersionLabel.setFont(16)
newVersionLabel.setText("新版本号： ")
newVersionLabel.setOrigin((240, 143))

# 新版本号输入框

newVersionTf = Textfield(panel)
newVersionTf.setOrigin((323, 140))
newVersionTf.setSize((120, 25))
newVersionTf.setFont(16)

# oldVersion = SDKVersionManager.get_old_version()
# temp = oldVersion.split('.')
# temp[len(temp) - 1] = str(int(temp[len(temp) - 1]) + 1)
# newVersion = ".".join(temp)
#
# newVersionTf.text(newVersion)

# 运行Demo工程

def onRunButtonAction(event):
    print "Run..."

runButton = Button(panel, onClick=onRunButtonAction)
runButton.setOrigin((25, 183))
runButton.setSize((190, 35))
runButton.setFont(17)
runButton.setTitle("\n运行Demo工程\n")

# 编译导出Framework

def onBuildButtonAction(event):

    mode = modeRadioList[modeRadio.getselect()].encode('utf-8')
    target = targetRadioList[targetRadio.getselect()].encode('utf-8')
    note = noteTf.gettext().encode('utf-8')
    version = newVersionTf.gettext().encode('utf-8')

    # buildHandler = BuildHandler(mode, target, note, version)
    # confirmDialog = wx.MessageDialog(panel, "", "编译导出前请确认无误",style=wx.YES_NO)

    # if confirmDialog.ShowModal() == wx.ID_YES:
    #     buildHandler.startBuild()


buildButton = Button(panel, onClick=onBuildButtonAction)
buildButton.setOrigin((240, 183))
buildButton.setSize((200, 35))
buildButton.setFont(17)
buildButton.setTitle("\n编译导出Framework\n")



""""""""""" 结束搭建界面 """""""""""

window.Show()
app.MainLoop()
