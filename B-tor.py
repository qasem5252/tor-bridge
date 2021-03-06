#!/usr/bin/python3
import time
import platform
import os
from colorama import Fore
from colorama import init

init(autoreset=True)
from subprocess import call, PIPE, check_call


class Config_Tor(object):
    def __init__(self):
        self.torrc = "/etc/tor/torrc"
        self.report_t = r''''''
        self.text_1 = r''' 
UseBridges 1
ClientTransportPlugin obfs3 exec /usr/bin/obfsproxy managed
ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy managed
'''
        self.text_2 = r'''
Bridge obfs4 161.97.248.185:9030 E795F5705ADF1EC8A9A525E2AA82CABF025457A0 cert=Y5WYkpNJ+tHaeMawMfmYUWAZekysqHXX856uW5q6BWrJQVEydVzVFkID/2bUgVeGLYmvLg iat-mode=0
Bridge obfs4 125.212.251.104:6666 60B0409FF87E05CD1C88A7FB01E221E54A05EEA4 cert=K8j50CA2dN9mNF0sHB5nfI/AUMUxJumJejv7gl9IaIsJ2vS0icfexHJygze9/sXlimTAJQ iat-mode=0
Bridge obfs4 95.216.186.68:1192 CD6A3B2F22509345DB47F64B2A26FB6A601A1FA0 cert=1gRAX5LV2NQGphZgGTwQumnh01/LwThkRbUmiX7wwAJARWxx2hjBAT3dhbpy/QoyqRmZHg iat-mode=0
'''

        self.banner_t = r"""     

                    ++++                         #
                    +++++++++++++++++++++++++++++++++++++++++++++++++++++

            """

    def banner(self):
        for x in self.banner_t:
            print(Fore.LIGHTCYAN_EX + x, end='', flush=True)
            time.sleep(0.002)
        print()

    #=====================================

    def is_obfsproxy(self):
        x = call("ls /usr/bin/ | grep obfsproxy", shell=True, stdin=PIPE)
        if x == 0:
            return True
            # print("y")
        else:
            # print("n")
            return False

    def is_obfs4proxy(self):
        x = call("ls /usr/bin/ | grep obfs4proxy", shell=True, stdin=PIPE)
        if x == 0:
            return True
        else:
            return False

    def getMachine(self):
        x = platform.machine()
        if x.strip() == 'x86_64':
            return '64'
        else:
            return '32'

    def ins_obfsproxy(self):
        try:
            call(["sudo", "dpkg", "-i", "obfs/obfsproxy_all.deb"], stdout=PIPE)
        except:
            pass

    def ins_obf4sproxy_64(self):
        try:
            # call(["sudo", "dpkg", "-i", "obfs/obfs4proxy_amd64.deb"], stdout=PIPE)
            call(["sudo", "apt", "install", "./obfs/obfs4proxy_amd64.deb","-y"], stdout=PIPE)
        except:
            pass

    def ins_obf4sproxy_32(self):
        try:
            # call(["sudo", "dpkg", "-i", "obfs/obfsproxy_all.deb"], stdout=PIPE)
            call(["sudo","apt", "install", "./obfs/obfsproxy_all.deb", "y"], stdout=PIPE)

        except:
            pass

    #=====================================

    def install_obfs4proxy(self):
        try:
            # call(["sudo", "apt-get", "install", "obfs4proxyxxxx", "-y"], stdout=PIPE)
            if self.is_obfs4proxy() != True:
                if self.getMachine() == '64':
                    self.ins_obf4sproxy_64()
                    print(Fore.LIGHTGREEN_EX + "[✅] Install obfs4proxy [✅]")
                else:
                    self.ins_obf4sproxy_32()
                    print(Fore.LIGHTGREEN_EX + "[✅] Install obfs4proxy [✅]")
            else:
                print(Fore.LIGHTGREEN_EX + "[✅] obfs4proxy exists [✅]")
        except:
            pass
    def install_obfsproxy(self):
        try:
            # call(["sudo", "apt-get", "install", "obfsproxyxxxx", "-y"], stdout=PIPE)
            if self.is_obfsproxy() != True:
                self.ins_obfsproxy()
                print(Fore.LIGHTGREEN_EX + "[✅] Install obfsproxy [✅]")
            else:
                print(Fore.LIGHTGREEN_EX + "[✅] obfsproxy exists [✅]")

        except:
            self.ins_obfsproxy()


    def check_to_text(self):
        check = open(self.torrc, "r").read()
        if (self.text_1.strip() in check) and (self.text_2.strip() in check):
            return True
        else:
            return False


    def check_text_one(self):
        check = open(self.torrc, "r").read()
        if self.text_1.strip() in check:
            pass
        else:
            check1 = open(self.torrc, "a")
            check1.write(self.text_1.strip() + "\n")

    def check_text_tow(self):
        check2 = open(self.torrc, "r").read()
        if self.text_2.strip() in check2:
            pass
        else:
            check2 = open(self.torrc, "a")
            check2.write(self.text_2.strip() + "\n")

    def text_exiest(self):
        for x in self.report_t:
            print(Fore.LIGHTMAGENTA_EX + x, end='', flush=True)
            time.sleep(0.003)
        print()

if __name__ == '__main__':

    T = Config_Tor()
    T.banner()
    # if T.is_obfs4proxy() != True:
    T.install_obfs4proxy()
    # if T.is_obfsproxy() != True:
    T.install_obfsproxy()

    if T.check_to_text():
        T.text_exiest()
    else:
        T.check_text_one()
        T.check_text_tow()
        call(["service", "tor", "restart"])
        print(Fore.LIGHTGREEN_EX + "[✅] Successfully configured [✅] ")


