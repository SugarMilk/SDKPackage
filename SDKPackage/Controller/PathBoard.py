# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/6.

from wxPython.wxPythonEnum import *
from wxPython.wxPythonStaticText import StaticText
from wxPython.wxPythonButton import Button
from wxPython.wxPythonTextfield import Textfield
from wxPython.wxPythonFinderDialog import *
from Handler import PathConfigHandler

def openConfigBoard(superView, title):
    dialog = wx.Dialog(parent=superView, title=title, size=(940, 360))
    dialog.SetPosition((superView.GetPosition()[0], superView.GetPosition()[1] + 20))
    panel = wx.Panel(dialog)

    # Framework项目路径

    projectPathLabel = StaticText(panel)
    projectPathLabel.setFont(16)
    projectPathLabel.setText("Framework项目路径")
    projectPathLabel.setOrigin((20, 20))

    def onProjectPathButtonAction(event):
        chooseFileDialog(panel, onSelected=onProjectPathSelected)

    projectPathButton = Button(panel, onClick=onProjectPathButtonAction)
    projectPathButton.setOrigin((830, 20))
    projectPathButton.setTitle("选择")

    projectPathTf = Textfield(panel, style=textFieldType.readonly)
    projectPathTf.setOrigin((20, 45))
    projectPathTf.setSize((895, 25))
    projectPathTf.setTextColor("gray")
    projectPathTf.setText(PathConfigHandler.getValueForKey(PathConfigHandler.key_projectFilePath))

    def onProjectPathSelected(path):
        projectPathTf.setText(path)

    # SDK版本号文件路径

    versionPathLabel = StaticText(panel)
    versionPathLabel.setFont(16)
    versionPathLabel.setText("SDK版本号文件路径")
    versionPathLabel.setOrigin((20, 80))

    def onVersionPathButtonAction(event):
        chooseFileDialog(panel, onSelected=onVersionPathSelected)

    versionPathButton = Button(panel, onClick=onVersionPathButtonAction)
    versionPathButton.setOrigin((830, 80))
    versionPathButton.setTitle("选择")

    versionPathTf = Textfield(panel, style=textFieldType.readonly)
    versionPathTf.setOrigin((20, 105))
    versionPathTf.setSize((895, 25))
    versionPathTf.setTextColor("gray")
    versionPathTf.setText(PathConfigHandler.getValueForKey(PathConfigHandler.key_versionFilePath))

    def onVersionPathSelected(path):
        versionPathTf.setText(path)

    # 额外信息文件路径

    extraPathLabel = StaticText(panel)
    extraPathLabel.setFont(16)
    extraPathLabel.setText("额外信息文件路径")
    extraPathLabel.setOrigin((20, 140))

    def onExtraPathButtonAction(event):
        chooseFileDialog(panel, onSelected=onExtraPathSelected)

    extraPathButton = Button(panel, onClick=onExtraPathButtonAction)
    extraPathButton.setOrigin((830, 140))
    extraPathButton.setTitle("选择")

    extraPathTf = Textfield(panel, style=textFieldType.readonly)
    extraPathTf.setOrigin((20, 165))
    extraPathTf.setSize((895, 25))
    extraPathTf.setTextColor("gray")
    extraPathTf.setText(PathConfigHandler.getValueForKey(PathConfigHandler.key_extraFilePath))

    def onExtraPathSelected(path):
        extraPathTf.setText(path)

    # Framework导出目录

    exportPathLabel = StaticText(panel)
    exportPathLabel.setFont(16)
    exportPathLabel.setText("Framework导出目录")
    exportPathLabel.setOrigin((20, 200))

    def onExportPathButtonAction(event):
        chooseDirDialog(panel, onSelected=onExportPathSelected)

    exportPathButton = Button(panel, onClick=onExportPathButtonAction)
    exportPathButton.setOrigin((830, 200))
    exportPathButton.setTitle("选择")

    exportPathTf = Textfield(panel, style=textFieldType.readonly)
    exportPathTf.setOrigin((20, 225))
    exportPathTf.setSize((895, 25))
    exportPathTf.setTextColor("gray")
    exportPathTf.setText(PathConfigHandler.getValueForKey(PathConfigHandler.key_exportDirPath))

    def onExportPathSelected(path):
        exportPathTf.setText(path)

    # 保存配置

    def onSaveButtonAction(event):
        PathConfigHandler.setKeyWithValue(PathConfigHandler.key_projectFilePath, projectPathTf.getText())
        PathConfigHandler.setKeyWithValue(PathConfigHandler.key_versionFilePath, versionPathTf.getText())
        PathConfigHandler.setKeyWithValue(PathConfigHandler.key_extraFilePath, extraPathTf.getText())
        PathConfigHandler.setKeyWithValue(PathConfigHandler.key_exportDirPath, exportPathTf.getText())
        dialog.Close()

    saveButton = Button(panel, onClick=onSaveButtonAction)
    saveButton.setOrigin((200, 270))
    saveButton.setSize((200, 30))
    saveButton.setFont(15)
    saveButton.setTitle("\n保存配置\n")

    # 取消关闭

    def onCancelButtonAction(event):
        dialog.Close()

    cancelButton = Button(panel, onClick=onCancelButtonAction)
    cancelButton.setOrigin((500, 270))
    cancelButton.setSize((200, 30))
    cancelButton.setFont(15)
    cancelButton.setTitle("\n取消关闭\n")

    dialog.ShowModal()

