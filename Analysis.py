__author__ = 'zach'

from pandas import DataFrame as Df

supreme_court_decisions = Df.from_csv('./Supreme Court.txt', sep='\t')

print len(supreme_court_decisions[supreme_court_decisions['Federal Government'] == 1])
print len(supreme_court_decisions[supreme_court_decisions['Charter Right'] == 1])
