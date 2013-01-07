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

#### define methods

def usage():
  print ""
  print "get_stk_curl.py "
  print "-s, --stocks   comma separated list for all interested stocks"
  print "-h, --help     displays this help menu"
  print ""

def get_symbol_info(symbol):
  print 'called get_symbol_info ' + symbol
  (byear, bmonth, bdate) = (2012, 0, 1)
  (eyear, emonth, edate) = (2012, 11, 31)
  query = """ "http://ichart.finance.yahoo.com/table.csv?a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=d&ignore=.csv&s=%s" """ %\
    (bmonth, bdate, byear, emonth, edate, eyear, sym)

  print query
  filename = "data.%s.csv" %(sym)
  fullquery = "%s %s > %s" %(exename, query, filename)
  print "fullquery:" + fullquery
  os.system(fullquery)

#### define the default values
symbols = []
#symbols from washington post, historical
#symbols = ['COG', 'MA', 'BIIB', 'CMG', 'PRGO', 'ROST']

exename = "curl"

#### parse out the arguments
options, remainder = getopt.getopt(sys.argv[1:], 's:b:e:vh', ['stocks=',
                                                              'version',
                                                              'begdate=',
                                                              'enddate=',
                                                              'help'])
print 'OPTIONS    :', options

begdate = ""
enddate = ""

for opt, arg in options:
  if(opt in ('-s', '--stocks')):
    symbols = arg.split(',')
  elif opt in ('-b', '--begdate'):
    begdate = arg
  elif opt in ('-e', '--enddate'):
    enddate= arg
  elif opt in ('-v', '--version'):
    print "Version is 1.0.0"
    sys.exit(0)
  elif opt in ('-h', '--help'):
    usage()
    sys.exit(0)

byr = begdate[0:3]
bmn = begdate[4:5]
bdate = begdate[6:]
print "preparsed date:" + begdate
print "parsed date:"+ byr + bmn + bdate


for sym in symbols:
  get_symbol_info(sym)

print "exiting...."
