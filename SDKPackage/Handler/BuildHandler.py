# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/6.

from datetime import *
import os
import SDKVersionHandler
import PathConfigHandler

class BuildHandler:

    def __init__(self, mode="", target="", note="", version=""):
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.mode = mode
        self.target = target
        self.note = note
        self.version = version

    def confirmMessage(self):
        return "【时间】：{time}\n【模式】：{mode}\n【目的】：{target}\n【备注】：{note}\n【版本号】：{version}"\
            .format(time=self.time, mode=self.mode, target=self.target, note=self.note, version=self.version)

    def extraString(self):
        return "#define extra @\"【时间】：{time}\\n【模式】：{mode}\\n【目的】：{target}\\n【备注】：{note}\\n【版本号】：{version}\""\
            .format(time=self.time, mode=self.mode, target=self.target, note=self.note, version=self.version)

    def startBuild(self):
        self.setNewVersion()    # 第一步：提升版本号
        self.setExtraInfo()     # 第二步：配置额外信息
        self.cleanEnvironment() # 第三步：清空
        self.buildFramework()   # 第四步：编译
        self.exportFramework()  # 第五步：导出

    def setNewVersion(self):
        SDKVersionHandler.setNewVersion(self.version)

    def setExtraInfo(self):
        path = PathConfigHandler.getValueForKey(PathConfigHandler.key_extraFilePath)

        if os.path.exists(path) and os.path.isfile(path):
            context = open(path, 'w')
            context.write(self.extraString())
            context.close()

    def cleanEnvironment(self):
        print "清空环境"
        pass

    def buildFramework(self):
        print "编译Framework"
        pass

    def exportFramework(self):
        print "导出Framework"
        pass

