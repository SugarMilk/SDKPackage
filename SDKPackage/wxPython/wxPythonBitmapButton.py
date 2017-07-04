# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class BitmapButton(wx.BitmapButton):
    """wx.BitmapButton 图片按钮的简单封装"""

    def __init__(self, superView, imagePath, onClick=None):
        """
        BitmapButton 对象初始化
        :param superView: 父视图
        :param imagePath: 图片路径
        :param onClick: 按钮点击事件的方法绑定
        """
        image = wx.Image(imagePath, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.BitmapButton.__init__(self, superView, -1, image)
        self.Bind(wx.EVT_BUTTON, onClick, self)

    def setOrigin(self, origin):
        """
        设置控件位置
        :param origin: （x, y）
        """
        self.SetPosition(origin)

