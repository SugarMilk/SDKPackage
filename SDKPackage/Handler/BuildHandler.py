# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/6.

from datetime import *
import os, stat, commands
import SDKVersionHandler
import PathConfigHandler
from wxPython.wxPythonTextfield import Textfield

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

    def setConsoleView(self, textView):
        self.console = textView

    def startBuild(self):
        self.setNewVersion()    # 第一步：提升版本号
        self.setExtraInfo()     # 第二步：配置额外信息
        self.cleanEnvironment() # 第三步：清空
        self.buildFramework()   # 第四步：编译Framework
        self.processFramework()   # 第五步：加工Framework
        self.exportFramework()  # 第五步：导出Framework

    def setNewVersion(self):
        self.console.appendText("提升版本号....")
        SDKVersionHandler.setNewVersion(self.version)
        self.console.appendText("   已完成 \n")

    def setExtraInfo(self):
        self.console.appendText("配置额外信息....")
        path = PathConfigHandler.getValueForKey(PathConfigHandler.key_extraFilePath)

        if os.path.exists(path) and os.path.isfile(path):
            os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            context = open(path, 'w')
            context.write(self.extraString())
            context.close()
        self.console.appendText("   已完成 \n")

    def cleanEnvironment(self):
        self.console.appendText("清空缓存文件....")
        framework_workspace_dir = os.path.dirname(PathConfigHandler.getValueForKey(
            PathConfigHandler.key_projectFilePath))
        DerivedDataDir = framework_workspace_dir + '/DerivedData'
        if os.path.exists(DerivedDataDir):
            commands.getstatusoutput("rm -rf " + DerivedDataDir)
        self.console.appendText("   已完成 \n")

    def buildFramework(self):
        self.console.appendText("编译Framework....")
        framework_workspace_dir = os.path.dirname(PathConfigHandler.getValueForKey(
            PathConfigHandler.key_projectFilePath))

        workspace_name = os.path.basename(PathConfigHandler.getValueForKey(PathConfigHandler.key_projectFilePath))
        (short_name, extension) = os.path.splitext(workspace_name)
        scheme_name = short_name
        configuration = "Debug" if (self.mode is 1) else "Release"

        location_command = "cd {framework_workspace_dir}\n".format(framework_workspace_dir=framework_workspace_dir)
        build_command = "xcodebuild build -workspace {workspace_name} -scheme {scheme_name} -configuration {configuration} -sdk iphoneos".format(workspace_name=workspace_name, scheme_name=scheme_name, configuration=configuration)

        (buildStatusCode, outputContent) = commands.getstatusoutput(location_command + build_command)

        if buildStatusCode is 0:
            self.console.appendText("   已完成 \n")
        else:
            self.console.appendText("   Framework失败编译!!!!! \n")

    def processFramework(self):
        self.console.appendText("加工Framework....")
        framework_workspace_dir = os.path.dirname(PathConfigHandler.getValueForKey(
            PathConfigHandler.key_projectFilePath))

        command = """\
#!/usr/bin/env bash
cd {framework_workspace_dir}/DerivedData/Build/Products/{configuration}-iphoneos/
shopt -s extglob
rm -rf {otherLibraries}
cd GameFriendSDK.framework
rm -rf {otherUnavailableFile}"""\
            .format(framework_workspace_dir=framework_workspace_dir, configuration=self.mode,
                    otherLibraries="!(GameFriendSDK.framework)".decode('utf-8'),
                    otherUnavailableFile="!(GameFriendSDK|Headers|SDKResource.bundle)".decode('utf-8'))

        handler = open('../Resource/temp.sh', 'w')
        handler.write(command)
        handler.close()

        (processStatusCode, outputContent) = commands.getstatusoutput("sh ../Resource/temp.sh")

        if processStatusCode is 0:
            self.console.appendText("   已完成 \n")
        else:
            self.console.appendText("   失败 \n")


    def exportFramework(self):
        self.console.appendText("导出Framework....")

        exportDir = PathConfigHandler.getValueForKey(PathConfigHandler.key_exportDirPath)
        folderName = "GameFriendSDK DL {datetime}".format(datetime=self.time[5:])
        folderName = folderName.replace(" ", "\ ")
        folderName = folderName.replace(":", "-")
        folderPath = exportDir + '/' + folderName
        mkdirCommand = "mkdir {folderPath}".format(folderPath=folderPath)

        (mkdirStatusCode, outputContent) = commands.getstatusoutput(mkdirCommand)

        if mkdirStatusCode is 0:
            framework_workspace_dir = os.path.dirname(PathConfigHandler.getValueForKey(
                PathConfigHandler.key_projectFilePath))
            configuration = "Debug" if (self.mode is 1) else "Release"

            frameworkPath = "{framework_workspace_dir}/DerivedData/Build/Products/{configuration}-iphoneos/GameFriendSDK.framework".format(
                framework_workspace_dir=framework_workspace_dir,configuration=configuration)

            bundlePath = frameworkPath + "/SDKResource.bundle"

            moveBundleCommand = "mv {sourcePath} {destinationPath}".format(sourcePath=bundlePath, destinationPath=folderPath)

            (moveBundleStatusCode, outputContent) = commands.getstatusoutput(moveBundleCommand)

            if moveBundleStatusCode is 0:
                moveFrameworkCommand = "mv {sourcePath} {destinationPath}".format(sourcePath=frameworkPath,
                                                                                  destinationPath=folderPath)

                (moveFrameworkStatusCode, outputContent) = commands.getstatusoutput(moveFrameworkCommand)

                if moveFrameworkStatusCode is 0:
                    framework_workspace_dir = os.path.dirname(PathConfigHandler.getValueForKey(
                        PathConfigHandler.key_projectFilePath))
                    DerivedDataDir = framework_workspace_dir + '/DerivedData'
                    commands.getstatusoutput("rm -rf %s" % DerivedDataDir)

        self.console.appendText("   已完成 \n")

        self.console.appendText("\n٩(●˙▿˙●)۶…  GOOD JOB !! 你牛X  ⋆ฺ(◍•ᴗ•◍)❤")