from time import strftime
from datetime import datetime

class FTLogger:
  def __init__(self):
    pass

  def Debug(self,line):
    print "["+datetime.now().isoformat()+"][DEBUG] " + line

  def Info(self,line):
    print "["+datetime.now().isoformat()+"][INFO] " + line

  def Warn(self,line):
    print "["+datetime.now().isoformat()+"][WARN] " + line

  def Error(self,line):
    print "["+datetime.now().isoformat()+"][ERROR] " + line

  def Fatal(self,line):
    print "["+datetime.now().isoformat()+"][FATAL] " + line


