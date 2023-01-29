import re
import sys
import os
import time
import os.path
from os import path
import ipcalc
class xcol:
    LGREEN = '\033[38;2;129;199;116m'
    LRED = '\033[38;2;239;83;80m'
    RESET = '\u001B[0m'
    LBLUE = '\033[38;2;66;165;245m'
    GREY = '\033[38;2;158;158;158m'

if __name__ == '__main__':
   while(True):
      try:
         inpFile = input(xcol.GREY+"[URLS PATH] : "+xcol.RESET)
         with open(inpFile) as urlList:
            argFile = urlList.read().splitlines()
         break
      except:
         pass
   for data in argFile:
      subnet = ipcalc.Network(data)
      with open('ranged.txt', 'a') as f:
         for x in subnet:
            f.write(f"{x}\n")
         