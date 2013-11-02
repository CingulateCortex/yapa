#!/usr/bin/env python

import os
import errno
from color_class import bcolors
from lib.yapalib import yapalib


class additions:

    def welcome(self):
        os.system("clear")
        print "=========================================="
        print "      http://www.cingulatecortex.com      "
        print "=========================================="
        print "        Yet Another Pcap Analyzer         "
        print "=========================================="
        print "          Kubilay Onur GUNGOR             "
        print "=========================================="


    def mkdir_p(self,path):
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    def errorMessage(self):
        print "Incorrect Input\n"


    def menu(self):
        a = yapalib()


        print bcolors.OKBLUE + "1- Top Talkers\n" \
              "2- Hosts in Traffic\n" \
              "3- Show Hierarchy\n" \
              "4- Traffic with Destination Port\n" \
              "5- Show SYN Packets\n" \
              "6- Show User Agents\n" \
              "7- Show DNS Traffic\n" \
              "8- Show Any Mail\n" \
              "9- Show Any TCP Communication\n" \
              "10- Show All HTTP Traffic\n" \
              "11- Run All\n" \
              "12 - Quit"