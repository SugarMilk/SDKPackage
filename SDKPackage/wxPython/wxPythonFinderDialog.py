# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

def chooseDirDialog(superView, title="", onSelected=None):
    """
    选择文件夹目录的弹框
    :param superView: 父视图
    :param title: 弹框标题
    :param onSelected: 回调选中的目录路径
    """
    dialog = wx.DirDialog(superView, message=title)
    if dialog.ShowModal() == wx.ID_OK:
        if onSelected:
            onSelected(dialog.GetPath())
    dialog.Destroy()


def chooseFileDialog(superView, title="", onSelected=None):
    """
    选择文件的弹框
    :param superView: 父视图
    :param title: 弹框标题
    :param onSelected: 回调选中的文件路径
    """
    dialog = wx.FileDialog(superView, message=title)
    if dialog.ShowModal() == wx.ID_OK:
        if onSelected:
            onSelected(dialog.GetPath())
    dialog.Destroy()

