# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 10:26 下午
# @Author  : HuangSir
# @FileName: applist_model.py
# @Software: PyCharm
# @Desc: appList模型主程序

import sys

sys.path.append('..')

from conf.log_config import log
import pandas as pd
import numpy as np
from datetime import datetime
import joblib
import re
import warnings

warnings.filterwarnings('ignore')

from app.app.applist_ml.utils import load_txt_feat, stamp_format


class AppListML:
    """appList模型主程序"""

    def __init__(self):
        self.file = 'app/app/applist_ml/static/'
        self.model = joblib.load(self.file + 'dc_er_app_add_1120.pkl')
        self.feat = load_txt_feat(self.file + 'in_ml_col_1120.txt')
        self.comp = pd.read_excel(self.file + 'comp.xlsx', names=['package', 'name'])

    def __base_feat(self, data: dict):
        """基础变量"""
        app_list = data['appList']
        add_list = data['addList']

        df = pd.DataFrame(app_list)
        df['lastTime'] = df['lastUpdateTime'].apply(stamp_format)

        df['apply_time'] = data['applyTime']

        df['apply_time'] = pd.to_datetime(df['apply_time'])
        df['lastTime'] = pd.to_datetime(df['lastTime'])
        self_df = df[df.lastTime > datetime(2010, 1, 1)]

        day_tag = pd.DataFrame(pd.cut((self_df['apply_time'] - self_df['lastTime']).dt.days,
                                      bins=[0, 1, 3, 7, 15, 30, 60, np.inf], include_lowest=True,
                                      labels=['self_1', 'self_3', 'self_7', 'self_15', 'self_30', 'self_60',
                                              'self_90']).value_counts()).T
        day_tag.columns = day_tag.columns.tolist()
        self_comp = df[df.packageName.isin(self.comp.package)]

        comp_day_tag = pd.DataFrame(pd.cut((self_comp['apply_time'] - self_comp['lastTime']).dt.days,
                                           bins=[0, 1, 3, 7, 15, 30, 60, np.inf], include_lowest=True,
                                           labels=['comp_1', 'comp_3', 'comp_7', 'comp_15', 'comp_30', 'comp_60',
                                                   'comp_90']).value_counts()).T

        comp_day_tag.columns = comp_day_tag.columns.tolist()

        # day_tag['loan_app_id'] = data['loanAppId']
        day_tag['apply_time'] = data['applyTime']

        day_tag['all_self_cnt'] = self_df.shape[0]
        day_tag['all_self_comp_cnt'] = self_comp.shape[0]
        day_tag['all_cnt'] = df.shape[0]

        add_df = pd.DataFrame(add_list)
        add_df['contain_chs'] = add_df['n'].str.extract(r'([\u4e00-\u9fa5]+)')
        lxr_num = add_df.shape[0]
        chs_lxr_num = add_df[~add_df.contain_chs.isnull()].shape[0]
        cnt = 0
        for j in add_df.m.tolist():
            if re.match('^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$', '%s' % j):
                cnt += 1

        day_tag[
            ['lxr_num', 'chs_lxr_num', 'cnt', 'concat_apply_num', 'concat_apply_pass_num', 'concat_apply_pass_od_num',
             'concat_apply_overdue_num']] = [lxr_num, chs_lxr_num, cnt, data['concatApplyNum'],
                                             data['concatApplyPassNum'], data['concatApplyPassOdNum'],
                                             data['concatApplyOverdueNum']]

        all_tag = pd.concat([day_tag, comp_day_tag], axis=1)
        return all_tag

    def __trend_feat(self, base_feat: pd.DataFrame):
        """趋势变量"""
        for i in [1, 3, 7, 15, 30, 60, 90]:
            base_feat['self_%s_pct' % i] = base_feat['self_%s' % i] / base_feat['all_self_cnt']
            base_feat['self_%s_all_pct' % i] = base_feat['self_%s' % i] / base_feat['all_cnt']
            base_feat['comp_%s_pct' % i] = base_feat['comp_%s' % i] / base_feat['all_self_comp_cnt']

        base_feat['all_self_pct'] = base_feat['all_self_cnt'] / base_feat['all_cnt']
        base_feat['all_self_comp_pct'] = base_feat['all_self_comp_cnt'] / base_feat['all_cnt']

        base_feat['self_3_all'] = base_feat['self_1'] + base_feat['self_3']
        base_feat['self_7_all'] = base_feat['self_1'] + base_feat['self_3'] + base_feat['self_7']

        base_feat['self_15_all'] = base_feat['self_1'] + base_feat['self_3'] + base_feat['self_7'] + base_feat[
            'self_15']

        base_feat['self_30_all'] = base_feat['self_1'] + base_feat['self_3'] + base_feat['self_7'] + base_feat[
            'self_15'] + base_feat['self_30']

        base_feat['self_60_all'] = base_feat['self_1'] + base_feat['self_3'] + base_feat['self_7'] + base_feat[
            'self_15'] + base_feat['self_30'] + base_feat['self_60']

        base_feat['self_90_all'] = base_feat['self_1'] + base_feat['self_3'] + base_feat['self_7'] + base_feat[
            'self_15'] + base_feat['self_30'] + base_feat['self_60'] + base_feat['self_90']

        base_feat['self_3_1'] = base_feat['self_3'] - base_feat['self_1']
        base_feat['self_7_3'] = base_feat['self_7'] - base_feat['self_3']
        base_feat['self_15_7'] = base_feat['self_15'] - base_feat['self_7']
        base_feat['self_30_15'] = base_feat['self_30'] - base_feat['self_15']
        base_feat['self_60_30'] = base_feat['self_60'] - base_feat['self_30']
        base_feat['comp_3_all'] = base_feat['comp_1'] + base_feat['comp_3']

        base_feat['comp_7_all'] = base_feat['comp_1'] + base_feat['comp_3'] + base_feat['comp_7']

        base_feat['comp_15_all'] = base_feat['comp_1'] + base_feat['comp_3'] + base_feat['comp_7'] + base_feat[
            'comp_15']

        base_feat['comp_30_all'] = base_feat['comp_1'] + base_feat['comp_3'] + base_feat['comp_7'] + base_feat[
            'comp_15'] + base_feat['comp_30']

        base_feat['comp_60_all'] = base_feat['comp_1'] + base_feat['comp_3'] + base_feat['comp_7'] + base_feat[
            'comp_15'] + base_feat['comp_30'] + base_feat['comp_60']

        base_feat['comp_90_all'] = base_feat['comp_1'] + base_feat['comp_3'] + base_feat['comp_7'] + base_feat[
            'comp_15'] + base_feat['comp_30'] + base_feat['comp_60'] + base_feat['comp_90']

        base_feat['comp_3_all_pct'] = base_feat['comp_3_all'] / base_feat['self_3_all']
        base_feat['comp_7_all_pct'] = base_feat['comp_7_all'] / base_feat['self_7_all']
        base_feat['comp_15_all_pct'] = base_feat['comp_15_all'] / base_feat['self_15_all']
        base_feat['comp_30_all_pct'] = base_feat['comp_30_all'] / base_feat['self_30_all']
        base_feat['comp_60_all_pct'] = base_feat['comp_60_all'] / base_feat['self_60_all']
        base_feat['comp_90_all_pct'] = base_feat['comp_90_all'] / base_feat['self_90_all']
        base_feat['chs_lxr_num_pct'] = base_feat['chs_lxr_num'] / base_feat['lxr_num']
        base_feat['chs_nb_num_pct'] = base_feat['cnt'] / base_feat['lxr_num']
        base_feat['nb_lxr_chs_num'] = base_feat['cnt'] - base_feat['chs_lxr_num']

        base_feat['chs_num'] = (base_feat['cnt'] + base_feat['chs_lxr_num']) / base_feat['lxr_num']

        base_feat['concat_apply_pct'] = base_feat['concat_apply_num'] / base_feat['lxr_num']
        base_feat['concat_apply_pass_reg'] = base_feat['concat_apply_pass_num'] / base_feat['concat_apply_num']
        base_feat['concat_apply_overdue_reg'] = base_feat['concat_apply_overdue_num'] / base_feat['concat_apply_num']
        base_feat['concat_apply_od_pct'] = base_feat['concat_apply_pass_od_num'] / base_feat['concat_apply_num']

        columns = [i.rstrip() for i in self.feat]
        return base_feat[columns]

    def predict(self, data: dict):
        """
        输出逾期概率
        """
        if len(data['appList']) == 0:
            log.logger.warning('appList is empty')
            return -1
        elif len(data['addList']) == 0:
            log.logger.warning('addList is empty')
            return -1
        else:
            base_feat = pd.DataFrame(self.__base_feat(data))
            res_feat = self.__trend_feat(base_feat)
            res_feat.fillna(0, inplace=True)
            prob = np.nanmean([i.predict(res_feat) for i in self.model], axis=0)[0]
            return prob
