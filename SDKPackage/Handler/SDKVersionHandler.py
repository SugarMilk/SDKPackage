# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/6/30.

# todo: GameFriendSDKVersion.h文件路径动态获取

def getOldVersion():
    handler = open("GameFriendSDKVersion.h", "r")
    content = handler.read()
    handler.close()

    startLength = len("#define GameFriendSDKVersion @\"")
    endLength = len(content) - len("\"")

    return content[startLength:endLength]

def getSugguestionVersion():
    temp = getOldVersion().split('.')
    temp[len(temp) - 1] = str(int(temp[len(temp) - 1]) + 1)
    return ".".join(temp)

def setNewVersion(newVersion):
    newString = "#define GameFriendSDKVersion @\"" + newVersion + "\""

    handler = open("GameFriendSDKVersion.h", "w")
    handler.write(newString)
    handler.close()

