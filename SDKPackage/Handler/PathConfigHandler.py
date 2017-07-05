# coding: utf-8 python2.7
# created by mr.huangjian@foxmail.com on 2017/7/3.

import sys
sys.path.append("..")

# import os
# import sys
# sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../"))


import Tool.PersistenceUtil

print help(Tool)


# print sys.path
#
# settingPath = "settingPath.json"
#
# key_projectFilePath = "projectFilePath"
# key_versionFilePath = "versionFilePath"
# key_extraFilePath = "extraFilePath"
# key_exportDirPath = "exportDirPath"
#
# def set(key, value):
#     PersistenceUtil.modifyJson(settingPath, key, value)
#
# def get(key):
#     return PersistenceUtil.getValueFromJson(settingPath, key)
#
#
#
# set("", "")