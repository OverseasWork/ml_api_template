# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 10:04 下午
# @Author  : HuangSir
# @FileName: feat_map.py
# @Software: PyCharm
# @Desc:

FeatMap = {
    'gender':'gender',
    'gyro':'是否有陀螺仪',
    'maritalStatus':'marital_status',
    'jobType':'job_type',
    'concatApplyRatio':'通讯录申请占比',
    'remainingMemory':'可用内存',
    'workingYears':'working_years',
    'systemVersion':'安卓版本号',
    'concatRegisterRatio':'通讯录注册占比',
    'age':'age',
    'loginTotalSeconds':'login_total_seconds',
    'chooseDisburseCostSeconds':'choose_disburse_cost_seconds',
    'length':'屏幕长度',
    'prob':'prob',
    'remainingBattery':'剩余电量',
    'concatNum':'通讯录个数',

    # 'concatApplyNum':'concat_apply_num',
    # 'concatApplyPassNum':'concat_apply_pass_num',
    # 'concatApplyPassOdNum':'concat_apply_pass_od_num',
    # 'concatApplyOverdueNum':'concat_apply_overdue_num'
}

CatMap = {
    'children_number':{'ZERO':0,'ONE':1,'TWO':2,'THREE':3,'OVER_THREE':4}, # num
    'job_type':{'JOB_FREE':0,'OTHRES':0,'FULL_TIME':1,'PART_TIME':2,'STUDENT':2,'JOB_WAITING':2},
    'gender':{'FEMALE':0,'MALE':1},
    'working_years':{'LT_ONE':0,'BTW_ONE_TWO':1,'BTW_THREE_FIVE':2,'OVER_FIVE':3}, # num
    '是否有陀螺仪':{'f':0,'t':1},
    'marital_status':{'SINGLE':0,'DIVORCED':0,'WIDOWED':1,'MARRIED':1}
}












