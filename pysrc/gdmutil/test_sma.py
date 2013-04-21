from GDMUtils import *
import datetime

print "runnint test_sma.py"

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

data2 = dict()

for key in data.keys():
  data2[datetime.datetime.strptime(key,"%Y%m%d")] = data[key]

sma_d5 = gdm_utils.calc_sma(data, 5)

for key in sorted(sma_d5.keys()):
  print key + "|" + str(sma_d5[key])

sma_d5a = gdm_utils.calc_sma(data2, 5)
for key in sorted(sma_d5a.keys()):
  print key.isoformat() + "|" + str(sma_d5a[key])


