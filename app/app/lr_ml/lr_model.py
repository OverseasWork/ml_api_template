# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 5:35 下午
# @Author  : HuangSir
# @FileName: new_cust_model.py
# @Software: PyCharm
# @Desc: 新客模型

import sys
sys.path.append('..')
import joblib
import pandas as pd
from utils import scorecard_ply
from app.app.lr_ml.core import FeatMap

class LrModel:
    """lr模型"""
    def __init__(self):
        self.lr_card = joblib.load('app/app/lr_ml/static/cardDF.pkl')

    def predict(self, data: dict):
        # 变量置换
        ml_data = {v:[data[k]] for k,v in FeatMap.items()}
        # 数据格式构造
        # print(ml_data)
        ml_df = pd.DataFrame(ml_data)
        # 预测
        score_result = scorecard_ply(dt=ml_df,card=self.lr_card,only_total_score=False)
        score_result = score_result.to_dict(orient='index')[0]
        return score_result