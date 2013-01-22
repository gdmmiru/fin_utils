#!/usr/bin/python
# filename: get_stk_curl.py
# purpose : retrieves stock data from finance.yahoo using curl, dumps them to a
#           csv file in the current dir
# notes   : requires curl installed
# changes : 01.03.2012 - initial commit

# define imports
import os
import getopt
import sys
from datetime import datetime
from subprocess import Popen, PIPE


import ftutil.MongoDBManager as MongoDBManager
import ftutil.FTLogger as FTLogger

#### define methods
def usage():
  print ""
  print "get_stk_curl.py "
  print "-i, --ip       ip of target mongodb"
  print "-s, --stocks   comma separated list for all interested stocks"
  print "-f, --file     file listing stocks to retrieve"
  print "-d, --dump     dump to csv file"
  print "-h, --help     displays this help menu"
  print ""

def get_symbol_info_to_csv(symbol):
  g_logger.Info('called get_symbol_info ' + symbol)
  (byear, bmonth, bdate) = (2012, 0, 1)
  (eyear, emonth, edate) = (2012, 11, 31)
  query = """ "http://ichart.finance.yahoo.com/table.csv?a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=d&ignore=.csv&s=%s" """ %\
    (bmonth, bdate, byear, emonth, edate, eyear, sym)

  print query
  filename = "data.%s.csv" %(sym)
  fullquery = "%s %s > %s" %(exename, query, filename)
  print "fullquery:" + fullquery
  os.system(fullquery)

def get_symbol_info(symbol):
  g_logger.Info('called get_symbol_info ' + symbol)
  #get data starting from jan 2000 until now.... mite be a bit too much, but okay for now
  (byear, bmonth, bdate) = (2000, 0, 1)
  today = datetime.now()
  eyear = today.year
  emonth = today.month -1 #yahoo month starts at 0
  edate = today.day
  query = """http://ichart.finance.yahoo.com/table.csv?a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=d&ignore=.csv&s=%s""" %\
    (bmonth, bdate, byear, emonth, edate, eyear, sym)

  filename = "data.%s.csv" %(sym)
  fullquery = "%s %s" %(exename, query)
  g_logger.Info("get_symbol_info fullquery:"+fullquery)
  process = Popen([exename, query], stdout = PIPE)
  output = process.communicate()[0]
  lines = output.split("\n")
  header = lines[0]
  datalist = list()
  for line in lines[1:]:
    vals = line.split(",")
    if(len(vals) != 7):
      continue
    d = dict()
    d['date'] = vals[0]
    d['open'] = vals[1]
    d['high'] = vals[2]
    d['low'] = vals[3]
    d['close'] = vals[4]
    d['volume'] = vals[5]
    d['adj_close'] = vals[6]
    datalist.append(d)
  return datalist

def get_coll_key(symbol):
  return symbol+":S"

def remove_and_insert_to_mongo_db(symbol,data):
  mongodb = MongoDBManager.MongoDBManager(g_ip,27017)
  mongodb.sel_db("hist_data")
  mongodb.sel_coll('hist_px', get_coll_key(symbol))
  mongodb.remove_coll()
  mongodb.insert_doc(data)
  mongodb.retrieve_doc()

def blind_insert_to_mongo_db(symbol,data):
  mongodb = MongoDBManager(g_ip,27017)
  mongodb.sel_db("hist_data")
  mongodb.sel_coll('hist_px', get_coll_key(symbol))
  mongodb.insert_doc(data)

#### define the default values
g_symbols = ['AAPL']
#symbols from washington post, historical
#g_symbols = ['COG', 'MA', 'BIIB', 'CMG', 'PRGO', 'ROST']

exename = "curl"
g_logger = FTLogger.FTLogger()
g_ip = "localhost"
g_file = None

#### parse out the arguments
options, remainder = getopt.getopt(sys.argv[1:], 'i:s:f:b:e:dvh',
    ['ip=='
     'stocks=',
     'file='
     'begdate=',
     'enddate=',
     'dump',
     'version',
     'help'])

print 'OPTIONS    :', options

begdate = ""
enddate = ""
dump = False

for opt, arg in options:
  if(opt in ('-i', '--ip')):
    g_ip = arg
  elif(opt in ('-s', '--stocks')):
    g_symbols = arg.split(',')
  elif(opt in ('-f', '--file')):
    g_file = arg
  elif opt in ('-b', '--begdate'):
    begdate = arg
  elif opt in ('-e', '--enddate'):
    enddate= arg
  elif opt in ('-v', '--version'):
    print "Version is 1.0.0"
    sys.exit(0)
  elif opt in ('-d', '--dump'):
    dump = True
  elif opt in ('-h', '--help'):
    usage()
    sys.exit(0)

byr = begdate[0:3]
bmn = begdate[4:5]
bdate = begdate[6:]

g_logger.Info( "preparsed date:" + begdate)
g_logger.Info( "parsed date:"+ byr + bmn + bdate)

#if a filename is set, read the stock names, assume a stock per line
if(g_file != None):
  fileHandle = open(g_file)
  g_symbols = []
  for line in fileHandle.readlines():
    g_symbols.append(line.rstrip())
  fileHandle.close()


#run through each symbol name, curl yahoo and then push to mongodb
for sym in g_symbols:
  if(dump == True):
    get_symbol_info_to_csv(sym)
  else:
    datalist = get_symbol_info(sym)
    remove_and_insert_to_mongo_db(sym, datalist)


g_logger.Info("exiting....")
