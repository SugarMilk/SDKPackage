# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class Textfield(wx.TextCtrl):
    """wx.TextCtrl 文本输入框的简单封装"""

    def __init__(self, superView, style=0):
        """
        Textfield 对象初始化
        :param superView: 父视图
        :param style: 控件样式
        """
        wx.TextCtrl.__init__(self, superView, -1, style=style)

    def setText(self, text):
        """
        设置输入框文本内容
        :param text: 文本内容
        """
        self.SetLabelText(text)

    def getText(self):
        """
        获取输入框文本内容
        :return: 输入框文本内容
        """
        return self.GetValue()

    def setOrigin(self, origin):
        """
        设置控件位置
        :param origin: 位置 （x, y）
        """
        self.SetPosition(origin)

    def setSize(self, size):
        """
        设置控件尺寸
        :param size: 尺寸 （width, height）
        """
        self.SetSize(size)

    def setFont(self, font):
        """
        设置输入框文本字体大小
        :param font: 字体大小
        """
        self.SetFont(wx.Font(font, wx.ROMAN, wx.NORMAL, wx.NORMAL))

    def setTextcolor(self, textcolor):
        """
        设置输入框文字颜色
        :param textcolor: 文字颜色
        """
        self.SetForegroundColour(textcolor)

