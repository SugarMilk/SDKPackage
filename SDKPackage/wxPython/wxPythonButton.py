# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class Button(wx.Button):
    """wx.Button 按钮的简单封装"""

    def __init__(self, superView, onClick=None):
        """
        Button 对象初始化
        :param superView: 父视图
        :param onClick: 按钮点击事件的方法绑定
        """
        wx.Button.__init__(self, superView)
        self.Bind(wx.EVT_BUTTON, onClick, self)

    def setOrigin(self, origin):
        """
        设置控件位置
        :param origin: （x, y）
        """
        self.SetPosition(origin)

    def setSize(self, size):
        """
        设置控件大小
        :param size: （width, height）
        """
        self.DoSetSize(self.GetPosition()[0], self.GetPosition()[1], size[0], size[1], 0)

    def setTitle(self, title):
        """
        设置按钮标题
        :param title: 标题
        """
        self.SetLabel(title)

    def setFont(self, font):
        """
        设置按钮标题字体大小
        :param font: 标题字体大小
        """
        self.SetFont(wx.Font(font, wx.ROMAN, wx.NORMAL, wx.NORMAL))

