import subprocess
import re
import sys
import os


class netcommands():

    def getnetstr(self):
        if os.name == 'nt':
            try:
                result = subprocess.check_output(['netsh','wlan','show','interfaces']).decode(sys.stdout.encoding)
            except subprocess.CalledProcessError as err:
                print('netsh Command error' + err)
                exit(1)
            ssid,strength = self.parsenetsh(result)
        elif os.name == 'posix':
            try:
                result = subprocess.check_output(['iwconfig']).decode(sys.stdout.encoding)
            except subprocess.CalledProcessError as err:
                print('iwconfig Command error ' + err)
                exit(1)
            ssid,strength = self.parseiwconfig(result)
        else:
            ssid = 'error'
            strength = '0'
        
        return ssid,strength

    def parsenetsh(self,string):
        match1 = re.search('Signal.+: (\d{1,3}%)',string)
        strength = match1.group(1)

        match2 = re.search('SSID.+: (.+)',string)
        ssid = match2.group(1)

        return ssid,strength
    
    def parseiwconfig(self,string):
        match1 = re.search('Signal level=(-\d{1,3} dBm)',string)
        strength = match1.group(1)
        
        match2 = re.search('SSID:\"(.+)\"',string)
        ssid = match2.group(1)
        
        return ssid,strength

if __name__ == "__main__":
    nc = netcommands()
    ssid,strength = nc.getnetstr()
    print('SSID: ' + ssid + ', Strength: ' + strength)
