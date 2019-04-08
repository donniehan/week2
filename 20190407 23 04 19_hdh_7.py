# coding=utf8
__author__ = 'wangjp'

import time

import numpy as np
import pandas as pd
from FactorModule.FactorBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t


class Factor(FactorBase):

    # def __init__(self, not_run=0):
    def __init__(self):
        # print('not_run', not_run)
        # if not_run == 0:
        super(Factor, self).__init__()
        self.neutral = False
        self.factorName = __name__.split('.')[-1]
        self.needFields = [t.SELL_VOLUME_EXLARGE_ORDER_ACT, t.S_MFD_INFLOW_CLOSEVOLUME, t.PCFOCFTTM]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData                                # 计算所需数据

        factor = -((needData[t.SELL_VOLUME_EXLARGE_ORDER_ACT]*needData[t.S_MFD_INFLOW_CLOSEVOLUME])**0.5 - needData[t.PCFOCFTTM])

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()


#if __name__ == '__main__':
fct = Factor()
fct.run_factor()
