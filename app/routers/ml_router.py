# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 11:35 下午
# @Author  : HuangSir
# @FileName: ml_router.py
# @Software: PyCharm
# @Desc: 模型路由

from fastapi import APIRouter

from app.app.lr_ml.core import lrData
from app.app.lr_ml import lr_ml_main

from app.app.lgb_ml.core import lgbData
from app.app.lgb_ml import lgb_ml_main

ml_router = APIRouter()


@ml_router.post('/v3/lr/score', tags=['标准评分卡'])
async def lr_risk_score(data: lrData):
    data = data.dict()
    res = lr_ml_main(data)
    return res


@ml_router.post('/v3/lgb/score', tags=['集成树模型'])
async def lgb_risk_score(data: lgbData):
    data = data.dict()
    res = lgb_ml_main(data)
    return res
