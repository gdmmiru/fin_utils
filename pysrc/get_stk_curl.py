#!/usr/bin/python
# filename: get_stks_via_curl.py
# purpose : retrieves stock data from finance.yahoo using curl, dumps them to a
#           csv file in the current dir
# changes : 01.03.2012 - initial commit

# define imports
import os

#symbols = ['AA', 'GOOG','SDS', 'FB', 'GLD', 'SIRI', 'AMZN', 'SPY']
symbols = ['APOL']
#symbols from washington post, historical
#symbols = ['COG', 'MA', 'BIIB', 'CMG', 'PRGO', 'ROST']
begin_month = 0
end_month = 11
begin_date = 1
end_date = 31
begin_year = 2011
end_year = 2011

cmd = "curl"

for sym in symbols:
  query = """ "http://ichart.finance.yahoo.com/table.csv?a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=d&ignore=.csv&s=%s" """ %\
  (begin_month, begin_date, begin_year, end_month, end_date, end_year, sym)

  print query
  filename = "data.%s.csv" %(sym)
  fullquery = "%s %s > %s" %(cmd, query, filename)
  print "fullquery:" + fullquery
  os.system(fullquery)

print "exiting...."
