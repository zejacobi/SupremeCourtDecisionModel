__author__ = 'zach'

from pandas import DataFrame as Df

supreme_court_decisions = Df.from_csv('./Supreme Court.txt', sep=r'\t', header=1)
