import os
import os.path
from scapy.all import *
import subprocess
import sys
import commands


class pckgcheck:

    packages = ['awk','tcpflow',
            'tcpdump','ngrep3']

    @property
    def packageCheck(packages):
        string=""
        missingpck = []
        for item in packages.packages:
            string += " {0}".format(item)
        cmd = "dpkg-query -l " + string + "> a.out 2>&1"
        test= subprocess.Popen(cmd, shell=True)
        #output = subprocess.check_output(test.stdout)
        f = open('a.out')
        try:
            for line in f.readlines():
                if "dpkg-query:" in line:
                    missingpck.insert(0,line.split(" ")[5].split("\n")[0])
        #print "All packages are ok"
        finally:
            f.close()
        return missingpck