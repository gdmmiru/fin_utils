from GDMUtils import *


if __name__ == "__main__":
  print "running test_cme_histvol"
  gdm_utils = GDMUtils()
  data = dict()
  data['20080302'] = 18.0
  data['20080303'] = 18.270
  data['20080304'] = 17.750
  data['20080305'] = 17.900
  data['20080306'] = 17.790
  data['20080307'] = 17.310
  data['20080310'] = 17.750
  data['20080311'] = 18.500
  data['20080312'] = 18.950
  data['20080313'] = 19.000
  data['20080314'] = 18.300
  data['20080317'] = 17.930
  data['20080318'] = 18.430
  data['20080319'] = 18.025
  data['20080320'] = 18.035
  data['20080324'] = 18.535
  data['20080325'] = 19.035
  data['20080326'] = 19.220
  data['20080327'] = 19.305
  data['20080328'] = 19.675
  data['20080331'] = 19.690

  gdm_utils.printN()
  gdm_utils.calc_cme_hv_annual(data)


  vols = gdm_utils.calc_cme_hv_annual2(data,5)
  for key in sorted(vols.keys()):
    print key + "|"+ str(vols[key])

  print "**************************************************"
