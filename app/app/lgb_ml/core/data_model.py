# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 3:58 下午
# @Author  : HuangSir
# @FileName: data_model.py
# @Software: PyCharm
# @Desc:

from pydantic import BaseModel, Field
from typing import List
from .cat_enum import (Gender,MaritalStatus,JobType,WorkingYears,Gyro)
from app.app.applist_ml.core import AppList, AdList
from datetime import datetime

class DatalgbMl(BaseModel):
    """数据模型"""
    # ----------  基础信息 ------------------------
    gender: Gender = Field(title='性别', example='MALE', description='性别:MALE,FEMALE')

    age:int = Field(title='年龄',example=25,
                    description='客户年龄,计算逻辑:t_personal_info,extract(year FROM age(t.create_time,t.ktp_date_of_birth))')

    maritalStatus:MaritalStatus = Field(title='婚姻',example='SINGLE',
                              description='婚姻:WIDOWED,MARRIED,DIVORCED,SINGLE')

    jobType:JobType = Field(title='职业类型',example='OTHRES',
                        description='职业类型:JOB_FREE,OTHRES,FULL_TIME,JOB_WAITING,STUDENT,PART_TIME')

    workingYears:WorkingYears = Field(title='工作年限',example='LT_ONE',
                             description='工作年限:LT_ONE,BTW_ONE_TWO,BTW_THREE_FIVE,OVER_FIVE')

    # ----------  设备信息 ------------------------
    gyro:Gyro = Field(title='是否有陀螺仪',example='t',description='是否有陀螺仪:t,f; x_equipment.gyro')

    remainingMemory:int = Field(title='可用内存',example=671830016,description='可用内存;x_equipment.remaining_memory')

    systemVersion:int = Field(title='系统版本号',example=30,description='系统版本号,x_equipment.system_version')

    length:int = Field(title='屏幕长度',example=1920,description='屏幕长度,x_equipment.length')

    remainingBattery:int = Field(title='剩余电量',example=71,description='剩余电量,x_equipment.remaining_battery')

    # ----------  通讯录信息 ------------------------
    concatNum:int = Field(title='通讯录有效个数',example=100,description='通讯录有效个数')

    concatApplyNum:int = Field(default=0,title='通讯录下单客户数',example=2,description='手机号关联订单, 通讯录中下单客户数')

    concatApplyPassNum:int = Field(default=0,title='通讯录下单成功的客户数',example=1,description='手机号关联订单, 通讯录中下单成功的客户数')

    concatApplyPassOdNum:int = Field(default=0,title='通讯录手机号关联订单数',example=0,description='通讯录手机号关联订单数')

    concatApplyOverdueNum:int = Field(default=0,title='通讯录逾期客户数',example=0,description='通讯录手机号关联逾期订单的手机号个数')

    concatApplyRatio:float = Field(default=0.0,title='通讯录申请占比',example=0.2,description='通讯录中下单客户数*100/通讯录有效个数')

    concatRegisterRatio:float = Field(default=0.0,title='通讯录注册占比',example=0.1,description='通讯录中注册客户数*100/通讯录有效个数')

    # ----------  其他信息 ------------------------
    loginTotalSeconds:int = Field(title='登录总时长',example=1218552,description='变量在V2版评分卡已开发,login_total_seconds')

    chooseDisburseCostSeconds:int = Field(title='选择支付方式时长',example=36,description='变量在V2版评分卡已开发, choose_disburse_cost_seconds')

    applyTime:str = Field(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),title='下单时间',example='2021-06-25 09:39:24',
                          description='下单时间戳,格式:yyyy-mm-dd HH:MM:SS')

    appList: List[AppList] = Field(default=..., title='appList', description='AppList数据模型')

    addList: List[AdList] = Field(default=..., title='通讯录',description='AdList数据模型')

class lgbData(BaseModel):
    customerId: int = Field(title='客户ID', example=134671)
    loanAppId: int = Field(title='交易订单号', example=2111051703363537)
    data: DatalgbMl = Field(default=..., title='lgb模型入参')
