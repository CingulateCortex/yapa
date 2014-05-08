#!/usr/bin/python

import os
import errno
import sys
from lib.yapalib import yapalib
import subprocess

sys.path.append('/utilis/color_class.py')
from utilis.color_class import bcolors
from utilis.additions import additions

a = yapalib()
add = additions()
path = "results"

add.mkdir_p(path)
filename = sys.argv[1]


add.welcome()
print bcolors.HEADER + "Welcome to YAPA Pcap Analyzer"+ bcolors.ENDC
#print add.menu()
add.menu()




#dict = {"1":a.top_talkers(filename, "a.out")}
while True:
    num = raw_input(bcolors.WARNING + "Make your choice \n" + bcolors.ENDC)
    if num == "1":
        print bcolors.OKBLUE + "Reading PCAP file.. " + bcolors.ENDC
        a.top_talkers(filename,"top_talkers.out")
        print bcolors.OKGREEN + "The results of Top Talkers is under results folder\n" + bcolors.ENDC
    elif num == "2":
        a.hos_of_ip_traffic(filename,"host_of_ip_traffic.out")
    elif num =="3":
        a.show_hierarcy(filename,"show_hierarchy.out")
    elif num == "4":
        a.traffic_dest_port(filename,"traffic_dest_port.out")
    elif num == "5":
        a.show_syn_packets(filename,"syn_packages.out")
    elif num == "6":
        a.show_user_agents(filename,"user_agents.out")
    elif num == "7":
        a.show_dns_traffic(filename,"dns_traffic.out")
    elif num == "8":
        a.search_mail_pattern(filename,"any_mail.out")
    elif num == "9":
        a.show_any_tcp_connection(filename,"tcp_communication.out")
    elif num == "10":
        a.all_http_traffic(filename, "all_http_traffic.out")
    elif num == "11":
        a.top_talkers(filename,"top_talkers.out")
    elif num == "12":
        strn = raw_input("Enter your string the search in PCAP \n")
        while True:
            strn = raw_input("Enter your string the search in PCAP \n")
            if strn == "q":
                break
            else:
                a.search_string(filename,"search_result.out", strn)
    elif num=="13":
        rgxtxt = raw_input("Enter your Regex\n")
        a.search_regex(filename,"regex.out",rgxtxt)
    elif num=="14":
        break
    else:
        add.errorMessage()




