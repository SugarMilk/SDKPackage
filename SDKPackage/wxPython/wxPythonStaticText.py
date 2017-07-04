# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class StaticText(wx.StaticText):
    """wx.StaticText 文字标签的简单封装"""

    def __init__(self, superView, style=0):
        """
        StaticText 对象初始化
        :param superView: 父视图
        :param style: 控件样式
        """
        wx.StaticText.__init__(self, superView, -1, style=style)

    def setText(self, text):
        """
        设置标签文字
        :param text: 标签文字
        """
        self.SetLabel(text)

    def setMinsize(self, minsize):
        """
        设置控件最小尺寸
        :param minsize: 最小尺寸
        """
        self.SetMinSize(minsize)

    def setSize(self, size):
        """
        设置控件尺寸
        :param size: 尺寸 （width, height）
        """
        self.SetSize(size)

    def setOrigin(self, origin):
        """
        设置控件位置
        :param origin: 位置 （x, y）
        """
        self.SetPosition(origin)

    def setFont(self, font):
        """
        设置控件文字大小
        :param font: 字体大小
        """
        self.SetFont(wx.Font(font, wx.ROMAN, wx.NORMAL, wx.NORMAL))

    def setTextcolor(self, textcolor):
        """
        设置控件文字颜色
        :param textcolor: 文字颜色
        """
        self.SetForegroundColour(textcolor)

    def setBackgroundcolor(self, backgroundcolor):
        """
        设置控件背景颜色
        :param backgroundcolor: 背景颜色
        """
        self.SetBackgroundColour(backgroundcolor)

