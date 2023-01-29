import re
import sys
import os
import time
import socket
import urllib3
import json
import os.path
import requests
from os import path
from concurrent.futures import ThreadPoolExecutor
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class xcol:
    LGREEN = '\033[38;2;129;199;116m'
    LRED = '\033[38;2;239;83;80m'
    RESET = '\u001B[0m'
    LBLUE = '\033[38;2;66;165;245m'
    GREY = '\033[38;2;158;158;158m'

class ASN :
   def scan (self, asn):
      str = "";
      try:
         r = requests.get(f'https://api.bgpview.io/asn/{asn}/prefixes', verify=False, timeout=10, allow_redirects=False)
         resp = r.text
         rn = ""
         obj = json.loads(resp)
         obj2 = json.dumps(obj["data"])
         obj3 = json.loads(obj2)
         obj4 = json.dumps(obj3["ipv4_prefixes"])
         oc = re.sub(".*\"prefix\":\"","prefix::",obj4.replace("{",""). replace ("}","").replace("[",""). replace ("]","").replace(",","\n"). replace (" ","")). replace ("\"","")
         cv = oc.splitlines()
         for cn in cv:
            if "prefix::" in cn :
               rn = rn+cn+"\n"
         sasn = rn.replace("prefix::","")
         with open(os.path.join('', f'Ipv4.txt'), 'a', encoding='utf-8') as output:
            output.write(f'{sasn}')
         print(f"ASN : {asn}")
      except Exception as e :
            print(f"ERROR : {e}")
      
if __name__ == '__main__':
   os.system('clear')
   threads = []
   while(True):
      try:
         thrd = int(input(xcol.GREY+"[THREAD] : "+xcol.RESET))
         break
      except:
         pass
   while(True):
      try:
         inpFile = input(xcol.GREY+"[ASN LIST] : "+xcol.RESET)
         with open(inpFile) as urlList:
            argFile = urlList.read().splitlines()
         break
      except:
         pass
   with ThreadPoolExecutor(max_workers=thrd) as executor:
      for data in argFile:
         threads.append(executor.submit(ASN().scan, data))
   quit()