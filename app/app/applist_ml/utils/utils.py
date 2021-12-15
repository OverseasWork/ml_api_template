# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 7:05 下午
# @Author  : HuangSir
# @FileName: utils.py
# @Software: PyCharm
# @Desc:

import sys

sys.path.append('..')
import datetime
import time


def load_txt_feat(file: str):
    """加载txt"""
    with open(file, 'r') as f:
        feature = f.read().split('\n')
        feature = [i for i in feature if i]
        return feature


def stamp_format(tm):
    te = time.strftime("%Y-%m-%d", time.localtime(int(str(tm)[:10])))
    if te > datetime.datetime.strftime(datetime.datetime.today(), '%Y-%m-%d') or te < '2000-1-1':
        return '1990-1-1'
    else:
        return te
