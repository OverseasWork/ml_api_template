# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 10:55 下午
# @Author  : HuangSir
# @FileName: data_model.py
# @Software: PyCharm
# @Desc: appList + adBook

from pydantic import BaseModel,Field

class AppList(BaseModel):
    """appList"""
    # appName:str = Field(default=None, title='APP名称', example='Shazam',description='app名称')
    packageName:str = Field(title='包名', example='com.shazam.android',description='包名')
    # systemApp:str = Field(default=None, title='系统版本', example='1',description='')
    # versionCode:str =  Field(default=None, title='版本号', example='603001',description='app版本号')
    # firstInstallTime:int = Field(default=None, title='首次安装时间', example=1462084086000,description='首次安装时间戳')
    lastUpdateTime:int = Field(title='最近更新时间', example=1462084086000,description='最近更新时间戳')

class AdList(BaseModel):
    """通讯录"""
    n:str = Field(title='对方姓名', example='ابو مال',description='对方姓名')
    m:str = Field(title='对方号码', example='#10*52072742988790#',description='对方号码')
    # l:str = Field(default=None, title='更新时间', example='2021-10-14 23:40:20',description='yyyy-mm-dd HH:MM:SS')
    # u:str = Field(default=None, title='创建时间', example='2021-10-15 00:23:53',description='yyyy-mm-dd HH:MM:SS')


