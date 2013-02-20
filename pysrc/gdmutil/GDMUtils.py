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

  #calcs the annualized historical vol for the specified number of days
  def calc_cme_hv_annual2(self, data, days=30):
    trading_days_factor = math.sqrt(252)
    ln_of_returns = list()
    sorted_keys = sorted(data.iterkeys())
    prior_settle_px = data[sorted_keys[0]]
    vols = dict()
    curr_idx = 0
    trailing_idx = 0

    for key in sorted_keys[1:]:
      settle_px = data[key]
      ln_of_returns.append(math.log(settle_px/prior_settle_px))

      #set variables
      if(len(ln_of_returns) >= days):
        vol = np.std(ln_of_returns[trailing_idx:curr_idx])*trading_days_factor
        vols[key] = vol
        curr_idx += 1
      curr_idx += 1
      prior_settle_px = settle_px

    return vols


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
