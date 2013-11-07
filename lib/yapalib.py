#!/bin/env python
import os
import os.path
from scapy.all import *
import subprocess
import sys


class yapalib:

    def hos_of_ip_traffic(self,filepcap,path):

        cmd = "tshark -r %s -q -z hosts,ipv4 > results/%s" %(filepcap,path)
        subprocess.call(cmd, shell=True)

    def show_hierarcy(self,filepcap,path):
        cmd = "tshark -r %s -q -z io,phs > results/%s" %(filepcap,path)
        subprocess.call(cmd, shell=True)

    def traffic_dest_port(self,filepcap,path):
        cmd = "tshark -o column.format:'\"Source\", \"%s\", \"Destination\", \"%d\", \"dstport\", \"%uD\"' -r {} |sort|uniq > results/{}" .format(filepcap,path)
        subprocess.call(cmd,shell=True)

    def top_talkers(self,filepcap,path):
        cmd2= "tcpdump -tnr %s |awk -F '.' '{print $1\".\"$2\".\"$3\".\"$4}' | sort | uniq -c | sort -n | tail > results/%s 2>&1" %(filepcap,path)
        subprocess.call(cmd2,shell=True)

    def all_conversation(self,filepcap,path):
        cmd = "tshark -o column.format:'\"Source\", \"%s\", \"Destination\", \"%d\", \"dstport\", \"%uD\"' -r {} |sort|uniq >results/{}".format(filepcap,path)
        subprocess.call(cmd,shell=True)

    def show_user_agents(self,filepcap,path):

        cmd= "tcpdump -Ann -r %s 'port 80' | grep -Ei 'user-agent' |sort |uniq -c |sort -n > results/%s " %(filepcap,path)
        subprocess.call(cmd, shell=True)

    def all_http_traffic(self,filepcap,path):

        cmd = "tcpdump -Ann -r %s 'dst port 80' > results/%s"%(filepcap,path)
        subprocess.call(cmd, shell=True)

    def show_syn_packets(self,filepcap,path):
        cmd = "tshark -r %s tcp.flags.syn eq 0x1 > results/%s "%(filepcap,path)
        subprocess.call(cmd, shell=True)

    def search_string(self,filepcap, path, strn):

        cmd = "ngrep -q -I %s |grep -i '%s' > results/%s" %(filepcap,strn, path)
        subprocess.call(cmd, shell=True)

    def search_mail_pattern(self,filepcap,path):
        cmd = "ngrep -q -I %s '[a-zA-Z0-9.]+\.?@[a-zA-Z0-9.]+\.[a-zA-Z0-9]+' |grep -Eo '[a-zA-Z0-9.]+\.?@[a-zA-Z0-9.]+\.[a-zA-Z0-9]+'|sort|uniq > results/%s" %(filepcap,path)
        subprocess.call(cmd,shell=True)

    def show_any_tcp_connection(self,filepcap,path):

        cmd = "tcpick -r %s -yP \"port 25\" > results/%s" %(filepcap,path)
        subprocess.call(cmd, shell=True)

    def show_dns_traffic(self,filepcap,path):

        cmd = " tcpdump -Ann -r %s 'dst port 53' | grep  '(com|in|org)'>results/%s " %(filepcap,path)
        subprocess.call(cmd, shell= True)