# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/2.

import os
import json
import pickle

def writeJson(filePath, dictionary):
    """
    写入字典数据到某个文件
    :param filePath: 要写入文件的路径
    :param dictionary: 要写入的字典数据
    """
    context = open(filePath, 'w')
    json.dump(dictionary, context)
    context.close()

def readJson(filePath):
    """
    从某个文件中读取字典数据
    :param filePath: 要读取的文件路径
    :return: 读取到的字典数据
    """
    if not os.path.exists(filePath):
        writeJson(filePath, {})
    context = open(filePath, 'r')
    content = json.load(context)
    context.close()
    return content

def getValueFromJson(filePath, key):
    """
    从某个文件中读取字典数据中某个键的值
    :param filePath: 要读取的文件路径
    :param key: 键
    :return: 值
    """
    return readJson(filePath).get(key, "")

def modifyJson(filePath, key, value):
    """
    修改某个文件的字典数据的某个key-value
    :param filePath: 要修改的文件路径
    :param key: 要修改的字典数据中的key
    :param value: 要修改的字典数据中的key对应的value
    """
    dictionary = readJson(filePath)
    dictionary[key] = value
    writeJson(filePath, dictionary)


def writePickle(filePath, instance):
    """
    写入对象到Pickle文件中
    :param filePath: pickle文件路径
    :param instance: 要写入的对象
    """
    context = open(filePath, 'w')
    pickle.dump(instance, context)
    context.close()

def readPickle(filePath):
    """
    从Pickle文件中读取对象
    :param filePath: pickle文件路径
    :return: 要读取的对象
    """
    if not os.path.exists(filePath):
        return
    context = open(filePath, 'r')
    instance = pickle.load(context)
    context.close()
    return instance


