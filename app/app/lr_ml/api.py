# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 6:49 下午
# @Author  : HuangSir
# @FileName: api.py
# @Software: PyCharm
# @Desc: 新客信用分模型主程序

from conf.log_config import log

from app.app.applist_ml.applist_model import AppListML
from app.app.lr_ml.lr_model import LrModel

appModel = AppListML()
lrModel = LrModel()


def lr_ml_main(data):
    customerId = data['customerId']
    loanAppId = data['loanAppId']
    ml_data = data['data']
    try:
        log.logger.info(f'{loanAppId}:starting lr --------------------------------')
        prob = appModel.predict(ml_data)
        ml_data['prob'] = prob
        log.logger.info(f'get appModel prob:{round(prob, 4)}')

        score_point = lrModel.predict(data=ml_data)
        log.logger.info(f'get lrModel score:{score_point["score"]}')
        log.logger.info(f'{loanAppId}:finished lr --------------------------------\n')

        return {'customerId': customerId, 'loanAppId': loanAppId,
                'appProb': round(prob, 4), 'lrScorePoint': score_point,
                'code': 100, 'msg': '处理成功', 'detail': '', 'version': 'v3'}
    except Exception as error:
        log.logger.error(f'{loanAppId},-----> {str(error)}')
        return {'customerId': customerId, 'loanAppId': loanAppId,
                'code': 101, 'msg': '处理失败', 'detail': str(error), 'version': 'v3'}
