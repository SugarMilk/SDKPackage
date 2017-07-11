# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/6.

from datetime import *
import os, stat, commands
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
        return "#define GameFriendSDKExtraInfo @\"【时间】：{time}\\n【模式】：{mode}\\n【目的】：{target}\\n【备注】：{note}\\n【版本号】：{version}\""\
            .format(time=self.time, mode=self.mode, target=self.target, note=self.note, version=self.version)

    def startBuild(self):
        self.setNewVersion()    # 第一步：提升版本号
        self.setExtraInfo()     # 第二步：配置额外信息
        self.cleanEnvironment() # 第三步：清空
        self.buildFramework()   # 第四步：编译
        self.exportFramework()  # 第五步：导出

    def setNewVersion(self):
        SDKVersionHandler.setNewVersion(self.version)
        print "提升版本号——已完成\n"

    def setExtraInfo(self):
        path = PathConfigHandler.getValueForKey(PathConfigHandler.key_extraFilePath)

        if os.path.exists(path) and os.path.isfile(path):
            os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            context = open(path, 'w')
            context.write(self.extraString())
            context.close()
        print "配置额外信息——已完成\n"

    def cleanEnvironment(self):
        framework_workspace_dir = os.path.dirname(PathConfigHandler.getValueForKey(
            PathConfigHandler.key_projectFilePath))
        DerivedDataDir = framework_workspace_dir + '/DerivedData'
        statusCode = 0
        if os.path.exists(DerivedDataDir):
            (statusCode, outputContent) = commands.getstatusoutput("rm -rf " + DerivedDataDir)
        if statusCode is 0:
            print "清空环境——已完成\n"

    def buildFramework(self):
        framework_workspace_dir = os.path.dirname(PathConfigHandler.getValueForKey(
            PathConfigHandler.key_projectFilePath))

        workspace_name = os.path.basename(PathConfigHandler.getValueForKey(PathConfigHandler.key_projectFilePath))
        (short_name, extension) = os.path.splitext(workspace_name)
        scheme_name = short_name
        configuration = "Debug" if (self.mode is 0) else "Release"

        location_command = "cd {framework_workspace_dir}\n".format(framework_workspace_dir=framework_workspace_dir)
        build_command = "xcodebuild build -workspace {workspace_name} -scheme {scheme_name} -configuration {configuration} -sdk iphoneos".format(workspace_name=workspace_name, scheme_name=scheme_name, configuration=configuration)

        (buildStatusCode, outputContent) = commands.getstatusoutput(location_command + build_command)

        if buildStatusCode is 0:
            print "编译Framework——已完成\n"


    def exportFramework(self):
        print "导出Framework——已完成\n"
        pass

