# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/6/30.

# todo: GameFriendSDKVersion.h文件路径动态获取

import os
import PathConfigHandler

def getOldVersion():
    path = PathConfigHandler.getValueForKey(PathConfigHandler.key_versionFilePath)

    if os.path.exists(path) and os.path.isfile(path):
        handler = open(path, "r")
        content = handler.readline()
        handler.close()

        startLength = len("#define GameFriendSDKVersion @\"")

        if content.endswith("\n"):
            endLength = len(content) - len("\"\n")
        else:
            endLength = len(content) - len("\"")

        return content[startLength:endLength]


def getSugguestionVersion():
    version = getOldVersion()

    if version is not None:
        temp = version.split('.')
        lastIndex = len(temp) - 1
        temp[lastIndex] = str(int(temp[lastIndex]) + 1)
        return ".".join(temp)


def setNewVersion(newVersion):
    path = PathConfigHandler.getValueForKey(PathConfigHandler.key_versionFilePath)

    if os.path.exists(path) and os.path.isfile(path):
        newString = "#define GameFriendSDKVersion @\"" + newVersion + "\""

        handler = open(path, "w")
        handler.write(newString)
        handler.close()

