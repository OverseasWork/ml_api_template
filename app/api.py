# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 8:49 下午
# @Author  : HuangSir
# @FileName: api.py
# @Software: PyCharm
# @Desc:

from .routers import risk_router_init
from fastapi import FastAPI


def create_app():
    app = FastAPI(title='风险评分模型',
                  description="""标准评分卡,集成树模型同时调,入参类别变量务必根据枚举值输入,否则报错. \n
                  标准评分卡模型参数规范详情:  lrData\n
                  集成树模型参数规范详情:  lgbData
                  """,
                  version='3.0')
    risk_router_init(app)
    return app
