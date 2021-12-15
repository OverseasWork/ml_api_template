# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 9:57 下午
# @Author  : HuangSir
# @FileName: cat_enum.py
# @Software: PyCharm
# @Desc:

# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 9:41 下午
# @Author  : HuangSir
# @FileName: cat_enum.py
# @Software: PyCharm
# @Desc:类别枚举

from enum import Enum

class Gender(str,Enum):
    __doc__ = '性别枚举'
    MALE = 'MALE'
    FEMALE = 'FEMALE'

class MaritalStatus(str,Enum):
    __doc__ = '婚姻枚举'
    WIDOWED = 'WIDOWED'
    MARRIED = 'MARRIED'
    DIVORCED = 'DIVORCED'
    SINGLE = 'SINGLE'

class JobType(str,Enum):
    __doc__ = '工作枚举'
    JOB_FREE = 'JOB_FREE'
    OTHRES = 'OTHRES'
    FULL_TIME = 'FULL_TIME'
    JOB_WAITING = 'JOB_WAITING'
    STUDENT = 'STUDENT'
    PART_TIME = 'PART_TIME'

class WorkingYears(str,Enum):
    __doc__ = '工作年限枚举'
    LT_ONE = 'LT_ONE'
    BTW_ONE_TWO = 'BTW_ONE_TWO'
    BTW_THREE_FIVE = 'BTW_THREE_FIVE'
    OVER_FIVE = 'OVER_FIVE'

class Gyro(str,Enum):
    __doc__ = '是否有陀螺仪枚举'
    t = 't'
    f = 'f'