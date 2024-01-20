import subprocess
import re
import sys


class netcommands():

    def getnetsh(self):
        try:
            result = subprocess.check_output(['netsh','wlan','show','interfaces']).decode(sys.stdout.encoding)
        except subprocess.CalledProcessError as err:
            print('netsh Command error' + err)
            exit(1)
        ssid,strength = self.findstrength(result)
        return ssid,strength

    def findstrength(self,string):
        match1 = re.search("Signal.+: (\d{1,3})%",string)
        strength = match1.group(1)

        match2 = re.search("SSID.+: (.+)",string)
        ssid = match2.group(1)

        return ssid,strength

if __name__ == "__main__":
    nc = netcommands()
    ssid,strength = nc.getnetsh()
