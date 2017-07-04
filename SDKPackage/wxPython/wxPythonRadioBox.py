# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class RadioBox(wx.RadioBox):
    """wx.RadioBox 单选按钮组的简单封装"""

    def __init__(self, superView, choices, onRadioBox=None):
        """
        RadioBox 对象初始化
        :param superView: 父视图
        :param choices: 单选按钮组列表，["a", "b", "c"]
        :param onRadioBox: 单选按钮选中事件回调
        """
        wx.RadioBox.__init__(self, superView, choices=choices)
        self.Bind(wx.EVT_RADIOBOX, onRadioBox, self)

    def setSelectedIndex(self, index):
        """
        设置被选中的单选按钮索引
        :param index: 单选按钮索引
        """
        self.SetSelection(index)

    def getSelectedIndex(self):
        """
        返回被选中的单选按钮索引
        :return: 被选中的单选按钮索引
        """
        return self.GetSelection()

