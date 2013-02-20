import math
import numpy as np

class GDMUtils:
  def __init__(self):
    pass

  def printN(self):
    print "GDMUtils::printN()"

  #formula off of cmegroup.com website
  def calc_cme_hv_annual(self, data):

    trading_days_factor = math.sqrt(252)
    list_of_ln_returns = list()
    sorted_keys = sorted(data.iterkeys())
    prior_settle_px = data[sorted_keys[0]]

    for key in sorted_keys[1:]:
      settle_px = data[key]
      list_of_ln_returns.append(math.log(settle_px/prior_settle_px))
      prior_settle_px = settle_px

    cme_volatility = np.std(list_of_ln_returns) * trading_days_factor
    print "GDMUntils::calc_cme_histvol cme_volatility:" + str(cme_volatility)
    return cme_volatility

  def calc_cme_hv_daily(self, data, days):
    trading_days_factor = math.sqrt(252)
    list_of_ln_returns = list()
    sorted_keys = sorted(data.iterkeys())
    prior_settle_px = data[sorted_keys[0]]

    for key in sorted_keys[1:]:
      settle_px = data[key]
      list_of_ln_returns.append(math.log(settle_px/prior_settle_px))
      prior_settle_px = settle_px

    cme_volatility = np.std(list_of_ln_returns) * trading_days_factor
    print "GDMUntils::calc_cme_histvol cme_volatility:" + str(cme_volatility)
    return cme_volatility


  def calc_rsi(self, data, pxKey):
    pass
