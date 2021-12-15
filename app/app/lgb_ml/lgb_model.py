# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 10:40 下午
# @Author  : HuangSir
# @FileName: old_cust_model.py
# @Software: PyCharm
# @Desc:

import sys
sys.path.append('..')
import joblib
import pandas as pd
import numpy as np

from utils import load_txt_feature,prob2Score
from app.app.lgb_ml.core import FeatMap,CatMap

class LgbModel:
    """lgb模型"""
    def __init__(self):
        self.lgb_cv = joblib.load('app/app/lgb_ml/static/lgb_model.pkl')
        self.feat = load_txt_feature('app/app/lgb_ml/static/lgbFeat.txt')
        self.cat_feat = load_txt_feature('app/app/lgb_ml/static/lgbCatFeat.txt')
        self.num_feat = list(set(self.feat) - set(self.cat_feat))

    def predict(self, data: dict):
        # 模型置换
        ml_data = {v:data[k] for k,v in FeatMap.items()}
        # 变量排序
        ml_data = {k: [ml_data[k]] for k in self.feat}
        # 入参构造
        ml_df = pd.DataFrame(ml_data)
        # 入参编码
        ml_df = ml_df.replace(CatMap)
        # 预测
        prob = np.nanmean([self.lgb_cv[i].predict(ml_df) for i in range(len(self.lgb_cv))])
        # 评分转换
        score = prob2Score(prob=prob, basePoint=600, PDO=50, odds=20)
        score = int(score)
        return score
