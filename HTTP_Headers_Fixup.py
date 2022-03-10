#! /usr/bin/env python

# -- Example returning Datatime and hex output ---------------

import time
import os,sys

# print time.time()
# print int(time.time())
# print hex(int(time.time()))
class ChangeDate:
    def __init__(self, parent):
      self._parent = parent
        
    def fixup(self, element):
      ISOTIMEFORMAT = '%Y%m%dT%H%M%SZ'
      serverTime = time.strftime(ISOTIMEFORMAT, time.gmtime(time.time()))
      return str(serverTime)


# end


